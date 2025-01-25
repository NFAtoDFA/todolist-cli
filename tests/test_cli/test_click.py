import pytest
from click.testing import CliRunner
from main import cli

@pytest.fixture()
def runner():
    return CliRunner

def test_add_task(runner):
    result = runner.invoke(cli, ['add','Learn TDD'])
    assert result.exit_code == 0
    assert "Task: 'Learn TDD' added successfully." in result.output
