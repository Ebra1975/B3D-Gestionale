from celery import shared_task


@shared_task
def generate_document(generated_document_id):
    # Placeholder: document generation will be wired after the first DOCX template is defined.
    return {"generated_document_id": generated_document_id, "status": "placeholder"}
