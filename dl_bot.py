import glob
import os
import json
import requests
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
async def freq(ctx, word, n=20):
    results = os.popen(
        f"grep {word} -n -m {n} ~/github/video_dl_bot/weibo_wordfreq.release_UTF-8.txt"
    ).read()
    if len(results)==0:
        await ctx.send("No results")
    else:
        await ctx.send(results)


@client.command()
async def dl(ctx, url):
    #await ctx.channel.purge(limit=1)
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

@client.command()
async def affix(ctx):
    r=requests.get("https://raider.io/api/v1/mythic-plus/affixes?region=eu")
    data=json.loads(r.text)

    levels=["Base", "3+","7+","10+"]
    message=""
    for i in range(len(data['affix_details'])):
        message+=f"{levels[i]}\n"
        message+=f"{data['affix_details'][i]['name']}\n"
        message+=f"{data['affix_details'][i]['description']}\n"
        if i<len(data['affix_details'])-1:
            message+="---\n"

    await ctx.send(message)


client.run(discord_bot_token)
