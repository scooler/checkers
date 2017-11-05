import numpy as np

class Board:
  """
  0 - black
  1 - white
  """
  def __init__(self):
    board = [
      [0, 1] * 4,
      [1, 0] * 4
    ] * 4
    players_board = [
      [0, 1] * 4, # player 1
      [1, 0] * 4
    ] + [[0] * 8] * 4 + [ # 4 rows of nothing
    [0, 2] * 4, # player 2
      [2, 0] * 4
    ]
    self.board = np.array(board)
    self.players_board = np.array(players_board)
    self.x_size = 8
    self.y_size = 8


  # def move(self, x, y, current_player):
  #   self.board[x, y] = current_player


  # def are_same_and_non_zero(self, array):
  #   return np.unique(array).size == 1 and array[0] != 0

  # def is_board_full(self):
  #   return not np.any(np.unique(self.board) == 0)

  def is_finished(self):
    """is game finished"""
    return True
    # for i in range(0, self.x_size):                     # rows
    #   if self.are_same_and_non_zero(self.board[i, :]):
    #     self.player_who_won = self.board[i, 0]
    #     self.result = 'Won {} - row {}'.format(self.player(self.player_who_won), i)
    #     return True

    # for i in range(0, self.y_size):                     # columns
    #   if self.are_same_and_non_zero(self.board[:, i]):
    #     self.player_who_won = self.board[0, i]
    #     self.result = 'Won {} - col {}'.format(self.player(self.player_who_won), i)
    #     return True

    # if self.are_same_and_non_zero(np.diag(self.board)): # diagonal
    #   self.player_who_won = self.board[1, 1]
    #   self.result = 'Won {} - diagonal {}'.format(self.player(self.player_who_won), i)
    #   return True

    # if self.are_same_and_non_zero(np.diag(np.flipud(self.board))): # anty-diagonal
    #   self.player_who_won = self.board[1, 1]
    #   self.result = 'Won {} - anty-diagonal {}'.format(self.player(self.player_who_won), i)

    #   return True

    # if self.is_board_full():
    #   self.player_who_won = 0 # nobody
    #   self.result = 'Draw'
    #   return True # draw

    return False

  def show(self):
    # print(self.board)
    # print(self.players_board)
    return


  # def player(self, player_no):
  #   if player_no == 1: return 'Player 1 (X)'
  #   if player_no == 2: return 'Player 2 (O)'

  # def show_player_info(self, player_no):
  #   print("It's turn of ", self.player(player_no))
