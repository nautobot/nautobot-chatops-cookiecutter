"""All interactions with API behind my_plugin.

This class is usually a wrapper of an existing SDK, or a raw implementation of it to have reusable code in the worker.py.
"""

import logging


logger = logging.getLogger("rq.worker")


class NautobotPluginChatopsMyPlugin:  # pylint: disable=too-few-public-methods
    """Representation and methods for interacting with the API behind my_plugin."""

    def __init__(self):
        """Initialization of my_plugin class."""
