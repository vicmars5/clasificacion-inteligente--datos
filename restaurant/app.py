class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("name: ", self.restaurant_name)
        print("cuisine: ", self.cuisine_type)

    def open_restaurant(self):
        print("Restaurant is open")

restaurant1 = Restaurant("Sanborns", "Cafe")
restaurant2 = Restaurant("Starbucks", "Cafe")
restaurant3 = Restaurant("Wings Army", "Bar")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

