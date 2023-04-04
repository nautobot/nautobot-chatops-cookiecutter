# Nautobot ChatOps Cookiecutter

## Introduction

This project helps to get you started on your way of creating Nautobot ChatOps commands quickly. When running through the cookie cutting template, there are a few questions that will help dynamically create content within the final "baked cookie" project. This will create a new repository that will be the new chat bot that you can then install into your Nautobot instance. For more on building your own chat bot, take a look at the [blog post on Creating Custom Chat Commands](http://blog.networktocode.com/post/creating-custom-chat-commands-using-nautobot-chatops/).

### IMPORTANT Cookie Notes

- The logo of the project is a placeholder (`docs/images/icon-{{cookiecutter.plugin_slug}}.png`) - please replace it with your app icon, making sure it's at least 200x200px and has a transparent background!
- Please resolve and remove **all** of the comments and blocks marked with `Developer Note - Remove Me!` prior to publishing. Catch'em all with `rgrep "Developer Note" plugin-root`.
- The documentation website will be built and hosted on `readthedocs.io` for open source projects and is documented as part of the process.

Cookiecutter was chosen as a method to create projects from a template because it provides the capability to provide a customized project output based on a question/answer setup to help get customization in place.

Check out the [Python Cookiecutter documentation](https://cookiecutter.readthedocs.io/en/1.7.2/) for more details of the project.

## Getting Started

Below are the steps outlined in detail for getting started along with various tips and tricks that may be beneficial.

## Generating a New Nautobot Chatops Plugin

Let's walk you through baking a **nautobot-chatops-plugin** cookie. Below are the settings that will be asked for during the question part.

> NOTE: It is recommended to leave these first 4 options as default:

| Setting | Description |
|-------- | ----------- |
| **codeowner_github_usernames** | The Github codeowners for the new plugin |
| **full_name** | Used in the **author** field within `pyproject.toml` and `PluginConfig` |
| **email** | Used in the **author** field within `pyproject.toml` |
| **github_org** | Used to construct **repo_url** |
| **chatops_interactive_command**     | Slash command used to interact with Bot in chat client                                          |
| **plugin_name** | The Python name of the plugin |
| **verbose_name** | Used in `PluginConfig` |
| **plugin_slug** | Python packaging name |
| **project_slug** | Used to construct **repo_url** |
| **base_url** | Defines plugin's base url used in Nautobot |
| **min_nautobot_version** | The minimum supported Nautobot version |
| **max_nautobot_version** | The maximum supported Nautobot version |
| **nautobot_version** | Used for development purposes to decide with Nautobot-dev Docker image to use for development |
| **camel_name** | Used to define the plugin's subclassing of `PluginConfig`, e.g. `MyPluginConfig(PluginConfig):` |
| **project_short_description** | Used in the **description** field within `PluginConfig` |
| **version** | Version of the new Nautobot plugin |
| **Select open_source_license** | Determine if project is open source or not |
| **docs_base_url**| The main URL where the project documentation will be hosted. For open source projects use the default (`https://docs.nautobot.com`). |
| **docs_app_url**| The full URL for documentation hosting. You might want to shorten the project alias, for example `https://docs.nautobot.com/projects/chatops-my-plugin/en/latest` instead of `https://docs.nautobot.com/projects/nautobot-plugin-data-validation/en/latest`. Make sure there's no trailing `/`! |
| **setup_local_mattermost_dev_env**  | Setup Local mattermost development environment flag                                             |

> NOTE: Cookiecutter by default bakes the new cookie within the current working directory. If that is not desirable then use the `-o` option to specify a different output folder.

```bash
❯ cookiecutter .

codeowner_github_usernames [@smith-ntc]:
full_name [Network to Code, LLC]:
email [info@networktocode.com]:
github_org [nautobot]:
chatops_interactive_command [my_plugin]: 
plugin_name [nautobot_plugin_chatops_my_plugin]: 
verbose_name [Nautobot Plugin Chatops My Plugin]: 
plugin_slug [nautobot-plugin-chatops-my-plugin]: 
project_slug [nautobot-plugin-chatops-my-plugin]: 
repo_url [https://github.com/nautobot/nautobot-plugin-chatops-my-plugin]:
base_url [chatops-my-plugin]:
min_nautobot_version [1.5.2]:
max_nautobot_version [1.9999]:
nautobot_version [latest]:
camel_name [NautobotPluginChatopsMyPlugin]: 
project_short_description [Nautobot Plugin Chatops My Plugin]: 
version [0.1.0]:
Select open_source_license:
1 - Apache-2.0
2 - Not open source
Choose from 1, 2 [1]:
docs_base_url [https://docs.nautobot.com]:
docs_app_url [https://docs.nautobot.com/projects/chatops-my-plugin/en/latest]: https://docs.nautobot.com/projects/chatops-my-plugin/en/latest
Select setup_local_mattermost_dev_env:
1 - Yes
2 - No
Choose from 1, 2 [1]: 

Congratulations!  Your cookie has now been baked. It is located at /vagrant/nautobot-plugin-chatops-my-plugin.

⚠️⚠️ Before you start using your cookie you must run the following commands inside your cookie:

* poetry lock
* cp development/creds.example.env development/creds.env
* invoke makemigrations

creds.env will be ignored by git and can be used to override default environment variables.
```

Follow the directions provided at the end of baking the cookie.

```bash
➜ cd nautobot-plugin-chatops-my-plugin
➜ poetry lock
➜ cp development/creds.example.env development/creds.env
➜ invoke makemigrations
```

Here is an example of what your directory structure may look like (subject to change as the project is developed over time).

```bash
➜ ll nautobot-plugin-chatops-my-plugin
total 96K
drwxrwxr-x 1 vagrant vagrant 4.0K Oct 24 15:30 ./
drwxrwxr-x 1 vagrant vagrant 4.0K Oct 24 15:30 ../
-rw-rw-r-- 1 vagrant vagrant  118 Oct 24 15:30 .bandit.yml
-rw-rw-r-- 1 vagrant vagrant  295 Oct 24 15:30 .dockerignore
-rw-rw-r-- 1 vagrant vagrant  192 Oct 24 15:30 .flake8
drwxrwxr-x 1 vagrant vagrant 4.0K Oct 24 15:30 .github/
-rw-rw-r-- 1 vagrant vagrant 4.9K Oct 24 15:30 .gitignore
-rw-rw-r-- 1 vagrant vagrant  451 Oct 24 15:30 .readthedocs.yaml
-rw-rw-r-- 1 vagrant vagrant  214 Oct 24 15:30 .yamllint.yml
-rw-rw-r-- 1 vagrant vagrant  591 Oct 24 15:30 LICENSE
-rw-rw-r-- 1 vagrant vagrant 5.0K Oct 24 15:30 README.md
drwxrwxr-x 1 vagrant vagrant 4.0K Oct 24 15:30 development/
drwxrwxr-x 1 vagrant vagrant 4.0K Oct 24 15:30 docs/
-rw-rw-r-- 1 vagrant vagrant  325 Oct 24 15:30 invoke.example.yml
-rw-rw-r-- 1 vagrant vagrant  322 Oct 24 15:30 invoke.mysql.yml
-rw-rw-r-- 1 vagrant vagrant 3.8K Oct 24 15:30 mkdocs.yml
drwxr-xr-x  7 ntc  staff   224B Aug  3 08:15 nautobot_plugin_chatops_my_plugin
-rw-rw-r-- 1 vagrant vagrant 3.3K Oct 24 15:30 pyproject.toml
-rw-rw-r-- 1 vagrant vagrant  14K Oct 24 15:30 tasks.py

Once the cookie is generated the next step is to start developing the plugin! If you're not familiar with the development environment provided by this cookie, we recommend checking out the Development Environment guide located in the documentation tree at `docs/dev/dev_environment.md`.

## Automate local dev environment setup with Mattermost

The baked cookie supports the automated setup of a local [Mattermost](https://mattermost.com/) instance to quickly test your chatops plugin. All settings and credentials will be pre-configured, and a separate Docker container will run Mattermost in the background, accessible at http://localhost:8065. Be sure to answer yes to the question about setup_local_mattermost_dev_env.

To set up this environment, you must first run `poetry lock` command and have `creds.env` file in place. Then you run the following invoke commands from within the plugin folder.

```bash
➜ poetry shell             # Activate poetry environment
➜ invoke build             # Build the containers
➜ invoke setup-mattermost  # Setup the Mattermost container and configure all required settings
➜ invoke start             # Start all Nautobot containers
```

There is no additional setup needed. After a few seconds, you can test this deployment is working properly as follows:

**Mattermost**

- Go to http://localhost:8065/automationteam/messages/@ntcbot
- Log in using the default `admin/Nautobot123!!` credentials.
  - These are set in `development/development.env`, and may have been changed.
- Send a direct message to @nautobot-bot. You should be able to run an example command `/chatops_interactive_command hello-world test`, where "chatops_interactive_command" is what was configured for the last question during cookiecutter template generation.

**Nautobot**

- Got to http://localhost:8080
- Log in using the default `admin/admin` credentials.
  - These are set in `development/creds.env`, and may have been changed.

You can see the Mattermost token and command are already configured.

### Adding new chatbot commands

After updating the `{plugin-name}/worker.py` file and saving it, the backend Django service should auto-reload with your changes. If it doesn't, or a bug in the code caused it to crash, you can quickly relaunch it from your poetry environment with `invoke restart`.

## Get dev environment running - Manual

If you prefer to not use the local Mattermost instance for development purposes, you can follow the instructions below.

You must configure the relevant ChatOps plugin variables in development/creds.env. For example, if you want to use Slack, configure the relevant API token, secret, and set `enable_slack` to true.

Once done, setup the relevant SaaS application is setup on the backend. Follow the instructions found in the [Nautobot ChatOps Plugin](https://github.com/nautobot/nautobot-plugin-chatops/blob/develop/docs/chat_setup.md) repo.

Then run the following commands:

```bash
poetry shell
poetry install
invoke build
invoke start
```

Once the Docker containers are spun up, go to http://localhost:8080 to see the running instance. For dev purposes, add permissions for all commands in Plugins-->Access Grants for each of the following:

- Organization
- Channel
- User

Once completed, open Slack (or whichever chat app client you configured). You should be able to run an example command `/chatops_interactive_command hello-world test`, where "chatops_interactive_command" is what was configured for the last question during cookiecutter template generation.
