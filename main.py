class Main:
    def __init__(self):
        self.field = []

    def create_field(self):
        temp = []
        for y in range(7):
            for x in range(7):
                if y == 3 and x == 3:
                    temp.append(0)
                else:
                    if y < 2 or y > 4:
                        if x < 2 or x > 4:
                            temp.append(5)
                        else:
                            temp.append(1)
                    else:
                        temp.append(1)

            self.field.append(temp)
            temp = []

    def check_killmove(self, next=0):
        counter = 0
        for y in range(7):
            for x in range(7):
                if self.field[y][x] == 1:
                    # NOTE: horizontal rechts
                    if x <= 4:
                        if self.field[y][x + 2] == 0 and self.field[y][x + 1] == 1:
                            if counter == next:
                                print "horizontal rechts moeglich fuer Feld: ", y + 1, x + 1
                                return 1, y, x
                            else:
                                counter += 1
                    # NOTE: horizontal links
                    if x >= 2:
                        if self.field[y][x - 2] == 0 and self.field[y][x - 1] == 1:
                            if counter == next:
                                print "horizontal links moeglich fuer Feld: ", y + 1, x + 1
                                return 2, y, x
                            else:
                                counter += 1
                    # NOTE: vertikal
                    if y >= 2:
                        if self.field[y - 2][x] == 0 and self.field[y - 1][x] == 1:
                            if counter == next:
                                print "vertikal oben moeglich fuer Feld: ", y + 1, x + 1
                                return 3, y, x
                            else:
                                counter += 1
                    # NOTE: vertikal unten
                    if y <= 4:
                        if self.field[y + 2][x] == 0 and self.field[y + 1][x] == 1:
                            if counter == next:
                                print "vertikal unten moeglich fuer Feld: ", y + 1, x + 1
                                return 4, y, x
                            else:
                                counter +=1
        return 0, 0, 0

    def check_win(self):
        counter = 0
        for y in range(7):
            for x in range(7):
                if self.field[y][x] == 1:
                    counter += 1
                if counter == 2:
                    return 0
        if counter == 1:
            return 1
        else:
            return 0

    def check_killmove_dir(self, direction, y, x):
        if not None:
            # NOTE: horizontal rechts
            if not x > 5 and direction == 1:
                if self.field[y][x + 2] == 0 and self.field[y][x + 1] == 1:
                    print "horizontal rechts moeglich fuer Feld: ", y+1, x+1
                    return 1, y, x
            # NOTE: horizontal links
            if not x < 2 and direction == 2:
                if self.field[y][x - 2] == 0 and self.field[y][x - 1] == 1:
                    print "horizontal links moeglich fuer Feld: ", y+1, x+1
                    return 2, y, x
            # NOTE: vertikal oben
            if not y < 2 and direction == 3:
                if self.field[y - 2][x] == 0 and self.field[y - 1][x] == 1:
                    print "vertikal oben moeglich fuer Feld: ", y+1, x+1
                    return 3, y, x
            # NOTE: vertikal unten
            if y < 5 and direction == 4:
                if self.field[y + 2][x] == 0 and self.field[y + 1][x] == 1:
                    print "vertikal unten moeglich fuer Feld: ", y+1, x+1
                    return 4, y, x
        return 0, 0, 0

    def play_killmove(self, dir, y, x):
        if dir == 1:
            self.field[y][x] = 0
            self.field[y][x + 2] = 1
            self.field[y][x + 1] = 0
        if dir == 2:
            self.field[y][x] = 0
            self.field[y][x - 2] = 1
            self.field[y][x - 1] = 0
        if dir == 3:
            self.field[y][x] = 0
            self.field[y - 2][x] = 1
            self.field[y - 1][x] = 0
        if dir == 4:
            self.field[y][x] = 0
            self.field[y + 2][x] = 1
            self.field[y + 1][x] = 0

    def remove_killmove(self, dir, y, x):
        if dir == 1 and x < 5:
            self.field[y][x] = 1
            self.field[y][x + 2] = 0
            self.field[y][x + 1] = 1
        if dir == 2:
            self.field[y][x] = 1
            self.field[y][x - 2] = 0
            self.field[y][x - 1] = 1
        if dir == 3:
            self.field[y][x] = 1
            self.field[y - 2][x] = 0
            self.field[y - 1][x] = 1
        if dir == 4 and y < 5:
            self.field[y][x] = 1
            self.field[y + 2][x] = 0
            self.field[y + 1][x] = 1

    def print_field(self):
        for k in range(7):
            print self.field[k]

    def recursion(self, all_dir=[], all_pos=[], next=0):
        self.print_field()
        # NOTE: all_dir gibt die Richtung aller Moves an, um diese Rueckgaengig zu machen
        # TODO: geht alles eigentlich, nur in der Praxis nicht
        kill = False
        if self.check_killmove() != (0, 0, 0) and not self.check_win() and next == 1:
            dir, y, x = self.check_killmove()
            last_y, last_x = all_pos[len(all_pos)-1]
            print ""
            print all_dir
            print ""
            print self.check_killmove_dir(all_dir[len(all_dir) - 1], y, x)
            print (all_dir[len(all_dir)-1], last_y, last_x)
            counter = 0
            while True:
                counter += 1
                m, n, o = self.check_killmove(counter)
                if self.check_killmove_dir(m, n, o) != (0, 0, 0) and self.check_killmove_dir(m, n, o) != (all_dir[len(all_dir)-1], last_y, last_x):
                    print "drin"
                    self.play_killmove(m, n, o)
                    all_dir.append(m)
                    all_pos.append((n, o))
                    self.recursion(all_dir, all_pos)
                    break
                else:
                    print "nicht drin"
                    kill = True
                    break
        if self.check_killmove() != (0, 0, 0) and not self.check_win() == 1 and kill == False:
            aa, bb, cc = self.check_killmove()
            self.play_killmove(aa, bb, cc)
            print "1."
            all_dir.append(aa)
            all_pos.append((bb, cc))
            self.recursion(all_dir)
        if self.check_killmove() == (0, 0, 0) and not self.check_win() == 1 or kill == True:
            # NOTE: keine zuege mehr
            print ""
            print "2."
            print ""
            y_old, x_old = all_pos[len(all_pos) - 1]
            print y_old+1
            print x_old+1
            self.remove_killmove(all_dir[len(all_dir) - 1], y_old, x_old)
            all_pos.pop()
            all_dir.pop()
            self.recursion(all_dir, all_pos, 1)
        if self.check_killmove() == 0 and self.check_win():
            # NOTE: win
            exit()

    def kys(self):
        pass
