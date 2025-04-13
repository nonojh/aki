# Generated by AkiUnitTestGenerator

import pathlib

import pytest

from aki.tools.code_analyzer.filesystem_models import FileSystemNode, FileSystemNodeType


@pytest.fixture
def test_files_dir() -> pathlib.Path:
    """Return the path to the test files directory."""
    current_file = pathlib.Path(__file__)
    return current_file.parent / "test_files"


@pytest.mark.asyncio
async def test_content_utf8_file(test_files_dir):
    """Test reading a UTF-8 encoded file."""
    file_path = test_files_dir / "utf8_file.md"
    node = FileSystemNode(
        name=file_path.name,
        type=FileSystemNodeType.FILE,
        path_str=str(file_path),
        path=file_path,
        size=file_path.stat().st_size,
    )

    result = await node.content()

    assert "UTF-8 encoded text with emoji" in result
    assert "special characters like ñ, ö, é" in result
    assert "Japanese こんにちは" in result


@pytest.mark.asyncio
async def test_content_utf16_file(test_files_dir):
    """Test reading a UTF-16 encoded file."""
    file_path = test_files_dir / "utf16_file.md"
    node = FileSystemNode(
        name=file_path.name,
        type=FileSystemNodeType.FILE,
        path_str=str(file_path),
        path=file_path,
        size=file_path.stat().st_size,
    )

    result = await node.content()

    assert "UTF-16" in result
    assert "emoji" in result


@pytest.mark.asyncio
async def test_content_latin1_file(test_files_dir):
    """Test reading a Latin-1 encoded file."""
    file_path = test_files_dir / "latin1_file.md"
    node = FileSystemNode(
        name=file_path.name,
        type=FileSystemNodeType.FILE,
        path_str=str(file_path),
        path=file_path,
        size=file_path.stat().st_size,
    )

    result = await node.content()

    assert "Café" in result
    assert "è" in result
    assert "é" in result


@pytest.mark.asyncio
async def test_content_windows1252_file(test_files_dir):
    """Test reading a Windows-1252 encoded file."""
    file_path = test_files_dir / "windows1252_file.md"
    node = FileSystemNode(
        name=file_path.name,
        type=FileSystemNodeType.FILE,
        path_str=str(file_path),
        path=file_path,
        size=file_path.stat().st_size,
    )

    result = await node.content()

    assert "Special characters" in result
    assert "€" in result  # Euro symbol unique to windows-1252


@pytest.mark.asyncio
async def test_content_empty_file(test_files_dir):
    """Test reading an empty file."""
    file_path = test_files_dir / "empty_file.md"
    node = FileSystemNode(
        name=file_path.name,
        type=FileSystemNodeType.FILE,
        path_str=str(file_path),
        path=file_path,
        size=file_path.stat().st_size,
    )

    # Read the content
    result = await node.content()

    assert result == ""
