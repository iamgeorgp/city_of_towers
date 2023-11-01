import city_class
import func_dom_set
import func_path_finder

# Initialization of a city with specified parameters
city = city_class.CityGrid(5, 7, obstructed_percentage=65)
# Initialization of the graph of a city with towers with radius R
city.init_graph(R=1)
# Visualization of the city without towers
city.vizualize_graph()
# Finding the minimum number of towers and their location in the city
towers=func_dom_set.find_minimum_dom_sets(city.graph)
# Visualization of tower placement in the city
city.vizualize_graph(towers=towers)
# Finding the most stable path between given towers for data transmission
print('Shortest path: ', func_path_finder.path_between_towers(city, towers=towers))