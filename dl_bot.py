import glob
import os
from secrets import discord_bot_token

import discord
from discord.ext import commands, tasks

from dl_video import youtube_dl

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.online, activity=discord.Game("ur mum")
    )
    print("Bot online")


@client.command()
async def check(ctx, site):
    sites = os.popen(f"youtube-dl --list-extractors | grep -i {site}").read()
    await ctx.send(sites)


@client.command()
async def dl(ctx, url):
    await ctx.channel.purge(limit=1)
    await ctx.send(f"downloading: <{url}>")
    output = youtube_dl(url)
    await ctx.send(output)
    filename = glob.glob("./github/video_dl_bot/dls/*")[0]
    await ctx.send("uploading...")
    await ctx.send(file=discord.File(filename))
    os.popen("sudo rm ~/github/video_dl_bot/dls/*")


@client.command()
async def clear(ctx, amount):
    if amount == "all":
        await ctx.channel.purge(limit=999999)
    await ctx.channel.purge(limit=int(amount) + 1)


@client.command()
async def pi_temp(ctx):
    temp = os.popen("vcgencmd measure_temp").read()
    await ctx.send(f"pi {temp}")


client.run(discord_bot_token)
