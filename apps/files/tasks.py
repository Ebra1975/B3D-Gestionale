from celery import shared_task

from .models import AttachedFile


@shared_task
def process_attached_file(attached_file_id):
    attached_file = AttachedFile.objects.get(pk=attached_file_id)
    attached_file.processing_status = AttachedFile.ProcessingStatus.PROCESSING
    attached_file.save(update_fields=["processing_status", "updated_at"])

    # Placeholder: actual 3MF/G-code extraction will be implemented after sample files are tested.
    attached_file.extracted_metadata = {
        "status": "placeholder",
        "message": "Elaborazione preview/metadati da implementare.",
    }
    attached_file.processing_status = AttachedFile.ProcessingStatus.READY
    attached_file.save(update_fields=["extracted_metadata", "processing_status", "updated_at"])
