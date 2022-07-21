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

### Locally

The `Makefile` defines a target to run Mio locally via a script called
`localrun.sh`, which you're supposed to create with your token.
