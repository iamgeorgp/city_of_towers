import random
import networkx as nx
import matplotlib.pyplot as plt
# random.seed(42)

class CityGrid:
    """
    The class represents a city grid with towers and blocks.
    
    Attributes:
        N (int): The number of rows in the grid.
        M (int): The number of columns in the grid.
        radius (int): The radius of the towers.
        grid (list): A two-dimensional array representing a grid of blocks.
        graph (NetworkX Graph): A graph to represent the links between towers and blocks.
        obstructed_percentage (int): Percentage of blocks that are obstructed.

    Methods:
        __init__(self, N, M, obstructed_percentage=30): Initialization of the CityGrid object.
        init_graph(self, R): Initialization of the graph taking into account the radius of towers.
        visualize_graph(self, towers=None): Visualize city grid and links between towers.

    """

    def __init__(self, N, M, obstructed_percentage=30):
        """
        Initialization of CityGrid object.

        Parameters:
            N (int): The number of rows in the grid.
            M (int): The number of columns in the grid.
            obstructed_percentage (int): Percentage of blocks with obstructed percentage (default is 30).
        """

        self.N = N
        self.M = M
        self.radius = 0
        self.grid = [[0 for _ in range(M)] for _ in range(N)]
        self.graph = nx.Graph()
        self.obstructed_percentage = obstructed_percentage

        for i in range(N):
            for j in range(M):
                if random.randint(1, 100) <= obstructed_percentage:
                    self.grid[i][j] = 1
    def init_graph(self, R):
        """
        Initialization of the graph taking into account the radius of towers.

        Parameters:
            R (int): The radius of the towers.
        """

        self.radius = R
        for i in range(self.N):
            for j in range(self.M):
                if self.grid[i][j] == 0:
                    self.graph.add_node((i, j))
        for i in range(self.N):
            for j in range(self.M):
                if self.grid[i][j] == 0:
                    for dx in range(-R, R + 1):
                        for dy in range(-R, R + 1):
                            if (dx != 0 or dy != 0) and 0 <= i + dx < self.N and 0 <= j + dy < self.M and self.grid[i + dx][j + dy] == 0:
                                self.graph.add_edge((i, j), (i + dx, j + dy))
    def vizualize_graph(self, towers=None):
        """
        Visualization of the city grid and links between towers.

        Parameters:
            towers (list): List of tower coordinates in the format [(x1, y1), (x2, y2), ...]. (default None).
        """
        
        plt.figure(figsize=(self.N, self.M))
        pos = {(i, j): (j, -i) for i in range(self.N) for j in range(self.M)}
        node_colors=[]
        for i in range(self.N):
            for j in range(self.M):
                if (i,j) in self.graph.nodes:
                    if towers != None and (i,j) in towers:
                        node_colors.append((0.9, 0.2, 0.2))
                    else:
                        node_colors.append((0.2, 0.9, 0.2))

        # nx.draw(self.graph, pos, with_labels=True, node_size=1000, font_size=8, node_color=node_colors, font_color='black', node_shape='s') 
        plt.plot([], [], label='Tower', marker='o', color=(0.9, 0.2, 0.2), markersize=10, linestyle='None')
        plt.plot([], [], label='Availible field', marker='o', color=(0.2, 0.9, 0.2), markersize=10, linestyle='None')
        nx.draw_networkx_nodes(self.graph, pos, node_size=1000, node_color=node_colors)
        nx.draw_networkx_edges(self.graph, pos)
        nx.draw_networkx_labels(self.graph, pos)

        size=max(self.N, self.M)
        for x in range(size):
            for y in range(size):
                square = plt.Rectangle((x-0.5, -y-0.5), 1, 1, fill=False, color='gray', linewidth=0.5)
                plt.gca().add_patch(square)
        plt.title(f'{self.N}x{self.M} Towers with Radius={self.radius}')
        plt.legend( loc='best')
        plt.show()