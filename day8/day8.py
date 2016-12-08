
class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [ [ False for y in range(height) ] for x in range(width) ]

    def rect(self, w, h):
        for x in range(w):
            for y in range(h):
                self.pixels[x][y] = True

    def rotate_row(self, rownum, repeat):
        for r in range(repeat):
            tmp = self.pixels[-1][rownum]
            for i in range(self.width - 2, -1, -1):
                self.pixels[i+1][rownum] = self.pixels[i][rownum]
            self.pixels[0][rownum] = tmp

    def rotate_col(self, colnum, repeat):
        for r in range(repeat):
            tmp = self.pixels[colnum][-1]
            for i in range(self.height - 2, -1 , -1):
                self.pixels[colnum][i+1] = self.pixels[colnum][i]
            self.pixels[colnum][0] = tmp

    def show(self):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if self.pixels[x][y]: row += "x"
                else: row += " "
            print row

    def count(self):
        c = 0
        for x in range(self.width):
            for y in range(self.height):
                if self.pixels[x][y]:
                    c+=1

        return c
    
def execute_cmd(screen, cmd):
    parts = cmd.split(" ")

    if parts[0] == "rect":
        coords = parts[1].split("x")
        screen.rect(int(coords[0]), int(coords[1]))
    else:
        if parts[0] == "rotate":
            if parts[1] == "column":
                screen.rotate_col(int(parts[2][2:]), int(parts[4]))
            else:
                if parts[1] == "row":
                    screen.rotate_row(int(parts[2][2:]), int(parts[4]))

def test():
    s = Screen(50, 6)
    s.show()

    execute_cmd(s, "rect 2x3")
    s.show()

    execute_cmd(s, "rotate column y=0 2")
    s.show()

    execute_cmd(s, "rotate row x=0 1")
    s.show()

def main():
    s = Screen(50, 6)
    for l in open('input').readlines():
        execute_cmd(s, l.strip())

    print s.count()
    s.show()

main()
