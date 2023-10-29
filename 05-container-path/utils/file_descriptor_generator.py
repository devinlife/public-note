from pathlib import Path

from utils.file_descriptor import FileDescriptor


def get_file_descriptors(files, base_dir_name, relative_path) -> list[FileDescriptor]:
    return [get_file_descriptor(file, base_dir_name, relative_path) for file in files]


def get_file_descriptor(files, base_dir_name, relative_path) -> FileDescriptor:
    return FileDescriptor(
        filepath=str(Path(relative_path) / Path(files.key).name),
        url=files.download_url,
        base_path_local=base_dir_name,
    )
