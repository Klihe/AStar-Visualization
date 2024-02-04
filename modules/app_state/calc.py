# explore.py

from modules.config import Config
from modules.color import Color

def calc(curr_node: tuple[int], end_point: tuple[int], all_nodes: list) -> None:
    save_nodes: list = []
    end: bool = False

    while not end:
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbor_x = curr_node.x + i
                neighbor_y = curr_node.y + j

                if 0 <= neighbor_x < Config.COLUMNS and 0 <= neighbor_y < Config.ROWS:
                    neighbor_node = all_nodes[neighbor_x, neighbor_y]

                    if neighbor_node.point == end_point:
                        end = True

                    elif neighbor_node.color == Color.WHITE:
                        neighbor_node.color = Color.GREEN
                        neighbor_node.update_values(curr_node.point, curr_node.g)
                        save_nodes.append(neighbor_node)

                    elif neighbor_node.color == Color.GREEN and curr_node.g <= neighbor_node.g - 10:
                        neighbor_node.update_values(curr_node.point, curr_node.g)

        if not end:
            save_nodes = sorted(save_nodes, key=lambda x: x.f)
            save_nodes[0].color = Color.RED
            curr_node = save_nodes[0]
            save_nodes.pop(0)
