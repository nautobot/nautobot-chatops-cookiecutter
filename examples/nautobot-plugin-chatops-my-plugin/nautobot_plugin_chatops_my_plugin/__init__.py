"""Plugin declaration for nautobot_plugin_chatops_my_plugin."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
try:
    from importlib import metadata
except ImportError:
    # Python version < 3.8
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)

from nautobot.extras.plugins import PluginConfig


class NautobotPluginChatopsMyPluginConfig(PluginConfig):
    """Plugin configuration for the nautobot_plugin_chatops_my_plugin plugin."""

    name = "nautobot_plugin_chatops_my_plugin"
    verbose_name = "Nautobot Plugin Chatops My Plugin"
    version = __version__
    author = "Network to Code, LLC"
    description = "Nautobot Plugin Chatops My Plugin."
    required_settings = []
    min_version = "1.2.0"
    max_version = "1.9999"
    default_settings = {}
    caching_config = {}


config = NautobotPluginChatopsMyPluginConfig  # pylint:disable=invalid-name
