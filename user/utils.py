

def get_image_path(instance, filename: str) -> str:
    """
    :param instance: User instance
    :param filename: Name of file
    :return: Path for saving user images
    """
    return f'users/profile_images/{instance.user.pk}/{filename}'
