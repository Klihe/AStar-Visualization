# explore.py

from modules.config import Config
from modules.color import Color

def result(curr_node, end_point, all_nodes) -> None:
    save_nodes = []
    end = False

    while not end:
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbor_x = curr_node.x + i
                neighbor_y = curr_node.y + j

                if 0 <= neighbor_x < Config.COLUMNS and 0 <= neighbor_y < Config.ROWS:
                    neighbor_node = all_nodes[neighbor_x, neighbor_y]

                    if neighbor_node.point == end_point:
                        end = True

                    elif neighbor_node.color == Color.RED:
                        save_nodes.append(neighbor_node)

        if not end:
            save_nodes = sorted(save_nodes, key=lambda x: x.g)
            save_nodes[0].color = Color.BLUE
            curr_node = save_nodes[0]
            save_nodes.pop(0)
