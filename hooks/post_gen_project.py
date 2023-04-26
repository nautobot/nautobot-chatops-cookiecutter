from collections import OrderedDict
import json
from pathlib import Path

_PROJECT_PATH = Path.cwd()

_CONGRATS = f"""
Congratulations! Your cookie has now been baked. It is located at {_PROJECT_PATH}.

⚠️⚠️ Before you start using your cookie you must run the following commands inside your cookie:

* poetry lock
* cp development/creds.example.env development/creds.env
* poetry shell
* invoke makemigrations

The file "creds.env will be ignored by git and can be used to override default environment variables.
"""

_MATTERMOST_FILES = [
    "docker-compose.mattermost-dev.yml",
    "configure_chatops.sh",
    "Dockerfile-mattermost",
    "mattermost_config_docker.json",
    "mattermost-docker-entry.sh",
    "mattermost.env",
]

if __name__ == "__main__":
    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        (_PROJECT_PATH / "LICENSE").unlink()

    if "No" == "{{ cookiecutter.setup_local_mattermost_dev_env }}":
        for file in _MATTERMOST_FILES:
            (_PROJECT_PATH / "development" / file).unlink()

    # Persist the baked cookie parameters in-repo for future rebakes
    cookie = {{ cookiecutter }}
    del cookie["_template"]
    del cookie["_output_dir"]
    (_PROJECT_PATH / "cookie.json").write_text(json.dumps(cookie, indent=2))

    print(_CONGRATS)
