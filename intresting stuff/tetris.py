"""
Simple Tetris in Python using pygame
Save as tetris.py and run with: python tetris.py
Requires: pygame (pip install pygame)
"""

import pygame
import random
import sys

# ---------- Configuration ----------
CELL = 30
COLUMNS = 10
ROWS = 20
PLAY_WIDTH = CELL * COLUMNS
PLAY_HEIGHT = CELL * ROWS
SIDE_PANEL = 200
WIDTH = PLAY_WIDTH + SIDE_PANEL
HEIGHT = PLAY_HEIGHT
FPS = 60

# Colors
BLACK = (0, 0, 0)
GRAY = (40, 40, 40)
WHITE = (255, 255, 255)
LIGHT = (200, 200, 200)
COLORS = [
    (0, 240, 240),   # I - cyan
    (0, 0, 240),     # J - blue
    (240, 160, 0),   # L - orange
    (240, 240, 0),   # O - yellow
    (0, 240, 0),     # S - green
    (160, 0, 240),   # T - purple
    (240, 0, 0),     # Z - red
]

# ---------- Tetromino shapes ----------
# Each shape is a list of rotations, each rotation is a grid of strings.
SHAPES = {
    'I': [
        ["0000",
         "1111",
         "0000",
         "0000"],
        ["0010",
         "0010",
         "0010",
         "0010"],
    ],
    'J': [
        ["100",
         "111",
         "000"],
        ["011",
         "010",
         "010"],
        ["000",
         "111",
         "001"],
        ["010",
         "010",
         "110"],
    ],
    'L': [
        ["001",
         "111",
         "000"],
        ["010",
         "010",
         "011"],
        ["000",
         "111",
         "100"],
        ["110",
         "010",
         "010"],
    ],
    'O': [
        ["11",
         "11"],
    ],
    'S': [
        ["011",
         "110",
         "000"],
        ["010",
         "011",
         "001"],
    ],
    'T': [
        ["010",
         "111",
         "000"],
        ["010",
         "011",
         "010"],
        ["000",
         "111",
         "010"],
        ["010",
         "110",
         "010"],
    ],
    'Z': [
        ["110",
         "011",
         "000"],
        ["001",
         "011",
         "010"],
    ],
}

SHAPE_KEYS = list(SHAPES.keys())

# Map shape key to color index
SHAPE_TO_COLOR = {k: i for i, k in enumerate(SHAPE_KEYS)}

# ---------- Helper functions ----------


def rotate_shape(shape_rotations, rotation_index):
    return shape_rotations[rotation_index % len(shape_rotations)]


def shape_to_cells(shape_grid):
    """Convert shape grid (list of strings) to list of (r, c) coords where '1' exists."""
    cells = []
    for r, row in enumerate(shape_grid):
        for c, ch in enumerate(row):
            if ch == '1':
                cells.append((r, c))
    return cells


def create_empty_board(rows, cols):
    return [[None for _ in range(cols)] for _ in range(rows)]

# ---------- Game classes ----------


