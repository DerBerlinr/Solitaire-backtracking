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

    def check_killmove(self):
        for y in range(7):
            for x in range(7):
                if self.field[y][x] == 1:
                    # NOTE: horizontal rechts
                    if x <= 4:
                        if self.field[y][x + 2] == 0 and self.field[y][x + 1] == 1:
                            print "horizontal rechts moeglich fuer Feld: ", y + 1, x + 1
                            return 1, y, x
                    # NOTE: horizontal links
                    if x >= 2:
                        if self.field[y][x - 2] == 0 and self.field[y][x - 1] == 1:
                            print "horizontal links moeglich fuer Feld: ", y + 1, x + 1
                            return 2, y, x
                    # NOTE: vertikal
                    if y >= 2:
                        if self.field[y - 2][x] == 0 and self.field[y - 1][x] == 1:
                            print "vertikal oben moeglich fuer Feld: ", y + 1, x + 1
                            return 3, y, x
                    # NOTE: vertikal unten
                    if y <= 4:
                        if self.field[y + 2][x] == 0 and self.field[y + 1][x] == 1:
                            print "vertikal unten moeglich fuer Feld: ", y + 1, x + 1
                            return 4, y, x
        return 0, 0, 0

    def check_win(self):
        counter = 0
        for y in range(7):
            for x in range(7):
                if self.field[y][x] == 1:
                    counter += 1
        if counter == 1:
            return 1
        else:
            return 0

    def check_killmove_dir(self, direction, y, x):
        if not None:
            # NOTE: horizontal rechts
            if not x > 6 and direction == 1:
                if self.field[y][x + 2] == 0 and self.field[y][x + 1] == 1:
                    print "horizontal rechts moeglich fuer Feld: ", y, x
                    return 1
            # NOTE: horizontal links
            if not x < 2 and direction == 2:
                if self.field[y][x - 2] == 0 and self.field[y][x - 1] == 1:
                    print "horizontal links moeglich fuer Feld: ", y, x
                    return 2
            # NOTE: vertikal oben
            if not y < 2 and direction == 3:
                if self.field[y - 2][x] == 0 and self.field[y - 1][x] == 1:
                    print "vertikal oben moeglich fuer Feld: ", y, x
                    return 3
            # NOTE: vertikal unten
            if not y > 6 and direction == 4:
                if self.field[y + 2][x] == 0 and self.field[y + 1][x] == 1:
                    print "vertikal unten moeglich fuer Feld: ", y, x
                    return 4
        return 0

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
        if self.check_killmove() != (0, 0, 0) and not self.check_win() and next == 1:
            for i in range(1, 4):
                dir, y, x = self.check_killmove()
                if self.check_killmove_dir(all_dir[len(all_dir) - 1] + i, y, x):
                    self.play_killmove(dir, y, x)
                    all_dir.append(dir + i)
                    all_pos.append((y, x))
                    pass
            self.recursion(all_dir, all_pos)
        elif self.check_killmove() != (0, 0, 0) and not self.check_win() == 1:
            aa, bb, cc = self.check_killmove()
            self.play_killmove(aa, bb, cc)
            print "1."
            all_dir.append(aa)
            all_pos.append((bb, cc))
            self.recursion(all_dir)
        elif self.check_killmove() == (0, 0, 0) and not self.check_win() == 1:
            # NOTE: keine zuege mehr
            print ""
            print "2."
            print ""
            y_old, x_old = all_pos[len(all_pos) - 1]
            print y_old
            print x_old
            self.remove_killmove(all_dir[len(all_dir) - 1], y_old, x_old)
            all_dir.pop()
            all_pos.pop()
            self.recursion(all_dir, all_pos, 1)
        elif self.check_killmove() == 0 and self.check_win():
            # NOTE: win
            exit()

    def kys(self):
        pass
