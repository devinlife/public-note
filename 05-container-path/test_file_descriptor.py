import pytest
from your_module_name import PathDescriptor, FileDescriptor


def test_path_descriptor_local_path():
    descriptor = PathDescriptor(relative_path="rel_path", base_path_local="/base/local")
    assert descriptor.local_path == "/base/local/rel_path"

    with pytest.raises(ValueError):
        descriptor.container_path


def test_file_descriptor_initialization():
    with pytest.raises(ValueError):
        FileDescriptor(filepath="/abs_path/file.txt", base_path_local="/base/local")

    file_desc = FileDescriptor(filepath="rel_path/file.txt", base_path_local="/base/local")
    assert file_desc.filename == "file.txt"
    assert file_desc.local_filepath == "/base/local/rel_path/file.txt"

    with pytest.raises(ValueError):
        file_desc.container_filepath

    file_desc_with_container = FileDescriptor(
        filepath="rel_path/file.txt", base_path_local="/base/local", base_path_container="/base/container"
    )
    assert file_desc_with_container.container_filepath == "/base/container/rel_path/file.txt"


def test_file_descriptor_paths():
    file_desc = FileDescriptor(filepath="rel_path/file.txt", base_path_local="/base/local")
    assert file_desc.local_path == "/base/local/rel_path"

    with pytest.raises(ValueError):
        file_desc.container_path

    file_desc_with_container = FileDescriptor(
        filepath="rel_path/file.txt", base_path_local="/base/local", base_path_container="/base/container"
    )
    assert file_desc_with_container.container_path == "/base/container/rel_path"


if __name__ == "__main__":
    pytest.main()
