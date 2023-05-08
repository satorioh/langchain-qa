import os


def get_abs_path(path: str) -> str:
    current_path = os.path.abspath(__file__)
    dir_name, file_name = os.path.split(current_path)
    parent_dir = os.path.dirname(dir_name)
    return os.path.join(parent_dir, path)
