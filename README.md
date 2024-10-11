# BugBounty-Linux-Command-Bot

A Discord bot specifically designed to store and manage Linux commands or Bug Bounty commands. It supports dynamic command management, error handling, and useful utility functions for easy command handling.

## Features

- **Dynamic Command Management:** Easily add, delete, and display custom commands.
- **Logging:** Logs all activities and errors for debugging and monitoring.
- **Permissions Handling:** Ensures that only authorized users can execute specific commands.
- **Utility Functions:** Includes features like chat clearing and a list of all available commands.

## Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Discord.py](https://discordpy.readthedocs.io/) library installed

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/bugbounty-linux-command-bot.git
    cd bugbounty-linux-command-bot
    ```

2. **Install the required dependencies**:
    ```bash
    pip install discord.py
    ```

3. **Create a `commands.json` file** in the project directory:
   Create a file named `commands.json` in the root directory of your project with the following initial content:
    ```json
    {
        "example_command": "This is the content of the example command"
    }
    ```
   This file will store all the commands you add to the bot. When you add new commands using the bot, they will be saved in this file in a similar format.

4. **Set your bot's token**:
   Open the bot's code file and replace the placeholder `'YOUR_BOT_TOKEN'` with your actual Discord bot token:
    ```python
    bot.run('YOUR_BOT_TOKEN')
    ```

## Usage

### Available Commands

- **!addcommand `<alias>` `<content>`**: Add a new command with the given alias and content.
- **!delcommand `<alias>`**: Delete a command with the specified alias.
- **!show `<alias>`**: Display the content of a specific command.
- **!clear**: Clear all messages in the current chat channel.
- **!commands**: List all available custom commands.

 ![image](https://github.com/user-attachments/assets/c6fe8088-8d52-40b7-babb-def30c989f87)


### Error Handling

- If you use a non-existent command, the bot will notify you.
- Unauthorized users attempting to use protected commands will receive a permission error.
- Unexpected errors are logged to the daily log file for easy troubleshooting.

## Logging

Logs are automatically stored in the `logs` directory with filenames in the format `bot_YYYY-MM-DD.log`, making it easy to track the bot's activities.

## Contributing

Contributions are welcome! Feel free to fork the repository, submit a pull request, or open an issue if you have any suggestions or find bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

For issues or questions, open an issue on GitHub or contact the project maintainer.
