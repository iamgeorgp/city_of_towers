import random

class CityGrid:
    def __init__(self, n, m, obstructed_percentage=30):
        self.n = n
        self.m = m
        self.grid = [[0 for _ in range(m)] for _ in range(n)]
        
        # Initialize obstructed blocks randomly
        for i in range(n):
            for j in range(m):
                if random.randint(1, 100) <= obstructed_percentage:
                    self.grid[i][j] = 1