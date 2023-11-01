import networkx as nx

def path_between_towers(city, towers):
    '''
    Finds the shortest path between towers in the city, taking into account the range of towers.

    Parameters:
        city (CityGrid): Object representing the city.
        towers (list): A list of tower coordinates in the format [(x1, y1), (x2, y2), ...].

    Returns:
        list: A list of edges representing the shortest path.
              Each edge is represented as a pair ((x1, y1), (x2, y2)).
              Returns None if no path is found.
    '''
    if len(towers) != 1:
        G_towers = nx.Graph()
        for i in range (len(towers)-1):
            x1, y1 = towers[i]
            for j in range(i+1, len(towers)):
                x2, y2 = towers[j]
                if abs(x1-x2)<=2*city.radius and abs(y1-y2)<=2*city.radius:
                    G_towers.add_edge((x1,y1),(x2,y2))
        user_input = input('source vertex (x, y): ')
        x, y = map(int, user_input.strip('()').split(','))
        first = (x, y)
        user_input = input('target vertex (x, y): ')
        x, y = map(int, user_input.strip('()').split(','))
        second = (x, y)
        try:
            path = nx.shortest_path(G_towers, source=first, target=second, weight='weight')
            path_edges=[]
            for i in range(len(path)-1):
                path_edges.append((path[i],path[i+1]))
            return path_edges
        except nx.NetworkXNoPath:
            print("No path")
    return None
