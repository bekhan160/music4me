lang="python"
import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
import asyncio
import ffmpeg



YDL_OPTIONS = {'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True',
               'preferredquality': '192', 'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

client = commands.Bot(command_prefix='-')


@client.command()
async def play(ctx, arg):
    global vc

    try:
        voice_channel = ctx.message.author.voice.channel
        vc = await voice_channel.connect()
    except:
        print('Уже подключен или не удалось подключиться')

    if vc.is_playing():
        await ctx.send(f'{ctx.message.author.mention}, музыка уже проигрывается.')

    else:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(arg, download=False)

        URL = info['formats'][0]['url']

        vc.play(discord.FFmpegPCMAudio(executable='ffmpeg',source=URL, **FFMPEG_OPTIONS))

        while vc.is_playing():
            await asyncio.sleep(1)
        if not vc.is_paused():
            await vc.disconnect()


@client.command()
async def stop(ctx):
    await ctx.voice_client.disconnect()

client.run('OTgwNTEwNDEzMzUzNTE3MDU2.G8kMGT.hPr-ksmCCtuHy899PG2clFXcT_9xcC_PG-XxBU')

# Биринчи upd бул бот ырларды ойнойт бироок сен войс каналда болсон ал экинчи жолуу ойнобой
