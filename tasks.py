import pathlib
import sys
from invoke import task
from glob import glob


@task(help={"template": "Name of the cookiecutter template to test"})
def test(context, template=""):
    """Test a specific cookiecutter template."""
    # if not template:
    #     sys.exit("-t / --template parameter is required!")
    test_dir = pathlib.Path.cwd() / template / "tests"
    if test_dir.exists():
        print(f"Starting Test for {template}")
        context.run(f"pytest { test_dir } -v")
        # context.run(f"pytest { test_dir } -v --template { template }")
    else:
        sys.exit(f"No Test found for {template}")


@task
def tests(context):
    """Test all available cookiecutter templates."""
    context.run("pytest tests/ -vv")


@task(
    help={
        "build": "Whether to re-bake (build) the example before testing it",
        "example": "Glob-style pattern specifying which baked example(s) to test (default '*')",
        "template": "Name of the cookiecutter template to test",
    }
)
def baked_test(context, build=False, example="*", template=""):
    """Execute tests within a baked cookiecutter example."""
    # if not template:
    #     sys.exit("-t / --template parameter is required!")
    if not glob(f"{template}/examples/{example}"):
        sys.exit(f"No example matching '{example}' found for template '{template}'")
    for baked_cookie in glob(f"{template}/examples/{example}"):
        print(f"Running Tests for {template} example {baked_cookie}")
        with context.cd(baked_cookie):
            # Make sure to copy creds.example.env to creds.env for tests
            context.run("cp development/creds.example.env development/creds.env")
            if build:
                context.run("invoke build --no-cache")
            context.run("invoke tests")
