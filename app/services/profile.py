import os
from app.models.profile import Profile

UPLOAD_DIRECTORY = "uploads/profile_images"


def save_profile_image(profile: Profile, image_file):
    """
    Save the image file to the local directory and update the image field of the profile.
    """
    if not os.path.exists(UPLOAD_DIRECTORY):
        os.makedirs(UPLOAD_DIRECTORY)

    # Generate a unique filename
    filename = f"{profile.id}_{image_file.filename}"
    file_path = os.path.join(UPLOAD_DIRECTORY, filename)

    # Save the file
    with open(file_path, "wb") as buffer:
        buffer.write(image_file.file.read())

    # Update the image field with the file path
    profile.image = file_path
    profile.save()


def delete_profile_image(profile: Profile):
    """
    Delete the image file and clear the image field of the profile.
    """
    if profile.image and os.path.exists(profile.image):
        os.remove(profile.image)
    profile.image = None
    profile.save()


def get_profile_image_path(profile: Profile):
    """
    Get the path of the profile image.
    """
    return profile.image if profile.image and os.path.exists(profile.image) else None
