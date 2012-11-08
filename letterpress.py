class Tile:
    def __init__(self, position, letter, color, locked):
        self.position = position
        self.letter = letter
        self.color = color
        self.locked = locked

class Game:
    def __init__(self, board_string, word_list):
        self.tiles = {} # Maps position to tile information.
        self.word_list = word_list

        # Parse the board string.
        y = 0
        for line in board_string.splitlines():
            line = line.strip()
            if line == '':
                continue
            for x, letter in enumerate(line):
                tile = Tile((x, y), letter, None, False)
                self.tiles[tile.position] = tile
            y += 1

    def play(self, color, positions):
        word = ''.join(self.tiles[p].letter for p in positions)

        # Check word legality.
        if word not in self.word_list:
            return False

        # Color the tiles making up the word.
        for p in positions:
            self.tiles[p].color = color

        self._update_locked(color)

        return True

    def score(self, color):
        result = 0
        for tile in self._tiles_colored(color):
            if tile.color == color:
                result += 1
        return result

    def locked(self, color):
        result = []
        for tile in self._tiles_colored(color):
            if tile.color == color and tile.locked == True:
                result.append(tile.position)
        return result

    def _tiles_colored(self, color):
        for tile in self.tiles.values():
            if tile.color == color:
                yield tile

    def _update_locked(self, color):
        # A tile is locked if all neighboring tiles have the same color.
        for tile in list(self._tiles_colored(color)):
            x, y = tile.position
            neighbor_positions = [
                (x + 1, y),
                (x - 1, y),
                (x, y + 1),
                (x, y - 1),
            ]
            neighbor_tiles = [self.tiles.get(np) for np in neighbor_positions]
            locked = all(nt.color == color for nt in neighbor_tiles if nt)
            self.tiles[tile.position].locked = locked
