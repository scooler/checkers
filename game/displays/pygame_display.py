import pygame
from pygame.locals import Rect

SCREEN_SIZE = (800, 800) # this has to be a square
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
BLACK_PLAYER_COLOR = (50, 50, 50)
WHITE_PLAYER_COLOR = (200, 200, 200)

class PygameDisplay:
  def __init__(self, board):
    pygame.init()

    self.window = pygame.display.set_mode(SCREEN_SIZE)
    self.window.fill((0,0,0))
    self.board = board
    self.step_x = int(SCREEN_SIZE[0]/self.board.x_size)
    self.step_y = int(SCREEN_SIZE[1]/self.board.y_size)

  def draw(self):
    self.window.fill((0,0,0))
    self.draw_board()
    self.draw_players()
    pygame.display.update()
    # self.draw_selections()

  def draw_board(self):
    for i in range(0, self.board.x_size):
      for j in range(0, self.board.y_size):
        if self.board.board[i, j] == 1:
          pygame.draw.rect(self.window, WHITE_COLOR, Rect((j*self.step_x, i*self.step_y), (100, 100))) #, 2

  def draw_players(self):
    for i in range(0, self.board.x_size):
      for j in range(0, self.board.y_size):
        x = self.step_x * j
        y = self.step_y * i
        if self.board.players_board[j, i] == 1:
          self.draw_white(x , y)
        else:
          if self.board.players_board[j, i] == 2:
            self.draw_black(x , y)


  def draw_white(self, x, y):
    pos = (int(x + self.step_x/2), int(y + self.step_y/2))
    r = int(self.step_x/2)
    pygame.draw.circle(self.window, WHITE_PLAYER_COLOR, pos, r, 5)


  def draw_black(self, x, y):
    pos = (int(x + self.step_x/2), int(y + self.step_y/2))
    r = int(self.step_x/2)
    pygame.draw.circle(self.window, BLACK_PLAYER_COLOR, pos, r, 5)

  # def input(self, x, y, current_player): # here it's a raw mouse input (x & y are screen coordinates)
  #   print("x: ", x, "y: ", y)
  #   board_x = int(x / 200)
  #   board_y = int(y / 200)
  #   self.board.move(board_x, board_y, current_player)
