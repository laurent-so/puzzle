import pygame
import random

pygame.init()

FPS = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 600
TILE_SIZE = SCREEN_WIDTH // 3
BOARD_SIZE = 3
NUM_TILES = BOARD_SIZE ** 2 - 1
BG_COLOR, TEXT_COLOR = (255, 255, 255), (0, 0, 0)
FONT_SIZE, FONT_NAME = 50, pygame.font.match_font('arial')

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Slide Puzzle')
bg_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
bg_image.fill(BG_COLOR)

def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(FONT_NAME, size)
    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)

def draw_board(board):
    for row, col in ((row, col) for row in range(BOARD_SIZE) for col in range(BOARD_SIZE)):
        tile = board[row][col]
        if tile != None:
            x, y = col * TILE_SIZE, row * TILE_SIZE
            pygame.draw.rect(screen, BG_COLOR, (x, y, TILE_SIZE, TILE_SIZE))
            draw_text(screen, str(tile), FONT_SIZE, x + TILE_SIZE // 2, y + TILE_SIZE // 2)

def get_blank_position(board):
    for row, col in ((row, col) for row in range(BOARD_SIZE) for col in range(BOARD_SIZE)):
        if board[row][col] == None:
            return row, col

def is_legal_move(board, row, col):
    blank_row, blank_col = get_blank_position(board)
    return (row == blank_row and abs(col - blank_col) == 1) or (col == blank_col and abs(row - blank_row) == 1)

def get_random_move(board):
    blank_row, blank_col = get_blank_position(board)
    move_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    random.shuffle(move_offsets)
    for row_offset, col_offset in move_offsets:
        row, col = blank_row + row_offset, blank_col + col_offset
        if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and is_legal_move(board, row, col):
            return row, col
    return None, None

def do_move(board, row, col):
    blank_row, blank_col = get_blank_position(board)
    board[blank_row][blank_col], board[row][col] = board[row][col], None

def is_solved(board):
    return all(board[row][col] == row * BOARD_SIZE + col + 1 for row, col in ((row, col) for row in range(BOARD_SIZE) for col in range(BOARD_SIZE) if not (row == BOARD_SIZE - 1 and col == BOARD_SIZE - 1)))

# code non achevé

       
