import discord

from pydoc import describe
from urllib import response
from discord.ext import commands
from AntiScam import AntiScam

whitelist = [821961609001172992]
logs_channel = 925189755325546567

bot = commands.Bot(command_prefix='ipn!')


@bot.listen()
async def on_message(message):
    await AntiScam(message, bot=bot, whitelist=whitelist, muted_role='Muted', verified_role='Verificado', logs_channel=logs_channel)


@bot.command(name='s')
async def sumar(ctx, n1, n2):
    response = int(n1)+int(n2)
    await ctx.send("**¿No sabes sumar?**... bueno, la respuesta a esto es:  " + "__`" + str(response) + "`__")


@bot.command(name='m')
async def mult(ctx, n1, n2):
    response = int(n1)*int(n2)
    await ctx.send("**¿No sabes multiplicar?**... bueno, la respuesta a esto es:  " + "__`" + str(response) + "`__")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("Detectando..."))
    
    
bot.run(os.environ["DISCORD_TOKEN"])
