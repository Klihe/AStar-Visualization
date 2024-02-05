# explore.py

# imports of modules
from modules.config import Config
from modules.color import Color

# function calc is used to calculate the red_nodes
def calc(curr_node: tuple[int], end_point: tuple[int], all_nodes: list) -> None:
    # list to store the nodes
    save_nodes: list = []

    # boolean variable to check if the end point is reached
    end: bool = False

    while not end:
        # 3x3 grid around the current node
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbor_x = curr_node.x + i
                neighbor_y = curr_node.y + j

                # check if the neighbor is within the window
                if 0 <= neighbor_x < Config.COLUMNS and 0 <= neighbor_y < Config.ROWS:
                    neighbor_node = all_nodes[neighbor_x, neighbor_y]

                    if neighbor_node.point == end_point:
                        end = True
                    
                    # make the neighbor node green if it is white
                    elif neighbor_node.color == Color.WHITE:
                        neighbor_node.color = Color.GREEN
                        neighbor_node.update_values(curr_node.point, curr_node.g)
                        save_nodes.append(neighbor_node)

                    # update the values of the neighbor node if it is green
                    elif neighbor_node.color == Color.GREEN and curr_node.g <= neighbor_node.g - 10:
                        neighbor_node.update_values(curr_node.point, curr_node.g)

        if not end:
            # sort the nodes based on the final distance
            save_nodes = sorted(save_nodes, key=lambda x: x.f)

            # make the node red
            if len(save_nodes) > 0:
                save_nodes[0].color = Color.RED
                
                # set the current node to the node with the smallest distance
                curr_node = save_nodes[0]
                save_nodes.pop(0)

            # end if the end point can't reached
            else:
                end = True
