import discord
import discord.ext
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']


credentials=ServiceAccountCredentials.from_json_keyfile_name("Annie-e432eb58860b.json",scope)
gc= gspread.authorize(credentials)
wks=gc.open("Kurusaki_database_discord").sheet1


sp=wks.get_all_records()
#[{'Discord Name': 'Dong Cheng', 'ID': 185181025104560128, 'Points': 1}]

bot = commands.Bot(command_prefix='a.')

@bot.event
async def on_ready():
    """WHEN BOT IS READY, PRINT MESSAGE IN TERMINAL"""
    print ("I am running on " + bot.user.name)







bot.run('MzE3MDkyNzg4Mzc2NDM2NzM2.Ddsvww.ofp-IDE7rgMlsGRF243yCwbfoao')
