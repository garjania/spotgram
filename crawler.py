from telegram import TelegramBot
from spotify import SpotifyBot
from difflib import SequenceMatcher
import configparser as cfg

parser = cfg.ConfigParser()
parser.read('config.cfg')

dummy_channel = parser.get('info', 'dummy_channel')
target_channel = parser.get('info', 'target_channel')
playlist_id = parser.get('info', 'playlist_id')

print(type(dummy_channel), target_channel, playlist_id)

tbot = TelegramBot(parser.get('creds', 'tel_token'))
sbot = SpotifyBot(parser.get('creds', 'spot_token'))

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def spotify_search(audio):
    track = audio['title']
    artist = audio['performer']
    found = sbot.search_track(track[:25])
    if 'tracks' not in found:
        print(track)
        print(found)
        return
    result = {'track': None, 'artist': None, 'id': None}
    score = -1
    for item in found['tracks']['items']:
        found_name = item['name']
        t_score = similar(str.lower(found_name), str.lower(track))
        a_score = 0
        all_artists = ''
        for found_artist in item['artists']:
            all_artists += found_artist['name']
        a_score = similar(str.lower(all_artists), str.lower(artist))
        cal_score = 2*a_score + t_score + item['popularity']/25
        if cal_score > score:
            score = cal_score
            result['track'] = found_name
            result['artist'] = found_artist['name']
            result['id'] = item['id']
    return result

def crawl(_iter):
    try:
        content = tbot.forward_to_channel(_iter, target_channel, dummy_channel)
        if not content['ok']:
            return None
        if 'audio' in content['result']:
            result = spotify_search(content['result']['audio'])
            sbot.add_to_playlist(playlist_id, result['id'])
            return _iter, result
    except:
        print('error at: ', _iter)

if __name__=='__main__':
    for i in range(15):
        crawl(i)
