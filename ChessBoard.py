from chessman.Bing import *
from chessman.Shuai import *
from chessman.Pao import *
from chessman.Shi import *
from chessman.Xiang import *
from chessman.Ma import *
from chessman.Che import *


class ChessBoard:
    pieces = dict()
    pieces[4, 0] = Shuai(4, 0, True)

    pieces[0, 3] = Bing(0, 3, True)
    pieces[2, 3] = Bing(2, 3, True)
    pieces[4, 3] = Bing(4, 3, True)
    pieces[6, 3] = Bing(6, 3, True)
    pieces[8, 3] = Bing(8, 3, True)

    pieces[1,2] = Pao(1, 2, True)
    pieces[7,2] = Pao(7, 2, True)

    pieces[3,0] = Shi(3, 0, True)
    pieces[5,0] = Shi(5, 0, True)

    pieces[2,0] = Xiang(2, 0, True)
    pieces[6,0] = Xiang(6, 0, True)

    pieces[1, 0] = Ma(1, 0, True)
    pieces[7, 0] = Ma(7, 0, True)

    pieces[0, 0] = Che(0, 0, True)
    pieces[8, 0] = Che(8, 0, True)



    pieces[4, 9] = Shuai(4, 9, False)

    pieces[0, 6] = Bing(0, 6, False)
    pieces[2, 6] = Bing(2, 6, False)
    pieces[4, 6] = Bing(4, 6, False)
    pieces[6, 6] = Bing(6, 6, False)
    pieces[8, 6] = Bing(8, 6, False)

    pieces[1,7] = Pao(1, 7, False)
    pieces[7,7] = Pao(7, 7, False)

    pieces[3,9] = Shi(3, 9, False)
    pieces[5,9] = Shi(5, 9, False)

    pieces[2,9] = Xiang(2, 9, False)
    pieces[6,9] = Xiang(6, 9, False)

    pieces[1, 9] = Ma(1, 9, False)
    pieces[7, 9] = Ma(7, 9, False)

    pieces[0, 9] = Che(0, 9, False)
    pieces[8, 9] = Che(8, 9, False)

    selected_piece = None

    def __init__(self):
        pass

    def can_move(self, x, y, dx, dy):
        return self.pieces[x, y].can_move(self, dx, dy)

    def move(self, x, y, dx, dy):
        return self.pieces[x, y].move(self, dx, dy)

    def remove(self, x, y):
        del self.pieces[x, y]

    def select(self, x, y, player_is_red):
        # 返回true，代表走子完成，返回false，代表走子未完成
        # 如果没有选子，那么要先选自己要走的子
        if not self.selected_piece:
            # 如果选的是自己的子
            if (x, y) in self.pieces and self.pieces[x, y].is_red == player_is_red:
                # 改变board上的子的状态，以及board上面选了那个子
                self.pieces[x, y].selected = True
                self.selected_piece = self.pieces[x, y]
            return False

        # 如果选中的不是子
        if not (x, y) in self.pieces:
            # 如果前一次点击已经选了子了
            if self.selected_piece:
                ox, oy = self.selected_piece.x, self.selected_piece.y
                # 如果能往这里走
                if self.can_move(ox, oy, x-ox, y-oy):
                    # 走子，返回走子完成，释放selected piece
                    self.move(ox, oy, x-ox, y-oy)
                    self.pieces[x,y].selected = False
                    self.selected_piece = None
                    return True
            # 否则返回false
            return False

        if self.pieces[x, y].selected:
        # 选同一个子
            return False

        if self.pieces[x, y].is_red != player_is_red:
        # 吃对方子的情况。
            ox, oy = self.selected_piece.x, self.selected_piece.y
            if self.can_move(ox, oy, x-ox, y-oy):
                self.move(ox, oy, x-ox, y-oy)
                self.pieces[x,y].selected = False
                self.selected_piece = None
                return True
            return False
        for key in self.pieces.keys():
            self.pieces[key].selected = False
        self.pieces[x, y].selected = True
        self.selected_piece = self.pieces[x,y]
        return False