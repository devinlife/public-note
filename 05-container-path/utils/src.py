from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class VolumeDescriptor:
    relative_path: str
    base_path_local: str
    base_path_container: Optional[str] = None

    @property
    def local_path(self) -> Path:
        return Path(self.base_path_local) / self.relative_path

    @property
    def container_path(self) -> Optional[Path]:
        if self.base_path_container:
            return Path(self.base_path_container) / self.relative_path
        return None


@dataclass
class FileDescriptor:
    filename: str
    volume: VolumeDescriptor

    def __init__(self, filepath: str, base_path_local: str, base_path_container: Optional[str] = None):
        path_obj = Path(filepath)
        self.filename = path_obj.name
        self.volume = VolumeDescriptor(
            relative_path=str(path_obj.parent), base_path_local=base_path_local, base_path_container=base_path_container
        )

    @property
    def local_filepath(self) -> Path:
        return self.volume.local_path / self.filename

    @property
    def container_filepath(self) -> Optional[Path]:
        if self.volume.container_path:
            return self.volume.container_path / self.filename
        return None

    @property
    def local_path(self) -> Path:
        return self.volume.local_path

    @property
    def container_path(self) -> Optional[Path]:
        if self.volume.container_path:
            return self.volume.container_path
        return None


# 사용 예제
file_info = FileDescriptor(
    filepath="example.txt", base_path_local="/local_machaine/path", base_path_container="/container"
)

print(file_info.local_filepath)  # 출력: /local_machaine/path/specific_path/example.txt
print(file_info.local_path)  # 출력: /local_machaine/path/specific_path
print(file_info.container_filepath)  # 출력: /container/specific_path/example.txt
print(file_info.container_path)  # 출력: /container/specific_path
