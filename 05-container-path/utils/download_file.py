import zipfile

import httpx
from utils.file_descriptor import FileDescriptor

SUPPORTED_COMPRESSION_EXTENSIONS = [".zip"]


def download_files(self, client: httpx.Client, file_descriptors: list[FileDescriptor], extract: bool = False):
    if not file_descriptors:
        return

    return [self._download_file(client, file_descriptor, extract) for file_descriptor in file_descriptors]


def download_file(self, client: httpx.Client, file_descriptor: FileDescriptor, extract: bool = False):
    file_descriptor.local_filepath.parent.mkdir(parents=True, exist_ok=True)
    with file_descriptor.local_filepath.open("wb") as file:
        with client.stream("GET", file_descriptor.url) as response:
            for chunk in response.iter_bytes():
                file.write(chunk)
        file.seek(0)

        if extract:
            if file_descriptor.local_filepath.suffix not in SUPPORTED_COMPRESSION_EXTENSIONS:
                raise ValueError(f"not spported compression extension: {file_descriptor.local_filepath.suffix}")

            with zipfile.ZipFile(file) as zip_file:
                zip_file.extractall(path=file_descriptor.local_filepath.parent)
