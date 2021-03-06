"""Plugin declaration for {{cookiecutter.plugin_name}}."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
try:
    from importlib import metadata
except ImportError:
    # Python version < 3.8
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)

from nautobot.extras.plugins import PluginConfig


class {{cookiecutter.camel_name}}Config(PluginConfig):
    """Plugin configuration for the {{cookiecutter.plugin_name}} plugin."""

    name = "{{cookiecutter.plugin_name}}"
    verbose_name = "{{cookiecutter.verbose_name}}"
    version = __version__
    author = "{{cookiecutter.full_name}}"
    description = "{{cookiecutter.project_short_description}}."
    required_settings = []
    min_version = "{{cookiecutter.min_nautobot_version}}"
    max_version = "{{cookiecutter.max_nautobot_version}}"
    default_settings = {}
    caching_config = {}


config = {{cookiecutter.camel_name}}Config  # pylint:disable=invalid-name
