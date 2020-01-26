from board import *
from main import *
from time import *
from random import *

board = Board()
main = Main()

#print board.inside_board(1,5)
print "Programm zur Loesungsfindung zum Solitaerbrettspiel - Informatik Projekt von Erik Haarlaender und Max Kessler"
print " "
start = time()
for i in range(randint(1, 10)):
    print " "
    print "PROCESSING --- Please stand by!"
    solution = []
    main.recursion(board, solution)
    main.print_solutions(solution)
end = time()
time = end - start

print i, "solutions given in ", round(time), " seconds"


