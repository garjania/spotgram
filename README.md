# spotgram
## Clone 
You can either download the zip file or clone the repo using command bellow:
```bash
git clone https://github.com/garjania/spotgram.git
```
## Telegram Requirements
First you need a telegram bot for this code to work. For that create a new bot at [@BotFather](https://t.me/BotFather) by entering command `/newbot` over there. After the steps are finished, the BotFather will give you a bot token. Copy that token and paste it in `config.cfg` file in front of `tel_token` .

The next requirement is creating a dummy channel! don't ask why. Just create a dummy channel in your telegram and put the id of the channel without @ sign in front of `dummy_channel` in `config.cfg`. Then again, put the id of target channel, which is the channel you want to create a spotify playlist of, without @ in front of `target_channel`.

Next set the bot you just created as the adminstor of the dummy channel and the target channel. And it's all done for Telegram.

## Spotify Requirements
Go to this [link](https://developer.spotify.com/console/get-album/) and request a token by clicking on get token button. Then copy the token (remember to copy all of it) and paste it in front of `spot_token`.

And finally create an spotify playlist in your account and set the `playlist_id` in `config.cfg` as the id of the playlist you just created. To obtain the playlist id you just need to right click on your playlist go to Share > Copy link to playlist. the copied link should look like something like this : https://open.spotify.com/playlist/1234?si=567. Here 1234 is the playlist id.

## Running the Program

For running enter the command bellow in the code directory

```bash
python main.py
```
or maybe
```bash
python3 main.py
```