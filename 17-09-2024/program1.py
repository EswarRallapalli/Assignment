"""CreateCreate a dictionary where the keys are tuples representing coordinates (x, y) and the values are city names.
 Write a Python program to print the city name for a given coordinate.
 Example Dictionary: #{(40.7128, -74.0060): "New York", (34.0522, -118.2437): "Los Angeles"} # Input: (40.7128, -74.0060) # Expected Output: "New York"
"""
city = {(40.7128, -74.0060): "New York",(34.0522, -118.2437): "Los Angeles",(41.8781, -87.6298): "Chicago"}
def get_city_name(coordinates):
    return city.get(coordinates, "City not found")
 
 
input_coordinates = (40.7128, -74.0060)
city_name = get_city_name(input_coordinates)
print(city_name)
