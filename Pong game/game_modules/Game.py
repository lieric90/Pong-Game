from Ball import *
from Player import *
from constants import *

class Game():
    def __init__ (self):

#creates player and ball objects
        self.player1 = Player(100 , SCREEN_SIZE[1]/2)
        self.player2 = Player(SCREEN_SIZE[0] - 100 , SCREEN_SIZE[1]/2)

        self.ball = Ball(400,300) 

#initializes pygame library
        pygame.init()
        pygame.display.set_caption('PONG!')
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()

    def update(self):
        self.player1.update()
        self.player2.update()
        self.ball.update()
        self.draw_game()
        self.check_collision()
#sets constant fps
        self.clock.tick(FPS)
#updates screen
        pygame.display.flip()

        for event in pygame.event.get():

            #when a key is pressed down
            if event.type == pygame.KEYDOWN:
                #player movement in x axis using left and right arrow keys
                if event.key==pygame.K_UP:
                    self.player2.moveup()
                elif event.key==pygame.K_DOWN:
                    self.player2.movedown()
                if event.key == pygame.K_w:
                    self.player1.moveup()
                elif event.key==pygame.K_s:
                    self.player1.movedown()
            #quits game if x clicked on top right of screen
            if event.type == pygame.QUIT: 
                return True
    def check_collision(self):
        if self.player2.pos_x < self.ball.pos_x < self.player2.pos_x + 20:
            if self.player2.pos_y < self.ball.pos_y < self.player2.pos_y + 70:
                self.ball.velocityX = -1
        if self.player1.pos_x < self.ball.pos_x < self.player1.pos_x + 20:
            if self.player1.pos_y < self.ball.pos_y < self.player1.pos_y + 70:
                self.ball.velocityX = 1
    def draw_game(self):
        self.screen.fill([0,0,0])
        self.player1.draw_paddle(self.screen)
        self.player2.draw_paddle(self.screen)
        self.ball.draw_ball(self.screen)
