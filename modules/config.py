# config.py

class Config:
    COLUMNS = 15
    ROWS = 10

    GRID_THICKNESS = 2

    RECT_SIZE = 100

    WINDOW_WIDTH = COLUMNS * RECT_SIZE
    WINDOW_HEIGHT = ROWS * RECT_SIZE

    START_POINT = (0,0)
    END_POINT = (14,9)
    BARRIERS_POS = [(2,1),(2,2),(2,3),(3,2),(3,3)]