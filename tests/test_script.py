import pytest
from pytest_console_scripts import ScriptRunner


@pytest.mark.script_launch_mode('subprocess')
def test_number_of_bytes(script_runner: ScriptRunner) -> None:
    result = script_runner.run(['python3', 'pywc/main.py', '-c', 'data/test.txt'])
    assert result.returncode == 0
    assert result.stderr == ''
    assert result.stdout == '342190\tdata/test.txt\n'

@pytest.mark.script_launch_mode('subprocess')
def test_number_of_lines(script_runner: ScriptRunner) -> None:
    result = script_runner.run(['python3', 'pywc/main.py', '-l', 'data/test.txt'])
    assert result.returncode == 0
    assert result.stderr == ''
    assert result.stdout == '7145\tdata/test.txt\n'

@pytest.mark.script_launch_mode('subprocess')
def test_number_of_words(script_runner: ScriptRunner) -> None:
    result = script_runner.run(['python3', 'pywc/main.py', '-w', 'data/test.txt'])
    assert result.returncode == 0
    assert result.stderr == ''
    assert result.stdout == '58164\tdata/test.txt\n'

@pytest.mark.script_launch_mode('subprocess')
def test_number_of_characters(script_runner: ScriptRunner) -> None:
    result = script_runner.run(['python3', 'pywc/main.py', '-m', 'data/test.txt'])
    assert result.returncode == 0
    assert result.stderr == ''
    assert result.stdout == '339292\tdata/test.txt\n'

@pytest.mark.script_launch_mode('subprocess')
def test_no_parameters(script_runner: ScriptRunner) -> None:
    result = script_runner.run(['python3', 'pywc/main.py', 'data/test.txt'])
    assert result.returncode == 0
    assert result.stderr == ''
    assert result.stdout == '7145\t58164\t342190\tdata/test.txt\n'

@pytest.mark.script_launch_mode('subprocess')
def test_no_file(script_runner: ScriptRunner) -> None:
    result = script_runner.run(['cat', 'data/test.txt', '|', 'python3', 'pywc/main.py'], shell=True)
    assert result.returncode == 0
    assert result.stderr == ''

