import discord 
import yt_dlp 

#
# If you gonna run this, please note that this shit uses the PWD to store all
# downloaded videos. Good luck.
#

# LICENSE {{{
#
# Copyright 2022 © GG
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of 
# this software and associated documentation files (the “Software”), to deal 
# in the Software without restriction, including without limitation the rights to 
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
# of the Software, and to permit persons to whom the Software is furnished to do 
# so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.
# 
# }}}

client = discord.Client()
# { "ignoreerrors": True, "postprocessors": [{"FFmpegExtractAudioPP"}] }
youtubedl = yt_dlp.YoutubeDL()

# login in
with open("auth.txt", "r") as auth_file:
    AUTH = auth_file.read()


@client.event
async def on_ready():
    print(f"logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$download"):

        msg_content = message.content.split(' ')
        msg_content.pop(0)

        for url in msg_content:
            video_info = youtubedl.extract_info(url)

            with open(f"{video_info['title']}.mp3", "rb") as video_file:
                await message.channel.send(file=discord.File(video_file))


client.run(AUTH)

