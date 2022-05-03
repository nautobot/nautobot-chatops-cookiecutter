#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


mattermost_files = [
    "development/docker-compose.mattermost-dev.yml",
    "development/configure_chatops.sh",
    "development/Dockerfile-mattermost",
    "development/mattermost_config_docker.json",
    "development/mattermost-docker-entry.sh",
    "development/mattermost.env",
]

if __name__ == "__main__":
    # Delete Mattermost specific files
    if "No" == "{{ cookiecutter.setup_local_mattermost_dev_env }}":
        for file in mattermost_files:
            remove_file(file)

    if "Not open source or other" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    print("\nCongratulations!  Your cookie has now been baked.\n")
    print(
        "⚠️⚠️ Before you start using your cookie you must run the following commands inside your cookie:\n"
    )
    print("* cp development/creds.example.env development/creds.env\n* poetry lock\n")
    print(
        "creds.env will be ignored by git and can be used to override default environment variables.\n"
    )
