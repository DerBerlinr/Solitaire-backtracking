class Main:
    def __init__(self):
        counter=0


    def create_field(self):
        self.field = []
        temp = []
        for i in range(9):
            for j in range(9):
                if i == 4 and j == 4:
                    temp.append(0)
                else:
                    if i < 3 or i > 5:
                        if j < 3 or j > 5:
                            temp.append(None)
                        else:
                            temp.append(1)
                    else:
                        temp.append(1)

            self.field.append(temp)
            temp = []



    def check_killmove(self):
        for i in range(9):
            for j in range(9):
                if self.field[i][j] == 1:
                    # NOTE: horizontal rechts
                    if not j > 6:
                        if self.field[i][j+2]==0 and self.field[i][j+1]==1:
                            print "horizontal rechts moeglich fuer Feld: ", i, j
                            return 1, i , j
                    # NOTE: horizontal links
                    elif not j < 2:
                        if self.field[i][j-2]==0 and self.field[i][j-1]==1:
                            print "horizontal links moeglich fuer Feld: ", i, j
                            return 2, i, j
                    # NOTE: vertikal oben
                    elif not i < 2:
                        if self.field[i-2][j]==0 and self.field[i-1][j]==1:
                            print "vertikal oben moeglich fuer Feld: ", i, j
                            return 3, i, j
                    # NOTE: vertikal unten
                    elif not i > 6:
                        if self.field[i+2][j]==0 and self.field[i+1][j]==1:
                            print "vertikal unten moeglich fuer Feld: ", i, j
                            return 4, i, j
                    else:
                        return 0, 0, 0


    def check_win(self):
        counter = 0
        for i in range(9):
            for j in range(9):
                if self.field[i][j]==1:
                    counter+=1
        if counter == 1:
            return 1
        else:
            return 0

    def check_killmove_dir(self,dir):
        if not None:
            # NOTE: horizontal rechts
            if not j > 6 and dir == 1:
                if self.field[i][j+2]==0 and self.field[i][j+1]==1:
                    print "horizontal rechts moeglich fuer Feld: ", i, j
                    return 1
            # NOTE: horizontal links
            if not j < 2 and dir == 2:
                if self.field[i][j-2]==0 and self.field[i][j-1]==1:
                    print "horizontal links moeglich fuer Feld: ", i, j
                    return 2
            # NOTE: vertikal oben
            if not i < 2 and dir == 3:
                if self.field[i-2][j]==0 and self.field[i-1][j]==1:
                    print "vertikal oben moeglich fuer Feld: ", i, j
                    return 3
            # NOTE: vertikal unten
            if not i > 6 and dir == 4:
                if self.field[i+2][j]==0 and self.field[i+1][j]==1:
                    print "vertikal unten moeglich fuer Feld: ", i, j
                    return 4
        return 0


    def play_killmove(self, dir, i, j):
        if dir == 1:
            self.field[i][j]=0
            self.field[i][j+2]=1
            self.field[i][j+1]=0
        if dir == 2:
            self.field[i][j]=0
            self.field[i][j-2]=1
            self.field[i][j-1]=0
        if dir == 3:
            self.field[i][j]=0
            self.field[i-2][j]=1
            self.field[i-1][j]=0
        if dir == 4:
            self.field[i][j]=0
            self.field[i+2][j]=1
            self.field[i+1][j]=0

    def remove_killmove(self, dir):
        if dir == 1:
            self.field[i][j]=1
            self.field[i][j+2]=0
            self.field[i][j+1]=1
        if dir == 2:
            self.field[i][j]=1
            self.field[i][j-2]=0
            self.field[i][j-1]=1
        if dir == 3:
            self.field[i][j]=1
            self.field[i-2][j]=0
            self.field[i-1][j]=1
        if dir == 4:
            self.field[i][j]=1
            self.field[i+2][j]=0
            self.field[i+1][j]=1

    def print_field(self):
        for k in range(9):
            print self.field[k]


    def recursion(self, all_dir=[], next=0):
        self.print_field()
        # NOTE: all_dir gibt die Richtung aller Moves an, um diese Rueckgaengig zu machen
        if self.check_killmove() != 0 and not self.check_win() and next == 1:
            for i in range(1, 4):
                if check_killmove_dir(i):
                    play_killmove(check_killmove() + i)
            all_dir.append(check_killmove() + 1)
            recursion(all_dir)
        elif self.check_killmove() != 0 and not self.check_win() == 1:
            aa, bb, cc = self.check_killmove()
            self.play_killmove(aa, bb, cc)
            print "1."
            all_dir.append(self.check_killmove())
            self.recursion(all_dir)
        elif self.check_killmove() == 0 and not self.check_win() == 1:
            # NOTE: keine zuege mehr
            print all_dir
            self.remove_killmove(all_dir[len(all_dir)-1])
            all_dir.pop()
            recursion(all_dir, 1)
        elif self.check_killmove() == 0 and self.check_win():
            # NOTE: win
            exit()













    def kys(self):
        pass
