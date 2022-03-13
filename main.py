from discord import *
from pytube import *
import os
import sys

#
# Copyright 2021 © GG
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

# auth
client = Client()

auth_file = open("auth.txt", "r")

help_file = open("help.txt", "r")
help_content = help_file.read()

# creating "database"
try:
    os.mkdir("music-database")
except FileExistsError:
    print("using existing database")


@client.event
async def on_ready():
    print("logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # HELP, LICENSE, SOURCE, LEARN {{{
    if message.content.startswith("$help"):
        await message.channel.send("Hello, I'm Mio Akiyama, I'll help you download and listen to music.")
        await message.channel.send(help_content)

    elif message.content.startswith("$license"):
        await message.channel.send(content="MIT (Massachusetts Institute of Technology) License.", file=File("LICENSE"))

    elif message.content.startswith("$source"):
        await message.channel.send("If you have git installed, you can do 'git clone https://github.com/weebcyberpunk/mio' to download the source code.\nIf not, go to that url, click on 'Code' green button and 'Download ZIP'. Unzip the downloaded file to any location.")

    elif message.content.startswith("$learn fsf"):
        await message.channel.send(content="""
The Free Software Foundation (FSF) is a nonprofit with a worldwide mission to promote computer user freedom. We defend the rights of all software users.
.
As our society grows more dependent on computers, the software we run is of critical importance to securing the future of a free society. Free software is about having control over the technology we use in our homes, schools and businesses, where computers work for our individual and communal benefit, not for proprietary software companies or governments who might seek to restrict and monitor us. The Free Software Foundation exclusively uses free software to perform its work.
.
The Free Software Foundation is working to secure freedom for computer users by promoting the development and use of free (as in freedom) software and documentation - particularly the GNU operating system - and by campaigning against threats to computer user freedom like Digital Restrictions Management (DRM) and software patents.
.
Learn more: https://www.fsf.org/about/
        """)

    elif message.content.startswith("$learn ip"):
        await message.channel.send(content= """
Copying is not theft. Sharing ideias - and files, music and books are ideias - do not make anyone unable to use them too. That's why intellectual property doesn't really exist.

The issue that we're addressing in this minute meme is not the question of whether or not artists can or should not be able to pay their bills, as we believe that they should. The issue we're addressing in this minute meme is whether or not the act of making a copy of a work is a "theft" or not- in other words, whether making a copy denies someone else the work. Our argument is that making a copy does not deny anyone the work, and that traditional copyright systems restrict distribution.

Learn more: https://questioncopyright.org/
                """, file=File("ip-video.mp4"))

    # }}}

    # MAIN BOT FUNCTIONS {{{

    elif message.content.startswith("$video"):

        await message.channel.send("Downloading videos, please wait...")

        # get links
        spl_message = message.content.split()
        links = spl_message[1:]

        # downloading and sending
        for link in links:

            video = YouTube(link)
            if 

                # this is ugly but it's the only way to do it
                await message.channel.send(file=File(video.streams.filter(only_audio=True).first().download("music-database")))

        await message.channel.send("Finish <3")

    elif message.content.startswith("$playlist"):

        await message.channel.send("Downloading videos, please wait...")
        
        # getting playlist
        spl_message = message.content.split()
        link = spl_message[1]
        playlist = Playlist(link)
        urls = playlist.video_urls

        # downloading and sending
        for link in urls:

            # again this is ugly but it's the only way
            await message.channel.send(file=File(YouTube(link).streams.filter(only_audio=True).first().download("music-database")))

        await message.channel.send("Finish <3")

    # }}}

# end
client.run(auth_file.read())
help_file.close()
auth_file.close()
