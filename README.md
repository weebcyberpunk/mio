# Mio Akiyama

Mio Akiyama is a Discord bot that downloads music from YouTube named after the
*Keion!* character Mio Akiyama, a bass player.

## Running

You can run your own instance of Mio by running `main.py` with the
`DISCORD_TOKEN` envvar setted to a Discord bot token:

``` DISCORD_TOKEN=<your_token> python main.py ```

Mio requires the Python libraries to interact with Discord and
[yt-dlp](https://github.com/yt-dlp/yt-dlp).
[FFmpeg](https://github.com/FFmpeg/FFmpeg) installed in the system is also
required. See `requirements.txt`.

## Adding to server

I'm currently running an instance of Mio. You can add it to your server with
[this link](https://discord.com/api/oauth2/authorize?client_id=938200205638135808&permissions=3398656&scope=bot)
