import sys
from os.path import exists

from repka_defaults import *

music_is_on = 1

try:
    import miniaudio
    import libxmplite
except ModuleNotFoundError as e:
    music_is_on = 0
    print('Music modules not found, music disabled.\n'
          'To enable, please install:\n'
          '> pip install miniaudio\n'
          '> pip install libxmplite\n')


device = miniaudio.PlaybackDevice(output_format=miniaudio.SampleFormat.SIGNED16, nchannels=2, sample_rate=44100)
xmp = libxmplite.Xmp()
now_playing = ''


playlist = ['DEADLOCK.XM', 'ASTRAY.S3M', 'SHADOWRU.MOD', '2ND_PM.S3M']

'''
Playlist can be downloaded here:

https://api.modarchive.org/downloads.php?moduleid=174160#ambient_starfield.xm
https://api.modarchive.org/downloads.php?moduleid=125383#_escape_.mod
https://api.modarchive.org/downloads.php?moduleid=145030#dust_particle.xm
https://api.modarchive.org/downloads.php?moduleid=131449#szur_szur_-mix.mod
https://api.modarchive.org/downloads.php?moduleid=52662#mrg8bit.xm
https://api.modarchive.org/downloads.php?moduleid=79055#dust_particles.mod
https://api.modarchive.org/downloads.php?moduleid=96360#dancecore.mod
https://api.modarchive.org/downloads.php?moduleid=32814#acidgod.mod
'''

title_track = 'ambient_starfield.xm'
scores_track = '_escape_.mod'
start_track = 'dust_particle.xm'
slowest_track = 'szur_szur_-mix.mod'
slow_track = 'mrg8bit.xm'
normal_track = 'dust_particles.mod'
fast_track = 'dancecore.mod'
# faster_track = 'different_waves.mod'
fastest_track = 'acidgod.mod'

def check_music_files():
    if not exists(title_track):
        print (f'{title_track} not found')
        return 0
    if not exists(scores_track):
        print (f'{scores_track} not found')
        return 0
    if not exists(start_track):
        print (f'{start_track} not found')
        return 0
    if not exists(slowest_track):
        print (f'{slowest_track} not found')
        return 0
    if not exists(slow_track):
        print (f'{slow_track} not found')
        return 0
    if not exists(normal_track):
        print (f'{normal_track} not found')
        return 0
    if not exists(fast_track):
        print (f'{fast_track} not found')
        return 0
    if not exists(fastest_track):
        print (f'{fastest_track} not found')
        return 0
    return 1


    
def stream_module(xmp: libxmplite.Xmp):
    required_frames = yield b""  # generator initialization
    try:
        while True:
            buffer = xmp.play_buffer(required_frames * 2 * 2)
            required_frames = yield buffer
    except libxmplite.XmpError as x:
        print("XMP Playback error", x)


def play_song(song_name):
    global now_playing

    if song_name != now_playing:

        xmp.load(song_name)
        now_playing = song_name
        xmp.start(device.sample_rate)

        stream = stream_module(xmp)
        next(stream)
        device.start(stream)




def stop_song():
    global now_playing
    
    if now_playing:
        xmp.stop()
        xmp.release()
        device.stop()
        now_playing = ''

def close_music_device():
    device.close()

def select_track(speed):
    global now_playing    
    if speed < 28: track = slowest_track
    elif speed < 35: track = slow_track
    elif speed > 60: track = fastest_track
    elif speed > 48: track = fast_track
    elif now_playing != start_track: track = normal_track
    else: return now_playing
    return track
    
    
