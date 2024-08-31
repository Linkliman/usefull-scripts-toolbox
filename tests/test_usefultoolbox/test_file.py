import pytest
from usefultoolbox import file


# Fixtures for setup and teardown
@pytest.fixture(scope="function")
def setup_test_environment(tmp_path):
    """Setup a temporary directory and files for testing."""
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()

    test_file = test_dir / "test_file.txt"
    test_file.write_text("This is a test file.")

    return {"test_dir": test_dir, "test_file": test_file, "tmp_path": tmp_path}


# Test file operations
def test_read_file(setup_test_environment):
    test_file = setup_test_environment["test_file"]
    content = file.read_file(test_file)
    assert content == "This is a test file."


def test_write_file(setup_test_environment):
    test_file = setup_test_environment["test_file"]
    file.write_file(test_file, "New content.")
    assert test_file.read_text() == "New content."


def test_append_file(setup_test_environment):
    test_file = setup_test_environment["test_file"]
    file.write_file(test_file, " Additional content.", mode="a")
    assert test_file.read_text() == "This is a test file. Additional content."


def test_copy_file(setup_test_environment):
    test_file = setup_test_environment["test_file"]
    copy_file = setup_test_environment["test_dir"] / "copy_file.txt"
    file.copy_file(test_file, copy_file)
    assert copy_file.exists()
    assert copy_file.read_text() == "This is a test file."


def test_move_file(setup_test_environment):
    test_file = setup_test_environment["test_file"]
    new_location = (
        setup_test_environment["tmp_path"] / "new_location" / "moved_file.txt"
    )
    new_location.parent.mkdir(parents=True)
    file.move_file(test_file, new_location)
    assert new_location.exists()
    assert new_location.read_text() == "This is a test file."
    assert not test_file.exists()


def test_delete_file(setup_test_environment):
    test_file = setup_test_environment["test_file"]
    file.delete_file(test_file)
    assert not test_file.exists()


# Test directory operations
def test_create_directory(setup_test_environment):
    new_dir = setup_test_environment["tmp_path"] / "new_directory"
    file.create_directory(new_dir)
    assert new_dir.exists()


def test_list_directory(setup_test_environment):
    test_dir = setup_test_environment["test_dir"]
    contents = file.list_directory(test_dir)
    assert "test_file.txt" in contents


def test_delete_directory(setup_test_environment):
    test_dir = setup_test_environment["test_dir"]
    file.delete_directory(test_dir)
    assert not test_dir.exists()


# Test utility functions
def test_file_exists(setup_test_environment):
    test_file = setup_test_environment["test_file"]
    assert file.file_exists(test_file)
    assert not file.file_exists(test_file.parent / "non_existent_file.txt")


def test_directory_exists(setup_test_environment):
    test_dir = setup_test_environment["test_dir"]
    assert file.directory_exists(test_dir)
    assert not file.directory_exists(test_dir.parent / "non_existent_directory")

