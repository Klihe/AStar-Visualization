# config.py

class Config:
    COLUMNS: int = 11
    ROWS: int = 6

    GRID_THICKNESS: int = 2

    NODE_SIZE: int = 100

    WINDOW_WIDTH: int = COLUMNS * NODE_SIZE
    WINDOW_HEIGHT: int = ROWS * NODE_SIZE