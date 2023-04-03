import os
import shutil

from cookiecutter.config import get_user_config

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
USER_CONFIG = get_user_config()


def remove_file(directory, filepath):
    """
    Remove a file from the project directory.

    >>> remove_file('./api/', 'text.txt')
    # It will delete './api/text.txt' from project dir

    Args:
        directory (str): base directory path
        filepath (str): file path within the base directory
    """
    os.remove(os.path.join(directory, filepath))


CONGRATS = f"""
Congratulations! Your cookie has now been baked. It is located at {PROJECT_DIRECTORY}.

⚠️⚠️ Before you start using your cookie you must run the following commands inside your cookie:

* poetry lock
* cp development/creds.example.env development/creds.env
* poetry shell
* invoke makemigrations

The file "creds.env will be ignored by git and can be used to override default environment variables.
"""

mattermost_files = [
    "development/docker-compose.mattermost-dev.yml",
    "development/configure_chatops.sh",
    "development/Dockerfile-mattermost",
    "development/mattermost_config_docker.json",
    "development/mattermost-docker-entry.sh",
    "development/mattermost.env",
]

if __name__ == "__main__":
    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file(PROJECT_DIRECTORY, "LICENSE")

    # Delete Mattermost specific files
    if "No" == "{{ cookiecutter.setup_local_mattermost_dev_env }}":
        for file in mattermost_files:
            remove_file(PROJECT_DIRECTORY, file)

    # Persist the baked cookie parameters in-repo for future usage as a replay file.
    shutil.copy(
        os.path.join(USER_CONFIG["replay_dir"], "nautobot-plugin.json"),
        f"{PROJECT_DIRECTORY}/.cookiecutter.json",
    )

    print(CONGRATS)
