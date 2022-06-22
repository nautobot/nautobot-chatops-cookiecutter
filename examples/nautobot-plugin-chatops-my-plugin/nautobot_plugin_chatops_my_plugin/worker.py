"""Worker functions implementing Nautobot "my_plugin" command and subcommands."""

from django.conf import settings
from django_rq import job

from nautobot_chatops.workers.base import subcommand_of, handle_subcommands
from .my_plugin import NautobotPluginChatopsMyPlugin


# Import config vars from nautobot_config.py
EXAMPLE_VAR = settings.PLUGINS_CONFIG["nautobot_plugin_chatops_my_plugin"].get("example_var")


@job("default")
def my_plugin(subcommand, **kwargs):
    """Interact with my_plugin plugin."""
    return handle_subcommands("my_plugin", subcommand, **kwargs)


@subcommand_of("my_plugin")
def hello_world(dispatcher, arg1):
    """Run logic and return to user via client command '/my_plugin hello-world arg1'."""
    dispatcher.send_markdown(f"Command /my_plugin hello-world received with arg1={arg1}")

    # Creating an instance of NautobotPluginChatopsMyPlugin for pylint
    NautobotPluginChatopsMyPlugin()


    # Send a menu prompt
    # An example leveraging Nautobot resources can be found at:
    # https://github.com/nautobot/nautobot-plugin-chatops/blob/develop/nautobot_chatops/workers/nautobot.py
    #
    # In this example, a small list is created to send a prompt back
    #
    # if not arg1:
    #     choices = [("Name", "name-slug"), ("Name2", "name-slug2")]
    #     dispatcher.prompt_from_menu(
    #         "my_plugin get-menu",
    #         "Select name",
    #         choices,
    #     )

    # Logic/external API calls go here
    
    # Send Markdown formatted text as a result
    # dispatcher.send_markdown(f"Markdown formatted text goes here.")

    # Send block of text
    # dispatcher.send_blocks(
    #     [
    #         *dispatcher.command_response_header(
    #             "my_plugin", "hello-world",
    #         ),
    #         dispatcher.markdown_block(f"example-return-string"),
    #     ]
    # )

    # Send large table
    # dispatcher.send_large_table(
    #     ["Name", "Description"],
    #     ["name1", "description1"],
    # )
    return True
