

def get_image_path(instance, filename: str) -> str:
    """
    :param instance: User instance
    :param filename: Name of file
    :return: Path for saving user images
    """
    return f'users/{instance.user.pk}/profile_images/{filename}'
