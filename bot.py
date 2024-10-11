import discord
from discord.ext import commands
import json
import os
import logging
from datetime import datetime

# Create logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Set up logging with daily file rotation
log_filename = f'logs/bot_{datetime.now().strftime("%Y-%m-%d")}.log'
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=log_filename)

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

DATA_FILE = 'commands.json'

# Load data from JSON files
def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return {}

# Save data to JSON files
def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

commands_data = load_data(DATA_FILE)

# Error handling for the bot
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("This command does not exist. You can use !commands to see the available commands.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the required permissions to use this command.")
    else:
        await ctx.send(f"An error occurred: {error}")
        logging.error(f"Error occurred in command '{ctx.command}': {error}")

# Command to add new commands
@bot.command(name='addcommand', help='Add a new command. Usage: !addcommand <alias> <content>')
async def add_command(ctx, alias: str, *, content: str):
    if alias in commands_data:
        await ctx.send(f"Alias `{alias}` already exists!")
        return

    commands_data[alias] = content
    save_data(DATA_FILE, commands_data)
    await ctx.send(f"Command `{alias}` added successfully!")

# Command to delete a command
@bot.command(name='delcommand', help='Delete an existing command. Usage: !delcommand <alias>')
async def delete_command(ctx, alias: str):
    if alias in commands_data:
        del commands_data[alias]
        save_data(DATA_FILE, commands_data)
        await ctx.send(f"Command `{alias}` has been deleted.")
    else:
        await ctx.send(f"No command found with alias `{alias}`.")

# Command to display the content of a command directly
@bot.command(name='show', help='Show the content of a command. Usage: !show <alias>')
async def display_command(ctx, alias: str):
    content = commands_data.get(alias)
    if content:
        await ctx.send(f"Command `{alias}` content:\n```{content}```")
    else:
        await ctx.send(f"No command found with alias `{alias}`.")

# Command to clear the chat
@bot.command(name='clear', help='Clear the chat messages. Usage: !clear')
@commands.has_permissions(manage_messages=True)
async def clear_chat(ctx):
    await ctx.channel.purge()
    await ctx.send("Chat cleared!", delete_after=5)  # Auto-delete confirmation after 5 seconds

# Command to show available commands
@bot.command(name='commands', help='Show the list of available commands.')
async def list_commands(ctx):
    embed = discord.Embed(
        title="Available Commands",
        description="\n".join(f"`{alias}`" for alias in commands_data),
        color=0x1abc9c
    )
    await ctx.send(embed=embed)

# Initialize the bot
bot.run('YOUR_BOT_TOKEN')
