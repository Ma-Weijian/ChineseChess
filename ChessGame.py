from ChessBoard import *
from ChessView import ChessView
# from main import *
import tkinter

def real_coord(x):
    if x <= 50:
        return 0
    else:
        return int((x-50)/40) + 1


def board_coord(x):
    return 30 + 40*x


class ChessGame:

    board = ChessBoard()
    player_is_red = True
    def __init__(self):
        self.view = ChessView(self)
        self.view.showMsg("Red")
        self.view.draw_board(self.board)

    def start(self):
        self.view.start()

    def callback(self, event):
        print(event.x, event.y)
        rx, ry = real_coord(event.x), real_coord(event.y)
        # print(rx,ry,self.board.select(rx, ry, self.player_is_red))
        if self.board.select(rx, ry, self.player_is_red):
            # 只有走子完成，才会返回true，同时进入对方走子的状态
            self.player_is_red = not self.player_is_red
            self.view.showMsg("Red" if self.player_is_red else "Green")
        self.view.draw_board(self.board)

game = ChessGame()
game.start()
