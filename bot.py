import discord
from discord import app_commands
from discord.ext import commands
import os

# --- CONFIGURATION ---
TOKEN = os.environ.get("DISCORD_TOKEN", "COLLE_TON_TOKEN_ICI")
LIEN_ALICIA = "https://www.youtube.com/@syrensgaming13"

# --- SETUP ---
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} commande(s) synchronisée(s)")
    except Exception as e:
        print(f"Erreur de synchronisation : {e}")

@bot.tree.command(name="alicia", description="Envoie le lien de la chaîne")
async def alicia(interaction: discord.Interaction):
    await interaction.response.send_message(LIEN_ALICIA)

# --- LANCEMENT ---
if TOKEN == "COLLE_TON_TOKEN_ICI":
    print("ERREUR : remplace TOKEN par ton vrai token, ou mets-le dans la variable d'environnement DISCORD_TOKEN")
else:
    bot.run(TOKEN)