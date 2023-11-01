import city_class
import func_dom_set

city = city_class.CityGrid(5, 6, obstructed_percentage=55)
city.init_graph(R=1)
city.vizualize_graph()
city.vizualize_graph(towers=func_dom_set.find_minimum_dom_sets(city.graph))