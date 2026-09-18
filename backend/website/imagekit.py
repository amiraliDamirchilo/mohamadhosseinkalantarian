from pathlib import Path

from django.conf import settings
from django.core.exceptions import ValidationError
from imagekitio import ImageKit


def upload_media(uploaded_file, folder="/portfolio"):
    """Upload an admin-selected image or video to ImageKit and return its metadata."""
    if not settings.IMAGEKIT_PRIVATE_KEY:
        raise ValidationError("ImageKit is not configured. Add IMAGEKIT_PRIVATE_KEY to backend/.env.")
    try:
        # Django stores larger uploads in a TemporaryUploadedFile. ImageKit's
        # SDK accepts a pathlib.Path for those files, but not Django's wrapper.
        # Smaller in-memory uploads are passed as raw bytes.
        if hasattr(uploaded_file, "temporary_file_path"):
            file_data = Path(uploaded_file.temporary_file_path())
        else:
            uploaded_file.seek(0)
            file_data = uploaded_file.read()
        response = ImageKit(private_key=settings.IMAGEKIT_PRIVATE_KEY).files.upload(
            file=file_data,
            file_name=Path(uploaded_file.name).name,
            folder=folder,
            tags=["portfolio"],
        )
        return {"url": response.url, "file_id": response.file_id}
    except Exception as error:
        raise ValidationError(f"ImageKit upload failed: {error}") from error
