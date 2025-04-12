import os
import pytest
import asyncio
from unittest.mock import patch, MagicMock
from aki.tools.command_executor import ShellCommandTool, create_shell_command_tool

@pytest.fixture
def shell_command_tool():
    return create_shell_command_tool()

@pytest.fixture
def tmp_path():
    return '.'

def test_get_user_shell_with_env():
    """Test shell detection when SHELL env var is set"""
    with patch.dict(os.environ, {'SHELL': '/bin/zsh'}):
        tool = ShellCommandTool()
        assert tool._get_user_shell() == '/bin/zsh'

def test_get_user_shell_fallback():
    """Test shell detection fallback when SHELL env var is not set"""
    with patch.dict(os.environ, clear=True):
        tool = ShellCommandTool()
        assert tool._get_user_shell() == '/bin/sh'

def test_run_successful_command(shell_command_tool):
    """Test successful command execution"""
    result = shell_command_tool._run('echo "test"')
    assert result['success'] is True
    assert result['output'] == 'test'
    assert result['error'] is None

def test_run_failed_command(shell_command_tool):
    """Test failed command execution"""
    result = shell_command_tool._run('nonexistent_command')
    assert result['success'] is False
    assert result['error'] is not None

def test_run_timeout():
    """Test command timeout handling"""
    with patch('subprocess.run') as mock_run:
        mock_run.side_effect = TimeoutError()
        tool = ShellCommandTool()
        result = tool._run('sleep 10')
        assert result['success'] is False

def test_run_with_working_dir(shell_command_tool):
    """Test command execution in specific working directory"""
    test_dir = "tests"
    result = shell_command_tool._run('pwd', working_dir=str(test_dir))
    assert result['success'] is True
    assert str(test_dir) in result['output']

def test_invalid_working_dir(shell_command_tool):
    """Test handling of invalid working directory"""
    result = shell_command_tool._run('echo "test"', working_dir='/nonexistent/path')
    assert result['success'] is False
    assert 'error' in result.keys()

@pytest.mark.asyncio
async def test_arun_successful_command(shell_command_tool):
    """Test successful async command execution"""
    result = await shell_command_tool._arun('echo "test"')
    assert result['success'] is True
    assert result['output'] == 'test'
    assert result['error'] is None

@pytest.mark.asyncio
async def test_arun_failed_command(shell_command_tool):
    """Test failed async command execution"""
    result = await shell_command_tool._arun('nonexistent_command')
    assert result['success'] is False
    assert result['error'] is not None

@pytest.mark.asyncio
async def test_arun_timeout():
    """Test async command timeout handling"""
    with patch('asyncio.create_subprocess_exec') as mock_exec:
        mock_process = MagicMock()
        mock_process.communicate = MagicMock(side_effect=asyncio.TimeoutError())
        mock_exec.return_value = mock_process
        
        tool = ShellCommandTool()
        result = await tool._arun('sleep 100')
        assert result['success'] is False
        assert 'timed out' in result['error'].lower()

@pytest.mark.asyncio
async def test_arun_with_working_dir(shell_command_tool, tmp_path):
    """Test async command execution in specific working directory"""
    test_dir = "tests"
    result = await shell_command_tool._arun('pwd', working_dir=str(test_dir))
    assert result['success'] is True
    assert str(test_dir) in result['output']

def test_create_shell_command_tool():
    """Test factory function"""
    tool = create_shell_command_tool()
    assert isinstance(tool, ShellCommandTool)
    assert tool.name == "shell_command"
    assert tool.description == "Execute a shell command in a specified working directory"
