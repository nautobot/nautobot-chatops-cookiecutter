# nautobot-chatops-cookiecutter

## Why Cookiecutter?

Before we get started, let's provide some context around the terminology used within Cookiecutter.

* **cookie** - The Cookiecutter template that provides the framework for specific projects to allow developers to get started developing faster such as the ones defined above.
* **bake/baking** - The output of a cookie. If a cookie is baked, it means the project was created from a Cookiecutter template.

CookieCutter was choosen as a method as it provides the capability to provide a customized set of data based on a question/answer setup to help get customization in place.

Check out the [Python CookieCutter documentation](https://cookiecutter.readthedocs.io/en/1.7.2/) for more details of the project.

## Getting Started

Below are the steps outlined in detail for getting started along with various tips and tricks that may be beneficial.

## Generating a New Nautobot Chatops Plugin

Let's walk you through baking a **nautobot-chatops-plugin**.

> NOTE: It is recommended to leave these first 4 options as default:

| Setting                         | Description                                                                                     |
| ------------------------------- | ----------------------------------------------------------------------------------------------- |
| **codeowner_github_usernames**  | The Github codeowners for the new plugin                                                        |
| **full_name**                   | Used in the **author** field within `pyproject.toml` and `PluginConfig`                         |
| **email**                       | Used in the **author** field within `pyproject.toml`                                            |
| **github_org**                  | Used to construct **repo_url**                                                                  |
| **chatops_interactive_command** | Slash command used to interact with Bot in chat client                                          |
| **plugin_name**                 | The Python name of the plugin                                                                   |
| **verbose_name**                | Used in `PluginConfig`                                                                          |
| **plugin_slug**                 | Python packaging name                                                                           |
| **project_slug**                | Used to construct **repo_url**                                                                  |
| **base_url**                    | Defines plugin's base url used in Nautobot                                                      |
| **min_nautobot_version**        | The minimum supported Nautobot version                                                          |
| **max_nautobot_version**        | The maximum supported Nautobot version                                                          |
| **nautobot_version**            | Used for development purposes to decide with Nautobot-dev Docker image to use for development   |
| **camel_name**                  | Used to define the plugin's subclassing of `PluginConfig`, e.g. `MyPluginConfig(PluginConfig):` |
| **project_short_description**   | Used in the **description** field within `PluginConfig`                                         |
| **version**                     | Version of the new Nautobot plugin                                                              |
| **open_source_license**         | Determine if project is open source or not                                                      |

> NOTE: Cookiecutter by default bakes the new cookie within the current working directory. If that is not desirable then use the `-o` option to specify a different output folder.

```bash
➜ cookiecutter nautobot-plugin-chatops -o /path/to/dest/output/folder
codeowner_github_usernames []:
full_name [Network to Code, LLC]:
email [info@networktocode.com]:
github_org [nautobot]:
chatops_interactive_command [my_plugin]:
plugin_name [nautobot_plugin_chatops_my_plugin]:
verbose_name [Nautobot Plugin Chatops My Plugin]:
plugin_slug [nautobot-plugin-chatops-my-plugin]:
project_slug [nautobot-plugin-chatops-my-plugin]:
repo_url [https://github.com/nautobot/nautobot-plugin-chatops-my-plugin]:
min_nautobot_version [1.0.1]:
max_nautobot_version [1.9999]:
nautobot_version [latest]:
camel_name [NautobotPluginChatopsMyPlugin]:
project_short_description [Nautobot Plugin Chatops My Plugin]:
version [0.1.0]:
Select open_source_license:
1 - Apache-2.0
2 - Not open source or other
Choose from 1, 2 [1]:

Congratulations!  Your cookie has now been baked.

⚠️⚠️ Before you start using your cookie you must run the following commands inside your cookie:

* cp development/creds.example.env development/creds.env
* poetry lock

creds.env will be ignored by git and can be used to override default environment variables.
```

Follow the directions provided at the end of baking the cookie.

```bash
➜ cd nautobot-plugin-chatops-my-plugin
➜ poetry lock
➜ cp development/creds.example.env development/creds.env
```

Here is an example of what your directory structure may look like (subject to change as the project is developed over time).

> NOTE: there are hidden files not displayed in the below output.

```bash
➜ ll nautobot-plugin-chatops-my-plugin
total 104
-rw-r--r--  1 ntc  staff    29B Aug  3 08:15 FAQ.md
-rw-r--r--  1 ntc  staff    16K Aug  3 08:15 GETTING_STARTED.md
-rw-r--r--  1 ntc  staff   591B Aug  3 08:15 LICENSE
-rw-r--r--  1 ntc  staff   7.1K Aug  3 08:15 README.md
drwxr-xr-x  9 ntc  staff   288B Aug  3 08:15 development
-rw-r--r--  1 ntc  staff   300B Aug  3 08:15 invoke.example.yml
drwxr-xr-x  7 ntc  staff   224B Aug  3 08:15 nautobot_plugin_chatops_my_plugin
-rw-r--r--  1 ntc  staff   2.3K Aug  3 08:15 pyproject.toml
-rw-r--r--  1 ntc  staff    12K Aug  3 08:15 tasks.py
```

Once the cookie is generated the next step is to start developing the plugin! If you're not familiar with the development environment provided by this cookie, we recommend checking out the `GETTING_STARTED.md` located in the root of the newly baked cookie or checkout the generated **README** for a quick start guide.

## Automate local dev environment setup with Mattermost

The baked cookie supports the automated setup of a local Mattermost instance to quickly test your chatops plugin. All settings and credentials will be pre-configured, and a separate Docker container will run Mattermost in the background, accessible at http://localhost:8065

To setup this environment, after creating the `creds.env` file and running `poetry lock` run the following invoke commands from the plugin folder, using the optional `-m` or `--mattermost` flags:

```bash
➜ poetry shell             # Activate poetry environment
➜ invoke build -m          # Build the containers
➜ invoke setup-mattermost  # Setup the Mattermost container and configure all required settings
➜ invoke start -m          # Start all Nautobot containers
```

There is no additional setup needed. After a few seconds, you can test this deployment is working properly as follows:

**Mattermost**

- Go to http://localhost:8065/ntcteam/messages/@ntcbot
- Log in using the default `admin/Ntc01234!!` credentials.
  - These are set in `development/development.env`, and may have been changed.
- Send a direct message to @ntcbot. You should be able to run an example command `/chatops_interactive_command hello-world test`, where "chatops_interactive_command" is what was configured for the last question during cookiecutter template generation.

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
