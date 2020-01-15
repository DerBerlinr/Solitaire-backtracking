class Main:
    def __init__(self):
        pass

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
        for k in range(9):
            print self.field[k]

    def check_killmove(self):
        for i in range(9):
            for j in range(9):
                if not None:
                    # NOTE: horizontal rechts
                    if not j > 6:
                        if self.field[i][j+2]==0 and self.field[i][j+1]==1:
                            print "horizontal rechts moeglich fuer Feld: ", i, j
                    # NOTE: horizontal links
                    if not j < 2:
                        if self.field[i][j-2]==0 and self.field[i][j-1]==1:
                            print "horizontal links moeglich fuer Feld: ", i, j
                    # NOTE: vertikal oben
                    if not i < 2:
                        if self.field[i-2][j]==0 and self.field[i-1][j]==1:
                            print "vertikal oben moeglich fuer Feld: ", i, j
                    # NOTE: vertikal unten
                    if not i > 6:
                        if self.field[i+2][j]==0 and self.field[i+1][j]==1:
                            print "vertikal unten moeglich fuer Feld: ", i, j

    def play_killmove(self):
        pass
