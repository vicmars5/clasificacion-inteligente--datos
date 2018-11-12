class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("name: ", self.restaurant_name)
        print("cuisine: ", self.cuisine_type)

    def open_restaurant(self):
        print("Restaurant is open")

restaurant = Restaurant("Sanborns", "Cafe")

restaurant.describe_restaurant()
restaurant.open_restaurant()

