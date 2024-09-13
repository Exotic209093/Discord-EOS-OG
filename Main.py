# main.py
import discord
from discord.ext import commands, tasks
import requests
import logging
import os
import json  # For handling JSON data
from dotenv import load_dotenv  # Import dotenv to load .env variables

# Load environment variables from the .env file
load_dotenv()  # Load all variables from the .env file into the environment

# Load server IDs and specified player IDs from JSON
with open('config.json', 'r') as f:
    config_data = json.load(f)

server_ids = config_data['server_ids']  # List of server IDs
specified_ids = config_data['specified_ids']  # List of player IDs

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

# Sensitive Data from Environment Variables
Token = os.getenv('DISCORD_BOT_TOKEN')
admin_channel_id = os.getenv('ADMIN_CHANNEL_ID')  # Channel to send notifications

# BattleMetrics API key
API_KEY = os.getenv('BATTLEMETRICS_API_KEY')

BASE_URL = 'https://api.battlemetrics.com/'

# Store the last message object globally to edit it later
last_message = None

# Function to get server details including connected players
def get_server_details(server_id):
    endpoint = f'servers/{server_id}'
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    params = {'include': 'player'}
    response = requests.get(f'{BASE_URL}{endpoint}', headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        logging.error(f'Error retrieving server details: {response.status_code}')
        return None

# Task to run every 30 seconds and update the last message
@tasks.loop(seconds=30)
async def check_servers():
    global last_message  # Refer to the global message object

    logging.info("Checking BattleMetrics servers...")
    
    discord_message = "**Players Detected on Servers**\n\n"
    for server_id in server_ids:
        server_details = get_server_details(server_id)
        if server_details:
            server_name = server_details['data']['attributes']['name']
            # Clean up the server name
            server_name = server_name.replace("[WIPED MAY4] 7man/Shop/Kits/CrossPlay/12ma - ", "")
            players = server_details.get('included', [])
            player_names = []
            if players:
                for player in players:
                    if player['id'] in specified_ids:
                        player_names.append(player['attributes']['name'])
            if player_names:
                discord_message += f"`{server_name}` - Specified players connected: {', '.join(player_names)}\n"
            else:
                discord_message += f"`{server_name}` - No specified players connected.\n"
        else:
            discord_message += f'No details found for server ID {server_id}.\n'

    # Send or update the message in the Discord channel
    channel = client.get_channel(int(admin_channel_id))
    if channel:
        if last_message is None:  # Send a new message if no previous message exists
            last_message = await channel.send(discord_message)
        else:  # Edit the last message
            await last_message.edit(content=discord_message)
    else:
        logging.error(f"Admin channel with ID {admin_channel_id} not found.")

# Event when the bot is ready
@client.event
async def on_ready():
    logging.info("Bot is ready. Starting the server monitoring task...")
    check_servers.start()  # Start the task loop

# Logging setup
logging.basicConfig(level=logging.INFO)

# Run the bot
client.run(Token)
