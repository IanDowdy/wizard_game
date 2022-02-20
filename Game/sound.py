from pygame import *


class Sound(object):
    '''Play Sound effects'''

    def __init__(self):
        '''All sound effects'''

        '''This is where we'll put all the music references'''
        self.themes = {
            "title_screen": "resources/sound/title_music.wav"
        }

        mixer.music.set_volume(.6)

    def getMusic(self, sound):
        '''Return music themes'''
        return self.themes[sound]

    def stopSound(self, sound):
        '''stops specific sound'''
        self.sounds[sound].fadeout(500)

    def stopMusic(self):
        '''Stop mixer'''
        mixer.music.fadeout(500)
