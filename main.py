from board import *
import sys
import random
from time import *


class Main:
    def __init__(self):
        sys.setrecursionlimit(10000000)

    def recursion(self, board, solution, n=0):
        possible_moves = self.check_move(board)
        #Note: expencive operation ~+10s but returns different solutions every time
        random.shuffle(possible_moves)
        if len(possible_moves) == 0:
            if self.check_win(board) == True:
                #for i in range(10):
                    #print ""
                #print "                          YOU WON at:", n
                #for i in range(10):
                    #print ""
                return True
            else:
                return False


        #print "Es gibt so viele Moves: ", len(possible_moves)
        for j in range(len(possible_moves)):
            dir, x, y= possible_moves[j]
            board = board.create_copy()
            #board.print_board()
            self.play_move(dir, x, y, board)
            #print "Mein Zug ist dir=", dir, " x= ", x , " y = ", y , " --> folgendes Board"
            #board.print_board()
            #board.print_board()
            #if n == 1000 or n == 2000 or n == 3000:
                #print "Rekursionstiefe: ", n
            #if n == 300:
                #board.print_board()
                #print possible_moves
            #if n == 301:
                #board.print_board()
                #print possible_moves
            #if n == 302:
                #board.print_board()
                #print possible_moves
            #if n == 303:
                #board.print_board()
                #print possible_moves
            #if n == 304:
                #board.print_board()
                #print possible_moves
            if self.recursion(board, solution, n+1) == True:
                #print "Move ", n
                #board.print_board()
                solution.append(board)
                return True
            #return solution


    def check_move(self, board):
    # NOTE: Die next-vielte Loesung wird zurueckgegeben
    # NOTE: Es wird bei einer gefundenen Loesung immer die Richtung zurueckgegeben
        moves = []

        for y in range(7):
            for x in range(7):
                if board.inside_board(x, y):
                    if board.get_position(x, y) == 1:

                        # NOTE: horizontal rechts
                        if board.inside_board(x+2, y):
                            if board.get_position(x+2, y) == 0 and board.get_position(x+1, y) == 1:
                                #print "proc1 x=",x, " y=",y
                                moves.append((board.DIR_EAST, x, y))
                        # NOTE: horizontal links
                        if board.inside_board(x-2, y):
                            if board.get_position(x-2, y) == 0 and board.get_position(x-1, y) == 1:
                                #print "proc2 x=",x, " y=",y, " and ", x-2, "," , y, " is inside"
                                moves.append((board.DIR_WEST, x, y))
                        # NOTE: vertikal oben
                        if board.inside_board(x, y-2):
                            if board.get_position(x, y-2) == 0 and board.get_position(x, y-1) == 1:
                                #print "proc3 x=",x, " y=",y, " and ", x, "," , y-2, " is inside"
                                moves.append((board.DIR_NORTH, x, y))
                        # NOTE: vertikal unten
                        if board.inside_board(x, y+2):
                            if board.get_position(x, y+2) == 0 and board.get_position(x, y+1) == 1:
                                #print "proc4 x=",x, " y=",y
                                moves.append((board.DIR_SOUTH, x, y))
        return moves

    def play_move(self, dir, x, y, board):
        if dir == board.DIR_EAST:
            board.set_position(x, y, 0)
            board.set_position(x+1, y, 0)
            board.set_position(x+2, y, 1)
        if dir == board.DIR_WEST:
            board.set_position(x, y, 0)
            board.set_position(x-1, y, 0)
            board.set_position(x-2, y, 1)
        if dir == board.DIR_NORTH:
            board.set_position(x, y, 0)
            board.set_position(x, y-1, 0)
            board.set_position(x, y-2, 1)
        if dir == board.DIR_SOUTH:
            board.set_position(x, y, 0)
            board.set_position(x, y+1, 0)
            board.set_position(x, y+2, 1)

        return board


    def check_win(self, board):
        counter = 0
        for a in range(7):
            for b in range(7):
                if board.get_position(a, b) == 1:
                    counter+=1
                    if counter > 1:
                        return False
        if counter == 1:
            return True
        else:
            return False

    def print_solutions(self,solution):
        solution_len = len(solution)
        turn = 0
        while solution_len != 0:
            turn+=1
            print "ZUG",turn
            print "-------"
            solution[solution_len-1].print_board()
            print " "
            solution_len-=1
        solution_len = len(solution)
        print "Loesung nach",solution_len,"Zuegen."
        print " "
