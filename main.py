import discord 
import yt_dlp 
import os

#
# If you gonna run this, please note that this shit uses the PWD to store all
# downloaded videos. Good luck.
#
# Repo should includes Procfile to run on Heroku. Makefile should define a
# localrun.sh script to run locally with your token
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
youtubedl = yt_dlp.YoutubeDL({
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }]
})

@client.event
async def on_ready():
    print(f"logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('$'):

        if message.content.startswith("$download"):

            msg_content = message.content.split(' ')
            msg_content.pop(0)

            # corrects strange behaviour of msg_content to eventually have empty
            # strings because that breaks the youtube download
            if '' in msg_content:
                msg_content.remove('')

            # loop through urls
            for url in msg_content:
                # continue if url is not valid
                try:
                    video_info = youtubedl.extract_info(url, download=False)

                except yt_dlp.utils.ExtractorError:
                    await message.channel.send(f'{url} is not a valid link!')
                    continue

                else:
                    file_name = f"{video_info['title']} [{video_info['id']}].mp3"

                # if file exists, just sends. if not, downloads
                if not os.path.exists(file_name):
                    await message.channel.send('Downloading music, please wait... <3')
                    youtubedl.download(url)

                else:
                    await message.channel.send('Found music in database! Sending quickly... ;)')

                try: 
                    video_file = open(file_name, "rb")

                except OSError:
                    await message.channel.send("Cannot download this music, sorry ;(")

                else:
                    await message.channel.send(file=discord.File(video_file))
                    video_file.close()


        elif message.content.startswith('$ping'):
            await message.channel.send('Mio is listening! UwU <3')


client.run(os.getenv('DISCORD_TOKEN'))

