# get_plan

from modules.config import Config
from modules.color import Color

def get_plan(all_nodes: list) -> list[int]:
    nodes_barriers: list = []
    node_start: tuple[int] = None
    node_end: tuple[int] = None

    for i in range(Config.COLUMNS):
            for j in range(Config.ROWS):
                if all_nodes[i, j].color == Color.BLACK:
                    nodes_barriers.append(all_nodes[i][j].point)
                if all_nodes[i, j].color == Color.YELLOW:
                    node_start = all_nodes[i][j].point
                if all_nodes[i][j].color == Color.BLUE:
                    node_end = all_nodes[i][j].point
                
    return nodes_barriers, node_start, node_end
