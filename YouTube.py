import discord  # discord api
from discord.ext import commands  # commands extension
from apiclient.discovery import build  # youtube api
import json
from datetime import datetime
import time
import asyncio
import sys
import logging
import aiohttp
import re

bot = commands.Bot(command_prefix='r-', description=None)
# Some systems will crash without this because Google's Python is built
# differently
sys.modules['win32file'] = None
youtube_key = ''

from datadog import initialize

options = {
    'api_key': '',
    'app_key': ''
}

initialize(**options)
import datadog
from datadog import statsd


class YouTube:
    """Youtube Commands"""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

    @commands.command(pass_context=True)
    async def search(self, ctx):
        try:
            try:
                youtube = build("youtube", "v3", developerKey=youtube_key)
                search_response = youtube.search().list(q=ctx.message.content.split(
                    ' ', 2)[2], part="id,snippet", maxResults=1, type="video").execute()
                if len(search_response.get('items')) == 0:
                    await bot.say("No videos found.")
                else:
                    vidid = search_response.get('items')[0]['id']['videoId']
                    vidurl = "https://www.youtube.com/watch?v=" + vidid
                    yt_url = "http://www.youtube.com/oembed?url={0}&format=json".format(
                        vidurl)
                    metadata = await self.get_json(yt_url)
                    data = discord.Embed(
                        title="**__Search Result__**", colour=discord.Colour(value=11735575))
                    data.add_field(name="Video Title", value=metadata[
                                   'title'], inline=False)
                    data.add_field(name="Video Uploader", value=metadata[
                                   'author_name'], inline=False)
                    data.add_field(name="Video Link",
                                   value=vidurl, inline=False)
                    data.set_image(
                        url="https://i.ytimg.com/vi/{}/hqdefault.jpg".format(vidid))
                    try:
                        await bot.say(embed=data)
                        statsd.increment('bot.commands.run', 1)
                        
    @commands.command(pass_context=True)
    async def channel(self, ctx):
        try:
            try:
                youtube = build("youtube", "v3", developerKey=youtube_key)
                search_response = youtube.search().list(q=ctx.message.content.split(
                    ' ', 2)[2], part="id,snippet", maxResults=1, type="channel").execute()
                if len(search_response.get('items')) == 0:
                    await bot.say("No channels found.")
                else:
                    chanid = search_response.get('items')[0]['id']['channelId']
                    data = youtube.channels().list(part='statistics,snippet', id=chanid).execute()
                    subs = str(data['items'][0]['statistics']
                               ['subscriberCount'])
                    subsf = await self.thous(subs)
                    name = str(data['items'][0]['snippet']['title'])
                    img = str(data['items'][0]['snippet'][
                              'thumbnails']['medium']['url'])
                    chanurl = "https://www.youtube.com/channel/" + chanid
                    data = discord.Embed(
                        title="**__Search Result__**", colour=discord.Colour(value=11735575))
                    data.add_field(name="Channel Name",
                                   value=name, inline=False)
                    data.add_field(name="Subscribers",
                                   value=subsf, inline=False)
                    data.add_field(name="Channel Link",
                                   value=chanurl, inline=False)
                    data.set_image(url=img)
                    try:
                        await bot.say(embed=data)
                        statsd.increment('bot.commands.run', 1)

    @commands.command(pass_context=True)
    async def lookup(self, ctx):
        try:
            try:
                url = re.compile(
                    r'http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?')
                shorturl = re.compile(
                    r'http(?:s?):\/\/?youtu(?:\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?')
                q = ctx.message.content.split(' ', 2)[2]
                match = re.search(url, q)
                if match:
                    match2 = re.search(shorturl, q)
                    if match2:
                        a = match2.group(1)
                        q = 'https://www.youtube.com/watch?v={}'.format(a)
                    yt_url = "http://www.youtube.com/oembed?url={0}&format=json".format(
                        q)
                    metadata = await self.get_json(yt_url)
                    youtube = build("youtube", "v3", developerKey=youtube_key)
                    search_response = youtube.search().list(q=ctx.message.content.split(
                        ' ', 2)[2], part="id,snippet", maxResults=1, type="video").execute()
                    if len(search_response.get('items')) == 0:
                        await bot.say("No videos found.")
                    else:
                        vidid = search_response.get(
                            'items')[0]['id']['videoId']
                        data = discord.Embed(
                            title="**__Reverse Lookup__**", colour=discord.Colour(value=11735575))
                        data.add_field(name="Video Title", value=metadata[
                                       'title'], inline=False)
                        data.add_field(name="Video Uploader", value=metadata[
                                       'author_name'], inline=False)
                        data.add_field(name="Video Link",
                                       value=q, inline=False)
                        data.set_image(
                            url="https://i.ytimg.com/vi/{}/hqdefault.jpg".format(vidid))
                    try:
                        await bot.say(embed=data)
                        statsd.increment('bot.commands.run', 1)

    @commands.command(pass_context=True)
    async def new(self, ctx):
        try:
            try:
                youtube = build("youtube", "v3", developerKey=youtube_key)
                search_response = youtube.search().list(q=ctx.message.content.split(
                    ' ', 2)[2], part="id,snippet", maxResults=1, type="channel").execute()
                if len(search_response.get('items')) == 0:
                    await bot.say("No channels found.")
                else:
                    chanid = search_response.get('items')[0]['id']['channelId']
                channelDetails = youtube.channels().list(
                    id=chanid, part="contentDetails", maxResults=1).execute()
                playlistid = channelDetails['items'][0][
                    'contentDetails']['relatedPlaylists']['uploads']
                videos = youtube.playlistItems().list(
                    playlistId=playlistid, part="snippet", maxResults=1).execute()
                if len(videos.get('items')) == 0:
                    await bot.say("No channels found.")
                else:
                    vidid = videos['items'][0]['snippet'][
                        'resourceId']['videoId']
                    title = videos['items'][0]['snippet']['title']
                    dateraw = datetime.strptime(videos['items'][0]['snippet'][
                                                'publishedAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
                    uploader = videos['items'][0]['snippet']['channelTitle']
                    # '%H:%M (GMT), %A %d %b %Y'
                    uploaddate = datetime.strftime(
                        dateraw, '%H:%M %A %d %b %Y')
                    data = discord.Embed(
                        title="**__Latest Video from {}__**".format(uploader), colour=discord.Colour(value=11735575))
                    data.add_field(name="Video Title",
                                   value=title, inline=False)
                    data.add_field(name="Upload Date",
                                   value=uploaddate, inline=False)
                    data.add_field(
                        name="Video Link", value="https://youtube.com/watch?v={}".format(vidid), inline=False)
                    data.set_image(
                        url="https://i.ytimg.com/vi/{}/mqdefault.jpg".format(vidid))
                try:
                    await bot.say(embed=data)
                    statsd.increment('bot.commands.run', 1)

    async def get_json(self, yt_url):
        async with self.session.get(yt_url) as r:
            result = await r.json()
        return result

    async def thous(self, subs):
        return re.sub(r'(\d{3})(?=\d)', r'\1 ', str(subs)[::-1])[::-1]


def setup(bot):
    global logger
    logger = logging.getLogger('yt')
    bot.add_cog(YouTube(bot))
