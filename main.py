from pygame import *
from Game.sound import *

classes = ["player", "sound"]

'''Less sure what this does now'''
for i in classes:
    exec("from Game.%s import %s" % (i, i.title()))

init()


class Main:
    '''Main game class'''

    def __init__(self):
        self.screen = display.set_mode((800, 600))
        self.screenW, self.screenH = 800, 600
        display.set_caption("Super Stereotypical Wizard Man Person")
        display.set_icon(image.load('icon.jpg').convert_alpha())

        '''Startup music'''
        mixer.music.load(Sound().getMusic("title_screen"))
        # mixer.music.play(loops=-1)

        self.sound = Sound()

        # Start Screen
        self.startup = image.load(
            "resources/graphics/misc/title_bg.png").convert()

    # Start had , pos, click as parameters
    def start(self):
        '''Options on startup'''

        self.screen.blit(self.startup, (0, 0))


'''Main Class instantiated as Game'''
Game = Main()
'''Game Loop'''
running = True
playing = False

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    Game.start()
    display.flip()
