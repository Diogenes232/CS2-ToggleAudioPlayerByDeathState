# CS2-ToggleAudioPlayerByDeathState
CounterStrike 2 script that plays/continues music player in background (Spotify, YouTube, WinAmp, etc.) when you die in the game.. and stopps the audio player when the next round starts.
In more detail: it sends the signal "Play/pause media" to your OS when your life/death state changes in CS:GO or CS2.

### Instructions (installation)
- put file `gamestate_integration_music.cfg` in directory your directory `...\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg`
- open Steam, change to your profile (button next to `store`/`library` and copy the number from the url at the top (e.g. `4892389423924399` from `https://steamcommunity.com/profiles/4892389423924399/` - that's your SteamId)
- download `cs2_music_control.py` file to somewhere on your computer, open it with editor and replace `ADD-STEAM-ID-HERE` with your SteamId
- download (Python)[https://www.python.org/downloads/] with PIP (that's the package installer for Python)
- open the command line and download the libraries flask and keyboard to your system for the Python script to run: `pip install flask keyboard`

### Run the script
- start your audio player in background (works with YouTube in the browser or a media player like Spotify regardless if it's minimized)
- start the script with a double-click or enter `python cs2_music_control.py` (sometimes `python3 cs2_music_control.py`)
- start CS2
- when you are alive for the first time the music should stop ~10 seconds later (few seconds before contact with opponents; delay is configurable in the Python script)

#### Limitation
- key "G" is executed when the music player is stopped/continued; remove the key binding in the options of the game (removing that issue would resolve in using more libraries what I wanted to avoid)