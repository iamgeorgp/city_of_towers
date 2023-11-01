import random
import networkx as nx
import matplotlib.pyplot as plt

# random.seed(42)
class CityGrid:
    def __init__(self, N, M, obstructed_percentage=30):
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
        self.radius = R
        # Добавляем вершины
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
        print(towers)
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
        plt.plot([], [], label='Availible fild', marker='o', color=(0.2, 0.9, 0.2), markersize=10, linestyle='None')
        nx.draw_networkx_nodes(self.graph, pos, node_size=1000, node_color=node_colors)
        nx.draw_networkx_edges(self.graph, pos)
        nx.draw_networkx_labels(self.graph, pos)

        # Рисуем квадраты сетки
        size=max(self.N, self.M)
        for x in range(size):
            for y in range(size):
                square = plt.Rectangle((x-0.5, -y-0.5), 1, 1, fill=False, color='gray', linewidth=0.5)
                plt.gca().add_patch(square)
        plt.title(f'{self.N}x{self.M} Towers with Radius={self.radius}')
        plt.legend( loc='best')
        plt.show()