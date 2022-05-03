"""All interactions with {{ cookiecutter.chatops_interactive_command }}."""

import logging


logger = logging.getLogger("rq.worker")


class {{cookiecutter.camel_name}}:  # pylint: disable=too-few-public-methods
    """Representation and methods for interacting with {{ cookiecutter.chatops_interactive_command }}."""

    def __init__(self):
        """Initialization of {{ cookiecutter.chatops_interactive_command }} class."""
