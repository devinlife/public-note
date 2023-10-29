from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class PathDescriptor:
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
    url: str
    volume: PathDescriptor

    def __init__(self, filepath: str, url: str, base_path_local: str, base_path_container: Optional[str] = None):
        if filepath.startswith("/"):
            raise ValueError(f"filepath should be relative path: {filepath}")

        path_obj = Path(filepath)
        self.filename = path_obj.name
        self.url = url
        self.volume = PathDescriptor(
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


"""
# 사용 예제
file_info = FileDescriptor(
    filepath="relpath/example.txt",
    url="s3/workspace/id/example.txt",
    base_path_local="/local_machaine/path",
    base_path_container="/container",
)

print(file_info.local_filepath)
print(file_info.local_path)  
print(file_info.container_filepath) 
print(file_info.container_path)  
print(file_info.filename)
print(file_info.url)

/local_machaine/path/relpath/example.txt
/local_machaine/path/relpath
/container/relpath/example.txt
/container/relpath
example.txt
s3/workspace/id/example.txt
"""
