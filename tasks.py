import pathlib
import sys
from invoke import task


@task(help={"template": "Name of the cookiecutter template to test"})
def test(context, template=""):
    """Test a specific cookiecutter template."""
    if not template:
        sys.exit("-t / --template parameter is required!")
    test_dir = pathlib.Path.cwd() / template / "tests"
    if test_dir.exists():
        print(f"Starting Test for {template}")
        context.run(f"pytest { test_dir } -v --template { template }")
    else:
        sys.exit(f"No Test found for {template}")


@task
def tests(context):
    """Test all available cookiecutter templates."""
    context.run("pytest tests/ -vv")
