from .board import Board
from .displays.pygame_display import PygameDisplay

import pygame, sys
from pygame.locals import *

class Game:
  def __init__(self):
    self.board = Board()
    self.display = PygameDisplay(self.board)


  def start(self):
    self.game_loop()
    # self.finish()

  def game_loop(self):
    self.display.draw()
    while True:
      event = pygame.event.wait()
      if event.type==QUIT:
        pygame.quit()
        sys.exit()

      if event.type == MOUSEBUTTONDOWN and event.button == 1:
      #   print('Position: ', event.pos)
      #   board_x = int(event.pos[0] / 200)
      #   board_y = int(event.pos[1] / 200)
      #   return [board_x, board_y]
        self.display.draw()
    self.board.show()


    # while not self.board.is_finished():
      # self.displays[self.current_player-1].draw()
      # if self.output_enabled: self.board.show_player_info(self.current_player)
      # self.handle_input()
      # self.switch_player()