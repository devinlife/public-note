from pathlib import Path

from utils.file_descriptor import FileDescriptor
from utils.file_output_dto import FileOutputDto


def create_file_descriptors_from_dtos(files: FileOutputDto, base_dir_name, relative_path) -> list[FileDescriptor]:
    return [create_file_descriptor_from_dto(file, base_dir_name, relative_path) for file in files]


def create_file_descriptor_from_dto(file: FileOutputDto, base_dir_name, relative_path) -> FileDescriptor:
    return FileDescriptor(
        filepath=str(Path(relative_path) / Path(file.key).name),
        url=file.download_url,
        base_path_local=base_dir_name,
    )
