#!/usr/bin/env python

# Space Invaders
# Created by Lee Robinson

from pygame import *
import sys
from os.path import abspath, dirname
from random import randint, choice
from inspect import currentframe, getframeinfo

BASE_PATH = abspath(dirname(__file__))
FONT_PATH = BASE_PATH + '/fonts/'
IMAGE_PATH = BASE_PATH + '/images/'
SOUND_PATH = BASE_PATH + '/sounds/'

# Colors (R, G, B)
WHITE = (255, 255, 255)
GREEN = (78, 255, 87)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)

SCREEN = display.set_mode((800, 600)) # width, height
FONT = FONT_PATH + 'space_invaders.ttf'
IMG_NAMES = ['ship', 'mystery',
             'enemy1_1', 'enemy1_2',
             'enemy2_1', 'enemy2_2',
             'enemy3_1', 'enemy3_2',
             'explosionblue', 'explosiongreen', 'explosionpurple',
             'laser', 'enemylaser']
IMAGES = {name: image.load(IMAGE_PATH + '{}.png'.format(name)).convert_alpha()
          for name in IMG_NAMES}


class Ship(sprite.Sprite):
    def __init__(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        sprite.Sprite.__init__(self)
        self.image = IMAGES['ship']
        # self.rect = self.image.get_rect(topleft=(375, 540))
        self.rect = self.image.get_rect(topleft=(325, 540))
        self.speed = 20 # 5

    def update(self, keys, *args):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        if keys[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 740:
            self.rect.x += self.speed
        game.screen.blit(self.image, self.rect)

class Ship2(sprite.Sprite):
    def __init__(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        sprite.Sprite.__init__(self)
        self.image = IMAGES['ship']
        # self.rect = self.image.get_rect(topleft=(375, 540))
        self.rect = self.image.get_rect(topleft=(425, 540))
        self.speed = 20 # 5

    def update(self, keys, *args):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        if keys[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 740:
            self.rect.x += self.speed
        game.screen.blit(self.image, self.rect)

class Bullet(sprite.Sprite):
    def __init__(self, xpos, ypos, direction, speed, filename, side):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        sprite.Sprite.__init__(self)
        self.image = IMAGES[filename]
        self.rect = self.image.get_rect(topleft=(xpos, ypos))
        self.speed = speed
        self.direction = direction
        self.side = side
        self.filename = filename

    def update(self, keys, *args):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        game.screen.blit(self.image, self.rect)
        self.rect.y += self.speed * self.direction
        if self.rect.y < 15 or self.rect.y > 600:
            self.kill()


class Enemy(sprite.Sprite):
    def __init__(self, row, column):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        sprite.Sprite.__init__(self)
        self.row = row
        self.column = column
        self.images = []
        self.load_images()
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.direction = 1
        self.rightMoves = 30
        self.leftMoves = 30
        self.moveNumber = 15
        self.moveTime = 600
        self.timer = time.get_ticks()

    def update(self, keys, currentTime, enemies):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        if currentTime - self.timer > self.moveTime:
            if self.direction == 1:
                maxMove = self.rightMoves + enemies.rightAddMove
            else:
                maxMove = self.leftMoves + enemies.leftAddMove

            if self.moveNumber >= maxMove:
                if self.direction == 1:
                    self.leftMoves = 30 + enemies.rightAddMove
                elif self.direction == -1:
                    self.rightMoves = 30 + enemies.leftAddMove
                self.direction *= -1
                self.moveNumber = 0
                self.rect.y += 35
            elif self.direction == 1:
                self.rect.x += 10
                self.moveNumber += 1
            elif self.direction == -1:
                self.rect.x -= 10
                self.moveNumber += 1

            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]

            self.timer += self.moveTime

        game.screen.blit(self.image, self.rect)

    def load_images(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        images = {0: ['1_2', '1_1'],
                  1: ['2_2', '2_1'],
                  2: ['2_2', '2_1'],
                  3: ['3_1', '3_2'],
                  4: ['3_1', '3_2'],
                  }
        img1, img2 = (IMAGES['enemy{}'.format(img_num)] for img_num in
                      images[self.row])
        self.images.append(transform.scale(img1, (40, 35)))
        self.images.append(transform.scale(img2, (40, 35)))


class EnemiesGroup(sprite.Group):
    def __init__(self, columns, rows):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        sprite.Group.__init__(self)
        self.enemies = [[0] * columns for _ in range(rows)]
        self.columns = columns
        self.rows = rows
        self.leftAddMove = 0
        self.rightAddMove = 0
        self._aliveColumns = list(range(columns))
        self._leftAliveColumn = 0
        self._rightAliveColumn = columns - 1
        self._leftKilledColumns = 0
        self._rightKilledColumns = 0

    def add(self, *sprites):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        super(sprite.Group, self).add(*sprites)

        for s in sprites:
            self.enemies[s.row][s.column] = s

    def is_column_dead(self, column):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        for row in range(self.rows):
            if self.enemies[row][column]:
                return False
        return True

    def random_bottom(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        random_index = randint(0, len(self._aliveColumns) - 1)
        col = self._aliveColumns[random_index]
        for row in range(self.rows, 0, -1):
            enemy = self.enemies[row - 1][col]
            if enemy:
                return enemy
        return None

    def kill(self, enemy):
        # on double hit calls twice for same enemy, so check before
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        if not self.enemies[enemy.row][enemy.column]:
            return  # nothing to kill

        self.enemies[enemy.row][enemy.column] = None
        isColumnDead = self.is_column_dead(enemy.column)
        if isColumnDead:
            self._aliveColumns.remove(enemy.column)

        if enemy.column == self._rightAliveColumn:
            while self._rightAliveColumn > 0 and isColumnDead:
                self._rightAliveColumn -= 1
                self._rightKilledColumns += 1
                self.rightAddMove = self._rightKilledColumns * 5
                isColumnDead = self.is_column_dead(self._rightAliveColumn)

        elif enemy.column == self._leftAliveColumn:
            while self._leftAliveColumn < self.columns and isColumnDead:
                self._leftAliveColumn += 1
                self._leftKilledColumns += 1
                self.leftAddMove = self._leftKilledColumns * 5
                isColumnDead = self.is_column_dead(self._leftAliveColumn)

"""
class Blocker(sprite.Sprite):
    def __init__(self, size, color, row, column):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        sprite.Sprite.__init__(self)
        self.height = size
        self.width = size
        self.color = color
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.row = row
        self.column = column

    def update(self, keys, *args):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        game.screen.blit(self.image, self.rect)
"""

class Mystery(sprite.Sprite):
    def __init__(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        sprite.Sprite.__init__(self)
        self.image = IMAGES['mystery']
        self.image = transform.scale(self.image, (75, 35))
        self.rect = self.image.get_rect(topleft=(-80, 45))
        self.row = 5
        self.moveTime = 25000
        self.direction = 1
        self.timer = time.get_ticks()
        self.mysteryEntered = mixer.Sound(SOUND_PATH + 'mysteryentered.wav')
        self.mysteryEntered.set_volume(0.3)
        self.playSound = True

    def update(self, keys, currentTime, *args):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        resetTimer = False
        passed = currentTime - self.timer
        if passed > self.moveTime:
            if (self.rect.x < 0 or self.rect.x > 800) and self.playSound:
                self.mysteryEntered.play()
                self.playSound = False
            if self.rect.x < 840 and self.direction == 1:
                self.mysteryEntered.fadeout(4000)
                self.rect.x += 2
                game.screen.blit(self.image, self.rect)
            if self.rect.x > -100 and self.direction == -1:
                self.mysteryEntered.fadeout(4000)
                self.rect.x -= 2
                game.screen.blit(self.image, self.rect)

        if self.rect.x > 830:
            self.playSound = True
            self.direction = -1
            resetTimer = True
        if self.rect.x < -90:
            self.playSound = True
            self.direction = 1
            resetTimer = True
        if passed > self.moveTime and resetTimer:
            self.timer = currentTime


class Explosion(sprite.Sprite):
    def __init__(self, xpos, ypos, row, ship, mystery, score):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        sprite.Sprite.__init__(self)
        self.isMystery = mystery
        self.isShip = ship
        if mystery:
            self.text = Text(FONT, 20, str(score), WHITE, xpos + 20, ypos + 6)
        elif ship:
            self.image = IMAGES['ship']
            self.rect = self.image.get_rect(topleft=(xpos, ypos))
        else:
            self.row = row
            self.load_image()
            self.image = transform.scale(self.image, (40, 35))
            self.rect = self.image.get_rect(topleft=(xpos, ypos))
            game.screen.blit(self.image, self.rect)

        self.timer = time.get_ticks()

    def update(self, keys, currentTime):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        passed = currentTime - self.timer
        if self.isMystery:
            if passed <= 200:
                self.text.draw(game.screen)
            elif 400 < passed <= 600:
                self.text.draw(game.screen)
            elif passed > 600:
                self.kill()
        elif self.isShip:
            if 300 < passed <= 600:
                game.screen.blit(self.image, self.rect)
            elif passed > 900:
                self.kill()
        else:
            if passed <= 100:
                game.screen.blit(self.image, self.rect)
            elif 100 < passed <= 200:
                self.image = transform.scale(self.image, (50, 45))
                game.screen.blit(self.image,
                                 (self.rect.x - 6, self.rect.y - 6))
            elif passed > 400:
                self.kill()

    def load_image(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        imgColors = ['purple', 'blue', 'blue', 'green', 'green']
        self.image = IMAGES['explosion{}'.format(imgColors[self.row])]


class Life(sprite.Sprite):
    def __init__(self, xpos, ypos):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        sprite.Sprite.__init__(self)
        self.image = IMAGES['ship']
        self.image = transform.scale(self.image, (23, 23))
        self.rect = self.image.get_rect(topleft=(xpos, ypos))

    def update(self, keys, *args):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        game.screen.blit(self.image, self.rect)


class Text(object):
    def __init__(self, textFont, size, message, color, xpos, ypos):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        self.font = font.Font(textFont, size)
        self.surface = self.font.render(message, True, color)
        self.rect = self.surface.get_rect(topleft=(xpos, ypos))

    def draw(self, surface):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        surface.blit(self.surface, self.rect)


class SpaceInvaders(object):
    def __init__(self):
        # It seems, in Linux buffersize=512 is not enough, use 4096 to prevent:
        #   ALSA lib pcm.c:7963:(snd_pcm_recover) underrun occurred
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        mixer.pre_init(44100, -16, 1, 4096)
        init()
        self.caption = display.set_caption('Space Invaders')
        self.screen = SCREEN
        self.background = image.load(IMAGE_PATH + 'background.jpg').convert()
        self.startGame = False
        self.mainScreen = True
        self.gameOver = False
        # Initial value for a new game
        self.enemyPositionDefault = 65
        # Counter for enemy starting position (increased each new round)
        self.enemyPositionStart = self.enemyPositionDefault
        # Current enemy starting position
        self.enemyPosition = self.enemyPositionStart

    def reset(self, score, lives, newGame=False):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        self.player = Ship()
        self.player2 = Ship2()
        self.playerGroup = sprite.Group(self.player)
        self.playerGroup = sprite.Group(self.player2)
        self.explosionsGroup = sprite.Group()
        self.bullets = sprite.Group()
        self.mysteryShip = Mystery()
        self.mysteryGroup = sprite.Group(self.mysteryShip)
        self.enemyBullets = sprite.Group()
        self.reset_lives(lives)
        self.enemyPosition = self.enemyPositionStart
        self.make_enemies()
        # Only create blockers on a new game, not a new round
        """if newGame:
            self.allBlockers = sprite.Group(self.make_blockers(0),
                                            self.make_blockers(1),
                                            self.make_blockers(2),
                                            self.make_blockers(3))"""
        self.keys = key.get_pressed()
        self.clock = time.Clock()
        self.timer = time.get_ticks()
        self.noteTimer = time.get_ticks()
        self.shipTimer = time.get_ticks()
        self.score = score
        self.lives = lives
        self.create_audio()
        self.create_text()
        self.makeNewShip = False
        self.shipAlive = True

    """def make_blockers(self, number):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        blockerGroup = sprite.Group()
        for row in range(4):
            for column in range(9):
                blocker = Blocker(10, GREEN, row, column)
                blocker.rect.x = 50 + (200 * number) + (column * blocker.width)
                blocker.rect.y = 450 + (row * blocker.height)
                blockerGroup.add(blocker)
        return blockerGroup"""

    def reset_lives_sprites(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        self.life1 = Life(715, 3)
        self.life2 = Life(742, 3)
        self.life3 = Life(769, 3)

        if self.lives == 3:
            self.livesGroup = sprite.Group(self.life1, self.life2, self.life3)
        elif self.lives == 2:
            self.livesGroup = sprite.Group(self.life1, self.life2)
        elif self.lives == 1:
            self.livesGroup = sprite.Group(self.life1)

    def reset_lives(self, lives):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        self.lives = lives
        self.reset_lives_sprites()

    def create_audio(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        self.sounds = {}
        for sound_name in ['shoot', 'shoot2', 'invaderkilled', 'mysterykilled',
                           'shipexplosion']:
            self.sounds[sound_name] = mixer.Sound(
                SOUND_PATH + '{}.wav'.format(sound_name))
            self.sounds[sound_name].set_volume(0.2)

        self.musicNotes = [mixer.Sound(SOUND_PATH + '{}.wav'.format(i)) for i
                           in range(4)]
        for sound in self.musicNotes:
            sound.set_volume(0.5)

        self.noteIndex = 0

    def play_main_music(self, currentTime):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        moveTime = self.enemies.sprites()[0].moveTime
        if currentTime - self.noteTimer > moveTime:
            self.note = self.musicNotes[self.noteIndex]
            if self.noteIndex < 3:
                self.noteIndex += 1
            else:
                self.noteIndex = 0

            self.note.play()
            self.noteTimer += moveTime

    def create_text(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        self.titleText = Text(FONT, 50, 'Space Invaders', WHITE, 164, 155)
        self.titleText2 = Text(FONT, 25, 'Press any key to continue', WHITE,
                               201, 225)
        self.gameOverText = Text(FONT, 50, 'Game Over', WHITE, 250, 270)
        self.nextRoundText = Text(FONT, 50, 'Next Round', WHITE, 240, 270)
        self.enemy1Text = Text(FONT, 25, '   =   10 pts', GREEN, 368, 270)
        self.enemy2Text = Text(FONT, 25, '   =  20 pts', BLUE, 368, 320)
        self.enemy3Text = Text(FONT, 25, '   =  30 pts', PURPLE, 368, 370)
        self.enemy4Text = Text(FONT, 25, '   =  ?????', RED, 368, 420)
        self.scoreText = Text(FONT, 20, 'Score', WHITE, 5, 5)
        self.livesText = Text(FONT, 20, 'Lives ', WHITE, 640, 5)

    @staticmethod
    def should_exit(evt):
        # type: (pygame.event.EventType) -> bool
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        return evt.type == QUIT or (evt.type == KEYUP and evt.key == K_ESCAPE)

    def check_input(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        self.keys = key.get_pressed()
        for e in event.get():
            if self.should_exit(e):
                sys.exit()
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    if len(self.bullets) == 0 and self.shipAlive:
                        if self.score < 0: # < 1000:
                            bullet = Bullet(self.player.rect.x + 23,
                                            self.player.rect.y + 5, -1,
                                            15, 'laser', 'center')
                            self.bullets.add(bullet)
                            self.allSprites.add(self.bullets)
                            self.sounds['shoot'].play()

                        else:
                            bullet_l38 = Bullet(self.player.rect.x - 380,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l37 = Bullet(self.player.rect.x - 370,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l36 = Bullet(self.player.rect.x - 360,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l35 = Bullet(self.player.rect.x - 350,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l34 = Bullet(self.player.rect.x - 340,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l33 = Bullet(self.player.rect.x - 330,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l32 = Bullet(self.player.rect.x - 320,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l31 = Bullet(self.player.rect.x - 310,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l30 = Bullet(self.player.rect.x - 300,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l29 = Bullet(self.player.rect.x - 290,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l28 = Bullet(self.player.rect.x - 280,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l27 = Bullet(self.player.rect.x - 270,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l26 = Bullet(self.player.rect.x - 260,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l25 = Bullet(self.player.rect.x - 250,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l24 = Bullet(self.player.rect.x - 240,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l23 = Bullet(self.player.rect.x - 230,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l22 = Bullet(self.player.rect.x - 220,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l21 = Bullet(self.player.rect.x - 210,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l20 = Bullet(self.player.rect.x - 200,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l19 = Bullet(self.player.rect.x - 190,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l18 = Bullet(self.player.rect.x - 180,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l17 = Bullet(self.player.rect.x - 170,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l16 = Bullet(self.player.rect.x - 160,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l15 = Bullet(self.player.rect.x - 150,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l14 = Bullet(self.player.rect.x - 140,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l13 = Bullet(self.player.rect.x - 130,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l12 = Bullet(self.player.rect.x - 120,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l11 = Bullet(self.player.rect.x - 110,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l10 = Bullet(self.player.rect.x - 100,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l9 = Bullet(self.player.rect.x - 90,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l8 = Bullet(self.player.rect.x - 80,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l7 = Bullet(self.player.rect.x - 70,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l6 = Bullet(self.player.rect.x - 60,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l5 = Bullet(self.player.rect.x - 50,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l4 = Bullet(self.player.rect.x - 40,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l3 = Bullet(self.player.rect.x - 30,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l2 = Bullet(self.player.rect.x - 20,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_l1 = Bullet(self.player.rect.x - 10,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'left')
                            bullet_center = Bullet(self.player.rect.x + 0,
                                                self.player.rect.y + 5, -1,
                                                43, 'laser', 'center')
                            bullet_r1 = Bullet(self.player.rect.x + 10,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r2 = Bullet(self.player.rect.x + 20,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r3 = Bullet(self.player.rect.x + 30,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r4 = Bullet(self.player.rect.x + 40,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r5 = Bullet(self.player.rect.x + 50,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r6 = Bullet(self.player.rect.x + 60,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r7 = Bullet(self.player.rect.x + 70,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r8 = Bullet(self.player.rect.x + 80,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r9 = Bullet(self.player.rect.x + 90,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r10 = Bullet(self.player.rect.x + 100,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r11 = Bullet(self.player.rect.x + 110,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r12 = Bullet(self.player.rect.x + 120,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r13 = Bullet(self.player.rect.x + 130,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r14 = Bullet(self.player.rect.x + 140,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r15 = Bullet(self.player.rect.x + 150,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r16 = Bullet(self.player.rect.x + 160,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r17 = Bullet(self.player.rect.x + 170,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r18 = Bullet(self.player.rect.x + 180,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r19 = Bullet(self.player.rect.x + 190,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r20 = Bullet(self.player.rect.x + 200,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r21 = Bullet(self.player.rect.x + 210,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r22 = Bullet(self.player.rect.x + 220,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r23 = Bullet(self.player.rect.x + 230,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r24 = Bullet(self.player.rect.x + 240,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r25 = Bullet(self.player.rect.x + 250,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r26 = Bullet(self.player.rect.x + 260,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r27 = Bullet(self.player.rect.x + 270,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r28 = Bullet(self.player.rect.x + 280,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r29 = Bullet(self.player.rect.x + 290,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r30 = Bullet(self.player.rect.x + 300,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r31 = Bullet(self.player.rect.x + 310,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r32 = Bullet(self.player.rect.x + 320,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r33 = Bullet(self.player.rect.x + 330,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r34 = Bullet(self.player.rect.x + 340,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r35 = Bullet(self.player.rect.x + 350,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r36 = Bullet(self.player.rect.x + 360,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r37 = Bullet(self.player.rect.x + 370,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r38 = Bullet(self.player.rect.x + 380,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r39 = Bullet(self.player.rect.x + 390,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r40 = Bullet(self.player.rect.x + 400,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')
                            bullet_r41 = Bullet(self.player.rect.x + 410,
                                                 self.player.rect.y + 5, -1,
                                                 43, 'laser', 'right')

                            self.bullets.add(bullet_l38)
                            self.bullets.add(bullet_l37)
                            self.bullets.add(bullet_l36)
                            self.bullets.add(bullet_l35)
                            self.bullets.add(bullet_l34)
                            self.bullets.add(bullet_l33)
                            self.bullets.add(bullet_l32)
                            self.bullets.add(bullet_l31)
                            self.bullets.add(bullet_l30)
                            self.bullets.add(bullet_l29)
                            self.bullets.add(bullet_l28)
                            self.bullets.add(bullet_l27)
                            self.bullets.add(bullet_l26)
                            self.bullets.add(bullet_l25)
                            self.bullets.add(bullet_l24)
                            self.bullets.add(bullet_l23)
                            self.bullets.add(bullet_l22)
                            self.bullets.add(bullet_l21)
                            self.bullets.add(bullet_l20)
                            self.bullets.add(bullet_l19)
                            self.bullets.add(bullet_l18)
                            self.bullets.add(bullet_l17)
                            self.bullets.add(bullet_l16)
                            self.bullets.add(bullet_l15)
                            self.bullets.add(bullet_l14)
                            self.bullets.add(bullet_l13)
                            self.bullets.add(bullet_l12)
                            self.bullets.add(bullet_l11)
                            self.bullets.add(bullet_l10)
                            self.bullets.add(bullet_l9)
                            self.bullets.add(bullet_l8)
                            self.bullets.add(bullet_l7)
                            self.bullets.add(bullet_l6)
                            self.bullets.add(bullet_l5)
                            self.bullets.add(bullet_l4)
                            self.bullets.add(bullet_l3)
                            self.bullets.add(bullet_l2)
                            self.bullets.add(bullet_l1)
                            self.bullets.add(bullet_center)
                            self.bullets.add(bullet_r1)
                            self.bullets.add(bullet_r2)
                            self.bullets.add(bullet_r3)
                            self.bullets.add(bullet_r4)
                            self.bullets.add(bullet_r5)
                            self.bullets.add(bullet_r6)
                            self.bullets.add(bullet_r7)
                            self.bullets.add(bullet_r8)
                            self.bullets.add(bullet_r9)
                            self.bullets.add(bullet_r10)
                            self.bullets.add(bullet_r11)
                            self.bullets.add(bullet_r12)
                            self.bullets.add(bullet_r13)
                            self.bullets.add(bullet_r14)
                            self.bullets.add(bullet_r15)
                            self.bullets.add(bullet_r16)
                            self.bullets.add(bullet_r17)
                            self.bullets.add(bullet_r18)
                            self.bullets.add(bullet_r19)
                            self.bullets.add(bullet_r20)
                            self.bullets.add(bullet_r21)
                            self.bullets.add(bullet_r22)
                            self.bullets.add(bullet_r23)
                            self.bullets.add(bullet_r24)
                            self.bullets.add(bullet_r25)
                            self.bullets.add(bullet_r26)
                            self.bullets.add(bullet_r27)
                            self.bullets.add(bullet_r28)
                            self.bullets.add(bullet_r29)
                            self.bullets.add(bullet_r30)
                            self.bullets.add(bullet_r31)
                            self.bullets.add(bullet_r32)
                            self.bullets.add(bullet_r33)
                            self.bullets.add(bullet_r34)
                            self.bullets.add(bullet_r35)
                            self.bullets.add(bullet_r36)
                            self.bullets.add(bullet_r37)
                            self.bullets.add(bullet_r38)
                            self.bullets.add(bullet_r39)
                            self.bullets.add(bullet_r40)
                            self.bullets.add(bullet_r41)


                            bullet2_l38 = Bullet(self.player2.rect.x - 385,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l37 = Bullet(self.player2.rect.x - 375,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l36 = Bullet(self.player2.rect.x - 365,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l35 = Bullet(self.player2.rect.x - 355,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l34 = Bullet(self.player2.rect.x - 345,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l33 = Bullet(self.player2.rect.x - 335,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l32 = Bullet(self.player2.rect.x - 325,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l31 = Bullet(self.player2.rect.x - 315,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l30 = Bullet(self.player2.rect.x - 305,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l29 = Bullet(self.player2.rect.x - 295,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l28 = Bullet(self.player2.rect.x - 285,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l27 = Bullet(self.player2.rect.x - 275,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l26 = Bullet(self.player2.rect.x - 265,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l25 = Bullet(self.player2.rect.x - 255,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l24 = Bullet(self.player2.rect.x - 245,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l23 = Bullet(self.player2.rect.x - 235,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l22 = Bullet(self.player2.rect.x - 225,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l21 = Bullet(self.player2.rect.x - 215,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l20 = Bullet(self.player2.rect.x - 205,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l19 = Bullet(self.player2.rect.x - 195,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l18 = Bullet(self.player2.rect.x - 185,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l17 = Bullet(self.player2.rect.x - 175,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l16 = Bullet(self.player2.rect.x - 165,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l15 = Bullet(self.player2.rect.x - 155,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l14 = Bullet(self.player2.rect.x - 145,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l13 = Bullet(self.player2.rect.x - 135,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l12 = Bullet(self.player2.rect.x - 125,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l11 = Bullet(self.player2.rect.x - 115,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l10 = Bullet(self.player2.rect.x - 105,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l9 = Bullet(self.player2.rect.x - 95,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l8 = Bullet(self.player2.rect.x - 85,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l7 = Bullet(self.player2.rect.x - 75,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l6 = Bullet(self.player2.rect.x - 65,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l5 = Bullet(self.player2.rect.x - 55,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l4 = Bullet(self.player2.rect.x - 45,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l3 = Bullet(self.player2.rect.x - 35,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l2 = Bullet(self.player2.rect.x - 25,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_l1 = Bullet(self.player2.rect.x - 15,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'left')
                            bullet2_center = Bullet(self.player2.rect.x + 5,
                                                self.player2.rect.y + 5, -1,
                                                33, 'laser', 'center')
                            bullet2_r1 = Bullet(self.player2.rect.x + 15,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r2 = Bullet(self.player2.rect.x + 25,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r3 = Bullet(self.player2.rect.x + 35,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r4 = Bullet(self.player2.rect.x + 45,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r5 = Bullet(self.player2.rect.x + 55,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r6 = Bullet(self.player2.rect.x + 65,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r7 = Bullet(self.player2.rect.x + 75,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r8 = Bullet(self.player2.rect.x + 85,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r9 = Bullet(self.player2.rect.x + 95,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r10 = Bullet(self.player2.rect.x + 105,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r11 = Bullet(self.player2.rect.x + 115,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r12 = Bullet(self.player2.rect.x + 125,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r13 = Bullet(self.player2.rect.x + 135,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r14 = Bullet(self.player2.rect.x + 145,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r15 = Bullet(self.player2.rect.x + 155,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r16 = Bullet(self.player2.rect.x + 165,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r17 = Bullet(self.player2.rect.x + 175,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r18 = Bullet(self.player2.rect.x + 185,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r19 = Bullet(self.player2.rect.x + 195,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r20 = Bullet(self.player2.rect.x + 205,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r21 = Bullet(self.player2.rect.x + 215,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r22 = Bullet(self.player2.rect.x + 225,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r23 = Bullet(self.player2.rect.x + 235,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r24 = Bullet(self.player2.rect.x + 245,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r25 = Bullet(self.player2.rect.x + 255,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r26 = Bullet(self.player2.rect.x + 265,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r27 = Bullet(self.player2.rect.x + 275,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r28 = Bullet(self.player2.rect.x + 285,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r29 = Bullet(self.player2.rect.x + 295,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r30 = Bullet(self.player2.rect.x + 305,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r31 = Bullet(self.player2.rect.x + 315,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r32 = Bullet(self.player2.rect.x + 325,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r33 = Bullet(self.player2.rect.x + 335,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r34 = Bullet(self.player2.rect.x + 345,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r35 = Bullet(self.player2.rect.x + 355,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r36 = Bullet(self.player2.rect.x + 365,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r37 = Bullet(self.player2.rect.x + 375,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r38 = Bullet(self.player2.rect.x + 385,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r39 = Bullet(self.player2.rect.x + 395,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r40 = Bullet(self.player2.rect.x + 405,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')
                            bullet2_r41 = Bullet(self.player2.rect.x + 415,
                                                 self.player2.rect.y + 5, -1,
                                                 33, 'laser', 'right')

                            self.bullets.add(bullet2_l38)
                            self.bullets.add(bullet2_l37)
                            self.bullets.add(bullet2_l36)
                            self.bullets.add(bullet2_l35)
                            self.bullets.add(bullet2_l34)
                            self.bullets.add(bullet2_l33)
                            self.bullets.add(bullet2_l32)
                            self.bullets.add(bullet2_l31)
                            self.bullets.add(bullet2_l30)
                            self.bullets.add(bullet2_l29)
                            self.bullets.add(bullet2_l28)
                            self.bullets.add(bullet2_l27)
                            self.bullets.add(bullet2_l26)
                            self.bullets.add(bullet2_l25)
                            self.bullets.add(bullet2_l24)
                            self.bullets.add(bullet2_l23)
                            self.bullets.add(bullet2_l22)
                            self.bullets.add(bullet2_l21)
                            self.bullets.add(bullet2_l20)
                            self.bullets.add(bullet2_l19)
                            self.bullets.add(bullet2_l18)
                            self.bullets.add(bullet2_l17)
                            self.bullets.add(bullet2_l16)
                            self.bullets.add(bullet2_l15)
                            self.bullets.add(bullet2_l14)
                            self.bullets.add(bullet2_l13)
                            self.bullets.add(bullet2_l12)
                            self.bullets.add(bullet2_l11)
                            self.bullets.add(bullet2_l10)
                            self.bullets.add(bullet2_l9)
                            self.bullets.add(bullet2_l8)
                            self.bullets.add(bullet2_l7)
                            self.bullets.add(bullet2_l6)
                            self.bullets.add(bullet2_l5)
                            self.bullets.add(bullet2_l4)
                            self.bullets.add(bullet2_l3)
                            self.bullets.add(bullet2_l2)
                            self.bullets.add(bullet2_l1)
                            self.bullets.add(bullet2_center)
                            self.bullets.add(bullet2_r1)
                            self.bullets.add(bullet2_r2)
                            self.bullets.add(bullet2_r3)
                            self.bullets.add(bullet2_r4)
                            self.bullets.add(bullet2_r5)
                            self.bullets.add(bullet2_r6)
                            self.bullets.add(bullet2_r7)
                            self.bullets.add(bullet2_r8)
                            self.bullets.add(bullet2_r9)
                            self.bullets.add(bullet2_r10)
                            self.bullets.add(bullet2_r11)
                            self.bullets.add(bullet2_r12)
                            self.bullets.add(bullet2_r13)
                            self.bullets.add(bullet2_r14)
                            self.bullets.add(bullet2_r15)
                            self.bullets.add(bullet2_r16)
                            self.bullets.add(bullet2_r17)
                            self.bullets.add(bullet2_r18)
                            self.bullets.add(bullet2_r19)
                            self.bullets.add(bullet2_r20)
                            self.bullets.add(bullet2_r21)
                            self.bullets.add(bullet2_r22)
                            self.bullets.add(bullet2_r23)
                            self.bullets.add(bullet2_r24)
                            self.bullets.add(bullet2_r25)
                            self.bullets.add(bullet2_r26)
                            self.bullets.add(bullet2_r27)
                            self.bullets.add(bullet2_r28)
                            self.bullets.add(bullet2_r29)
                            self.bullets.add(bullet2_r30)
                            self.bullets.add(bullet2_r31)
                            self.bullets.add(bullet2_r32)
                            self.bullets.add(bullet2_r33)
                            self.bullets.add(bullet2_r34)
                            self.bullets.add(bullet2_r35)
                            self.bullets.add(bullet2_r36)
                            self.bullets.add(bullet2_r37)
                            self.bullets.add(bullet2_r38)
                            self.bullets.add(bullet2_r39)
                            self.bullets.add(bullet2_r40)
                            self.bullets.add(bullet2_r41)

                            self.allSprites.add(self.bullets)
                            self.sounds['shoot2'].play()


    def make_enemies(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        enemies = EnemiesGroup(10, 5)
        for row in range(5):
            for column in range(10):
                enemy = Enemy(row, column)
                enemy.rect.x = 157 + (column * 50)
                enemy.rect.y = self.enemyPosition + (row * 45)
                enemies.add(enemy)

        self.enemies = enemies
        self.allSprites = sprite.Group(self.player, self.player2, self.enemies,
                                       self.livesGroup, self.mysteryShip)

    def make_enemies_shoot(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        if (time.get_ticks() - self.timer) > 700:
            enemy = self.enemies.random_bottom()
            if enemy:
                self.enemyBullets.add(
                    Bullet(enemy.rect.x + 14, enemy.rect.y + 20, 1, 5,
                           'enemylaser', 'center'))
                self.allSprites.add(self.enemyBullets)
                self.timer = time.get_ticks()

    def calculate_score(self, row):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        scores = {0: 30,
                  1: 20,
                  2: 20,
                  3: 10,
                  4: 10,
                  5: choice([50, 100, 150, 300])
                  }

        score = scores[row]
        self.score += score
        return score

    def create_main_menu(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        self.enemy1 = IMAGES['enemy3_1']
        self.enemy1 = transform.scale(self.enemy1, (40, 40))
        self.enemy2 = IMAGES['enemy2_2']
        self.enemy2 = transform.scale(self.enemy2, (40, 40))
        self.enemy3 = IMAGES['enemy1_2']
        self.enemy3 = transform.scale(self.enemy3, (40, 40))
        self.enemy4 = IMAGES['mystery']
        self.enemy4 = transform.scale(self.enemy4, (80, 40))
        self.screen.blit(self.enemy1, (318, 270))
        self.screen.blit(self.enemy2, (318, 320))
        self.screen.blit(self.enemy3, (318, 370))
        self.screen.blit(self.enemy4, (299, 420))

        for e in event.get():
            if self.should_exit(e):
                sys.exit()
            if e.type == KEYUP:
                self.startGame = True
                self.mainScreen = False

    def update_enemy_speed(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        if len(self.enemies) <= 10:
            for enemy in self.enemies:
                enemy.moveTime = 400
        if len(self.enemies) == 1:
            for enemy in self.enemies:
                enemy.moveTime = 200

    def check_collisions(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        collidedict = sprite.groupcollide(self.bullets, self.enemyBullets,
                                          True, False)
        if collidedict:
            for value in collidedict.values():
                for currentSprite in value:
                    self.enemyBullets.remove(currentSprite)
                    self.allSprites.remove(currentSprite)

        enemiesdict = sprite.groupcollide(self.bullets, self.enemies,
                                          True, False)
        if enemiesdict:
            for value in enemiesdict.values():
                for currentSprite in value:
                    self.enemies.kill(currentSprite)
                    self.sounds['invaderkilled'].play()
                    score = self.calculate_score(currentSprite.row)
                    explosion = Explosion(currentSprite.rect.x,
                                          currentSprite.rect.y,
                                          currentSprite.row, False, False,
                                          score)
                    self.explosionsGroup.add(explosion)
                    self.allSprites.remove(currentSprite)
                    self.enemies.remove(currentSprite)
                    self.gameTimer = time.get_ticks()
                    break

        mysterydict = sprite.groupcollide(self.bullets, self.mysteryGroup,
                                          True, True)
        if mysterydict:
            for value in mysterydict.values():
                for currentSprite in value:
                    currentSprite.mysteryEntered.stop()
                    self.sounds['mysterykilled'].play()
                    score = self.calculate_score(currentSprite.row)
                    explosion = Explosion(currentSprite.rect.x,
                                          currentSprite.rect.y,
                                          currentSprite.row, False, True,
                                          score)
                    self.explosionsGroup.add(explosion)
                    self.allSprites.remove(currentSprite)
                    self.mysteryGroup.remove(currentSprite)
                    newShip = Mystery()
                    self.allSprites.add(newShip)
                    self.mysteryGroup.add(newShip)
                    break

        bulletsdict = sprite.groupcollide(self.enemyBullets, self.playerGroup,
                                          True, False)
        if bulletsdict:
            for value in bulletsdict.values():
                for playerShip in value:
                    if self.lives == 3:
                        self.lives -= 1
                        self.livesGroup.remove(self.life3)
                        self.allSprites.remove(self.life3)
                    elif self.lives == 2:
                        self.lives -= 1
                        self.livesGroup.remove(self.life2)
                        self.allSprites.remove(self.life2)
                    elif self.lives == 1:
                        self.lives -= 1
                        self.livesGroup.remove(self.life1)
                        self.allSprites.remove(self.life1)
                    elif self.lives == 0:
                        self.gameOver = True
                        self.startGame = False
                    self.sounds['shipexplosion'].play()
                    explosion = Explosion(playerShip.rect.x, playerShip.rect.y,
                                          0, True, False, 0)
                    self.explosionsGroup.add(explosion)
                    self.allSprites.remove(playerShip)
                    self.playerGroup.remove(playerShip)
                    self.makeNewShip = True
                    self.shipTimer = time.get_ticks()
                    self.shipAlive = False

        if sprite.groupcollide(self.enemies, self.playerGroup, True, True):
            self.gameOver = True
            self.startGame = False

        """sprite.groupcollide(self.bullets, self.allBlockers, True, True)
        sprite.groupcollide(self.enemyBullets, self.allBlockers, True, True)
        sprite.groupcollide(self.enemies, self.allBlockers, False, True)"""

    def create_new_ship(self, createShip, currentTime):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        if createShip and (currentTime - self.shipTimer > 900):
            self.player = Ship()
            self.player2 = Ship2()
            self.allSprites.add(self.player)
            self.playerGroup.add(self.player)
            self.allSprites.add(self.player2)
            self.playerGroup.add(self.player2)
            self.makeNewShip = False
            self.shipAlive = True

    def create_game_over(self, currentTime):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        self.screen.blit(self.background, (0, 0))
        passed = currentTime - self.timer
        if passed < 750:
            self.gameOverText.draw(self.screen)
        elif 750 < passed < 1500:
            self.screen.blit(self.background, (0, 0))
        elif 1500 < passed < 2250:
            self.gameOverText.draw(self.screen)
        elif 2250 < passed < 2750:
            self.screen.blit(self.background, (0, 0))
        elif passed > 3000:
            self.mainScreen = True

        for e in event.get():
            if self.should_exit(e):
                sys.exit()

    def main(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        while True:
            if self.mainScreen:
                self.reset(0, 3, True)
                self.screen.blit(self.background, (0, 0))
                self.titleText.draw(self.screen)
                self.titleText2.draw(self.screen)
                self.enemy1Text.draw(self.screen)
                self.enemy2Text.draw(self.screen)
                self.enemy3Text.draw(self.screen)
                self.enemy4Text.draw(self.screen)
                self.create_main_menu()

            elif self.startGame:
                if len(self.enemies) == 0:
                    currentTime = time.get_ticks()
                    if currentTime - self.gameTimer < 3000:
                        self.screen.blit(self.background, (0, 0))
                        self.scoreText2 = Text(FONT, 20, str(self.score),
                                               GREEN, 85, 5)
                        self.scoreText.draw(self.screen)
                        self.scoreText2.draw(self.screen)
                        self.nextRoundText.draw(self.screen)
                        self.livesText.draw(self.screen)
                        self.livesGroup.update(self.keys)
                        self.check_input()
                    if currentTime - self.gameTimer > 3000:
                        # Move enemies closer to bottom
                        self.enemyPositionStart += 35
                        self.reset(self.score, self.lives)
                        self.gameTimer += 3000
                else:
                    currentTime = time.get_ticks()
                    self.play_main_music(currentTime)
                    self.screen.blit(self.background, (0, 0))
                    # self.allBlockers.update(self.screen)
                    self.scoreText2 = Text(FONT, 20, str(self.score), GREEN,
                                           85, 5)
                    self.scoreText.draw(self.screen)
                    self.scoreText2.draw(self.screen)
                    self.livesText.draw(self.screen)
                    self.check_input()
                    self.allSprites.update(self.keys, currentTime,
                                           self.enemies)
                    self.explosionsGroup.update(self.keys, currentTime)
                    self.check_collisions()
                    self.create_new_ship(self.makeNewShip, currentTime)
                    self.update_enemy_speed()

                    if len(self.enemies) > 0:
                        self.make_enemies_shoot()

            elif self.gameOver:
                currentTime = time.get_ticks()
                # Reset enemy starting position
                self.enemyPositionStart = self.enemyPositionDefault
                self.create_game_over(currentTime)

            display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    game = SpaceInvaders()
    game.main()
