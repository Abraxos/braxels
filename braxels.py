BRAILLE_BLOCK_OFFSET = 10240
BRAILLE = [[1, 8], [2, 16], [4, 32], [64, 128]]

class Foreground:
    BLACK = '\033[30m'   # black
    RED = '\033[31m'     # red
    GREEN = '\033[32m'   # green
    YELLOW = '\033[33m'  # yellow
    BLUE = '\033[34m'    # blue
    MAGENTA = '\033[35m' # magenta
    CYAN = '\033[36m'    # cyan
    WHITE = '\033[37m'   # white
    RESET = '\033[39m'   # reset

class Background:
    BLACK = '\033[40m'   # black
    RED = '\033[41m'     # red
    GREEN = '\033[42m'   # green
    YELLOW = '\033[43m'  # yellow
    BLUE = '\033[44m'    # blue
    MAGENTA = '\033[45m' # magenta
    CYAN = '\033[46m'    # cyan
    WHITE = '\033[47m'   # white
    RESET = '\033[49m'   # reset

def array_to_braille(array):
    s = 0
    if array[0][0]:
        s |= BRAILLE[0][0]
    if array[0][1]:
        s |= BRAILLE[0][1]
    if array[1][0]:
        s |= BRAILLE[1][0]
    if array[1][1]:
        s |= BRAILLE[1][1]
    if array[2][0]:
        s |= BRAILLE[2][0]
    if array[2][1]:
        s |= BRAILLE[2][1]
    if array[3][0]:
        s |= BRAILLE[3][0]
    if array[3][1]:
        s |= BRAILLE[3][1]
    return chr(BRAILLE_BLOCK_OFFSET + s)

class Braxel(object):
    def __init__(self, pixels,
                 foreground=Foreground.RESET,
                 background=Background.RESET):
        self.foreground = foreground
        self.background = background
        if isinstance(pixels, list) or isinstance(pixels, tuple):
            assert len(pixels) == 4
            assert all(len(row) == 2 for row in pixels)
            self.character = array_to_braille(pixels)

    def to_string(self):
        return self.foreground + self.background + self.character

    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        return str(self) + str(other)

    
def braxel_matrix_to_string(matrix):
    string = []
    for row in matrix:
        string.append(''.join([str(b) for b in row]))
    return '\n'.join(row for row in string)


def pixmap_to_braxel_matrix(pixels):
    assert len(pixels) % 4 == 0, "Number of rows must be divisible by 4"
    assert len(pixels[0]) % 2 == 0, "Number of columns must be divisible by 2"
    braxel_matrix = []
    for r in range(0, len(pixels), 4):
        braxel_row = []
        for c in range(0, len(pixels[r]), 2):
            braxel_row.append(Braxel([pixels[r][c:c+2],
                                      pixels[r+1][c:c+2],
                                      pixels[r+2][c:c+2],
                                      pixels[r+3][c:c+2]]))
        braxel_matrix.append(braxel_row)
    return braxel_matrix


def pixmap_to_str(pixels):
    return braxel_matrix_to_string(pixmap_to_braxel_matrix(pixels))

        
if __name__ == '__main__':
    print(Braxel([[0,0],
                  [0,0],
                  [0,0],
                  [0,0]]))
    print(Braxel([[1,0],
                  [0,0],
                  [0,0],
                  [0,0]]))
    print(Braxel([[0,1],
                  [0,0],
                  [0,0],
                  [0,0]]))
    print(Braxel([[0,0],
                  [1,0],
                  [0,0],
                  [0,0]]))
    print(Braxel([[0,0],
                  [0,1],
                  [0,0],
                  [0,0]]))
    print(Braxel([[0,0],
                  [0,0],
                  [1,0],
                  [0,0]]))
    print(Braxel([[0,0],
                  [0,0],
                  [0,1],
                  [0,0]]))
    print(Braxel([[0,0],
                  [0,0],
                  [0,0],
                  [1,0]]))
    print(Braxel([[0,0],
                  [0,0],
                  [0,0],
                  [0,1]]))
    print(Braxel([[1,1], [1,1], [1,1], [1,1]]))
    print(Braxel([[1,1], [1,1], [1,1], [1,1]]))
    print(Braxel([[1,1], [1,1], [1,1], [1,1]], Foreground.RED) + Braxel([[1,1], [1,1], [1,1], [1,1]], background=Background.WHITE) + Background.RESET)
    print(pixmap_to_str([[1,1,1,1,1,1,1,1],
                         [1,0,1,1,1,1,1,1],
                         [1,0,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,0,1],
                         [1,1,1,1,1,1,0,1],
                         [1,1,1,1,1,1,1,1]]))
    print(pixmap_to_str([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
                         [0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
                         [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
                         [0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                         [0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                         [0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                         [0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                         [0,0,0,0,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0],
                         [0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,0],
                         [0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,1,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0],
                         [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
                         [0,0,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,0],
                         [0,0,0,0,0,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]))
    
