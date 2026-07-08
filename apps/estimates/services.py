import re
import zipfile
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from io import BytesIO


@dataclass
class TechnicalFileImportResult:
    source_name: str
    material_weight_kg: Decimal | None = None
    machine_time_hours: Decimal | None = None
    plate_count: int | None = None
    raw_summary: str = ""

    @property
    def has_useful_data(self):
        return any([self.material_weight_kg, self.machine_time_hours, self.plate_count])


def parse_technical_file(uploaded_file):
    source_name = uploaded_file.name
    content = uploaded_file.read()
    uploaded_file.seek(0)

    if source_name.lower().endswith(".3mf"):
        text = _read_3mf_text(content)
    else:
        text = content.decode("utf-8", errors="ignore")

    weight = _extract_weight_kg(text)
    time_hours = _extract_time_hours(text)
    plate_count = _extract_plate_count(text)
    summary = _build_raw_summary(source_name, weight, time_hours, plate_count)

    return TechnicalFileImportResult(
        source_name=source_name,
        material_weight_kg=weight,
        machine_time_hours=time_hours,
        plate_count=plate_count,
        raw_summary=summary,
    )


def _read_3mf_text(content):
    pieces = []
    with zipfile.ZipFile(BytesIO(content)) as archive:
        for name in archive.namelist():
            lower_name = name.lower()
            if lower_name.endswith((".gcode", ".xml", ".config", ".ini", ".txt")):
                pieces.append(archive.read(name).decode("utf-8", errors="ignore"))
    return "\n".join(pieces)


def _extract_weight_kg(text):
    patterns = [
        r"filament used \[g\]\s*=\s*([0-9]+(?:[.,][0-9]+)?)",
        r"total filament used \[g\]\s*=\s*([0-9]+(?:[.,][0-9]+)?)",
        r"filament(?: used)?(?: weight)?\s*[:=]\s*([0-9]+(?:[.,][0-9]+)?)\s*g\b",
        r"filament_weight_mg\s*=\s*([0-9]+(?:[.,][0-9]+)?)",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            value = _decimal(match.group(1))
            if "mg" in pattern:
                return _quantize_weight(value / Decimal("1000000"))
            return _quantize_weight(value / Decimal("1000"))
    return None


def _extract_time_hours(text):
    seconds_patterns = [
        r";?TIME\s*:\s*([0-9]+)",
        r"estimated printing time \(normal mode\)\s*=\s*([0-9]+)s",
    ]
    for pattern in seconds_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return _quantize_hours(_decimal(match.group(1)) / Decimal("3600"))

    readable_patterns = [
        r"estimated printing time.*?=\s*([0-9dhms\s]+)",
        r"print time\s*[:=]\s*([0-9dhms\s]+)",
    ]
    for pattern in readable_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            seconds = _readable_time_to_seconds(match.group(1))
            if seconds:
                return _quantize_hours(Decimal(seconds) / Decimal("3600"))
    return None


def _extract_plate_count(text):
    matches = re.findall(r"\b(?:plate|build plate)\s*(?:count|number)?\s*[:=]\s*([0-9]+)", text, re.IGNORECASE)
    if matches:
        return max(int(value) for value in matches)

    object_matches = re.findall(r"<object\b", text, re.IGNORECASE)
    if object_matches:
        return 1
    return None


def _readable_time_to_seconds(value):
    total = 0
    for amount, unit in re.findall(r"([0-9]+)\s*([dhms])", value, re.IGNORECASE):
        amount = int(amount)
        unit = unit.lower()
        if unit == "d":
            total += amount * 86400
        elif unit == "h":
            total += amount * 3600
        elif unit == "m":
            total += amount * 60
        elif unit == "s":
            total += amount
    return total


def _build_raw_summary(source_name, weight, time_hours, plate_count):
    parts = [f"Import tecnico da {source_name}."]
    if weight:
        parts.append(f"Peso letto: {weight} kg/l per unita.")
    if time_hours:
        parts.append(f"Tempo letto: {time_hours} h per unita.")
    if plate_count:
        parts.append(f"Piatti rilevati: {plate_count}.")
    if len(parts) == 1:
        parts.append("Nessun dato tecnico riconosciuto automaticamente.")
    return " ".join(parts)


def _decimal(value):
    return Decimal(str(value).replace(",", "."))


def _quantize_weight(value):
    return value.quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)


def _quantize_hours(value):
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