class Piece:
    def __init__(self, key):
        self.key = key
        self.rotations = SHAPES[key]
        self.rotation = 0
        self.color_index = SHAPE_TO_COLOR[key]
        # spawn near top center
        self.grid = rotate_shape(self.rotations, self.rotation)
        self.cells = shape_to_cells(self.grid)
        self.row = - (len(self.grid))  # start slightly above visible top
        self.col = (COLUMNS // 2) - (len(self.grid[0]) // 2)

    def rotate(self, cw=True):
        self.rotation = (self.rotation + (1 if cw else -1)
                         ) % len(self.rotations)
        self.grid = rotate_shape(self.rotations, self.rotation)
        self.cells = shape_to_cells(self.grid)

    def get_cell_positions(self, offset_r=0, offset_c=0):
        """Return list of (r, c) for this piece's current position (with offsets)."""
        return [(self.row + r + offset_r, self.col + c + offset_c) for (r, c) in self.cells]


class Tetris:
    def __init__(self):
        self.board = create_empty_board(ROWS, COLUMNS)
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.drop_interval = 1000  # ms between automatic drops; decrease with levels
        self.current = self._next_piece()
        self.hold_piece = None
        self.hold_locked = False
        self.next_queue = [self._next_piece() for _ in range(3)]
        self.game_over = False
        self.paused = False
        self.last_drop_time = pygame.time.get_ticks()

    def _next_piece(self):
        key = random.choice(SHAPE_KEYS)
        return Piece(key)

    def spawn_piece(self):
        self.current = self.next_queue.pop(0)
        self.next_queue.append(self._next_piece())
        self.hold_locked = False
        # If spawn collides -> game over
        if not self.valid_position(self.current, 0, 0):
            self.game_over = True

    def valid_position(self, piece, dr=0, dc=0):
        for r, c in piece.get_cell_positions(dr, dc):
            if r < 0:
                continue  # cells above top are allowed initially
            if r >= ROWS or c < 0 or c >= COLUMNS:
                return False
            if self.board[r][c] is not None:
                return False
        return True

    def lock_piece(self):
        for r, c in self.current.get_cell_positions():
            if 0 <= r < ROWS and 0 <= c < COLUMNS:
                self.board[r][c] = self.current.color_index
        cleared = self.clear_lines()
        self.update_score(cleared)
        self.spawn_piece()

    def clear_lines(self):
        new_board = []
        cleared = 0
        for row in self.board:
            if all(cell is not None for cell in row):
                cleared += 1
            else:
                new_board.append(row)
        while len(new_board) < ROWS:
            new_board.insert(0, [None for _ in range(COLUMNS)])
        self.board = new_board
        self.lines_cleared += cleared
        # level up every 10 lines (simple)
        self.level = 1 + (self.lines_cleared // 10)
        # speed up
        self.drop_interval = max(100, 1000 - (self.level - 1) * 80)
        return cleared

    def update_score(self, lines):
        # Classic scoring: 0, 40, 100, 300, 1200 times level (Tetris)
        if lines == 0:
            return
        points_map = {1: 40, 2: 100, 3: 300, 4: 1200}
        self.score += points_map.get(lines, 0) * self.level

    def hold(self):
        if self.hold_locked:
            return
        if self.hold_piece is None:
            self.hold_piece = Piece(self.current.key)
            self.spawn_piece()
        else:
            # swap
            temp = self.hold_piece
            self.hold_piece = Piece(self.current.key)
            self.current = temp
            # reset current's spawn position
            self.current.row = -len(self.current.grid)
            self.current.col = (COLUMNS // 2) - \
                (len(self.current.grid[0]) // 2)
            if not self.valid_position(self.current, 0, 0):
                self.game_over = True
        self.hold_locked = True

    def soft_drop(self):
        if self.valid_position(self.current, 1, 0):
            self.current.row += 1
        else:
            self.lock_piece()
            self.last_drop_time = pygame.time.get_ticks()

    def hard_drop(self):
        # drop until cannot
        while self.valid_position(self.current, 1, 0):
            self.current.row += 1
        self.lock_piece()
        self.last_drop_time = pygame.time.get_ticks()

    def tick(self):
        if self.game_over or self.paused:
            return
        now = pygame.time.get_ticks()
        if now - self.last_drop_time > self.drop_interval:
            self.last_drop_time = now
            if self.valid_position(self.current, 1, 0):
                self.current.row += 1
            else:
                self.lock_piece()

# ---------- Rendering ----------


def draw_grid(surface):
    for r in range(ROWS):
        for c in range(COLUMNS):
            rect = pygame.Rect(c*CELL, r*CELL, CELL, CELL)
            pygame.draw.rect(surface, GRAY, rect, 1)


def draw_board(surface, board):
    for r in range(ROWS):
        for c in range(COLUMNS):
            val = board[r][c]
            rect = pygame.Rect(c*CELL, r*CELL, CELL, CELL)
            if val is not None:
                color = COLORS[val]
                pygame.draw.rect(surface, color, rect.inflate(-2, -2))
            else:
                pygame.draw.rect(surface, BLACK, rect)


def draw_piece(surface, piece, ghost=False):
    for r, c in piece.get_cell_positions():
        if r < 0:
            continue
        if 0 <= r < ROWS and 0 <= c < COLUMNS:
            rect = pygame.Rect(c*CELL, r*CELL, CELL, CELL)
            color = COLORS[piece.color_index]
            if ghost:
                pygame.draw.rect(surface, color, rect.inflate(-2, -2), 1)
            else:
                pygame.draw.rect(surface, color, rect.inflate(-2, -2))


def draw_next(surface, pieces):
    font = pygame.font.SysFont(None, 24)
    x0 = PLAY_WIDTH + 20
    y0 = 30
    surface.blit(font.render("Next:", True, WHITE), (x0, y0))
    y0 += 30
    for i, p in enumerate(pieces):
        # draw a mini-representation
        mini_cell = CELL // 2
        for r, c in p.get_cell_positions(0, 0):
            # convert the piece's local cells to its rotation grid positions
            # easier approach: draw relative to p.grid
            pass
    # We'll draw them by rendering their grid strings for simplicity:
    x0 = PLAY_WIDTH + 20
    y0 = 60
    for i, p in enumerate(pieces):
        grid = rotate_shape(p.rotations, p.rotation)
        for r, row in enumerate(grid):
            for c, ch in enumerate(row):
                if ch == '1':
                    rect = pygame.Rect(
                        x0 + c * (CELL//1.6), y0 + r*(CELL//1.6) + i*80, int(CELL//1.6), int(CELL//1.6))
                    pygame.draw.rect(
                        surface, COLORS[p.color_index], rect.inflate(-1, -1))


def draw_hold(surface, piece):
    font = pygame.font.SysFont(None, 24)
    x0 = PLAY_WIDTH + 20
    y0 = PLAY_HEIGHT - 200
    surface.blit(font.render("Hold:", True, WHITE), (x0, y0))
    y0 += 30
    if piece:
        grid = rotate_shape(piece.rotations, piece.rotation)
        for r, row in enumerate(grid):
            for c, ch in enumerate(row):
                if ch == '1':
                    rect = pygame.Rect(
                        x0 + c*(CELL//1.6), y0 + r*(CELL//1.6), int(CELL//1.6), int(CELL//1.6))
                    pygame.draw.rect(
                        surface, COLORS[piece.color_index], rect.inflate(-1, -1))


def draw_ui(surface, game):
    font = pygame.font.SysFont(None, 28)
    x0 = PLAY_WIDTH + 20
    y0 = 10
    surface.blit(font.render(f"Score: {game.score}", True, WHITE), (x0, y0))
    surface.blit(font.render(
        f"Level: {game.level}", True, WHITE), (x0, y0 + 30))
    surface.blit(font.render(
        f"Lines: {game.lines_cleared}", True, WHITE), (x0, y0 + 60))

# ---------- Main loop ----------


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris - Python")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    game = Tetris()
    # start with a proper current piece
    game.current = game._next_piece()

    running = True
    while running:
        dt = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_p:
                    game.paused = not game.paused
                if game.game_over:
                    if event.key == pygame.K_RETURN:
                        game = Tetris()
                        game.current = game._next_piece()
                if not game.game_over and not game.paused:
                    if event.key == pygame.K_LEFT:
                        if game.valid_position(game.current, 0, -1):
                            game.current.col -= 1
                    elif event.key == pygame.K_RIGHT:
                        if game.valid_position(game.current, 0, 1):
                            game.current.col += 1
                    elif event.key == pygame.K_DOWN:
                        game.soft_drop()
                    elif event.key == pygame.K_SPACE:
                        game.hard_drop()
                    elif event.key == pygame.K_UP or event.key == pygame.K_x:
                        # rotate cw with wall kicks attempt
                        old_rot = game.current.rotation
                        game.current.rotate(True)
                        if not game.valid_position(game.current, 0, 0):
                            # try wall kicks: left or right
                            if game.valid_position(game.current, 0, -1):
                                game.current.col -= 1
                            elif game.valid_position(game.current, 0, 1):
                                game.current.col += 1
                            else:
                                game.current.rotation = old_rot
                                game.current.grid = rotate_shape(
                                    game.current.rotations, old_rot)
                                game.current.cells = shape_to_cells(
                                    game.current.grid)
                    elif event.key == pygame.K_z:
                        # rotate ccw
                        old_rot = game.current.rotation
                        game.current.rotate(False)
                        if not game.valid_position(game.current, 0, 0):
                            if game.valid_position(game.current, 0, -1):
                                game.current.col -= 1
                            elif game.valid_position(game.current, 0, 1):
                                game.current.col += 1
                            else:
                                game.current.rotation = old_rot
                                game.current.grid = rotate_shape(
                                    game.current.rotations, old_rot)
                                game.current.cells = shape_to_cells(
                                    game.current.grid)
                    elif event.key == pygame.K_c:
                        game.hold()

        # Automatic tick
        game.tick()

        # Render
        screen.fill(BLACK)
        # board area
        board_surface = pygame.Surface((PLAY_WIDTH, PLAY_HEIGHT))
        board_surface.fill(BLACK)
        draw_board(board_surface, game.board)
        draw_grid(board_surface)
        # ghost piece (optional)
        # compute ghost piece position
        ghost = Piece(game.current.key)
        ghost.rotation = game.current.rotation
        ghost.grid = rotate_shape(ghost.rotations, ghost.rotation)
        ghost.cells = shape_to_cells(ghost.grid)
        ghost.row = game.current.row
        ghost.col = game.current.col
        while game.valid_position(ghost, 1, 0):
            ghost.row += 1
        draw_piece(board_surface, ghost, ghost=True)

        draw_piece(board_surface, game.current)
        screen.blit(board_surface, (0, 0))

        # UI panel background
        panel_rect = pygame.Rect(PLAY_WIDTH, 0, SIDE_PANEL, HEIGHT)
        pygame.draw.rect(screen, (18, 18, 18), panel_rect)

        draw_ui(screen, game)
        draw_next(screen, game.next_queue)
        draw_hold(screen, game.hold_piece)

        if game.paused:
            txt = font.render("PAUSED", True, WHITE)
            screen.blit(txt, (PLAY_WIDTH//2 - txt.get_width() //
                        2, PLAY_HEIGHT//2 - txt.get_height()//2))
        if game.game_over:
            go = font.render("GAME OVER", True, WHITE)
            info = pygame.font.SysFont(None, 20).render(
                "Press Enter to restart", True, LIGHT)
            screen.blit(go, (PLAY_WIDTH//2 - go.get_width() //
                        2, PLAY_HEIGHT//2 - go.get_height()))
            screen.blit(
                info, (PLAY_WIDTH//2 - info.get_width()//2, PLAY_HEIGHT//2 + 10))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
