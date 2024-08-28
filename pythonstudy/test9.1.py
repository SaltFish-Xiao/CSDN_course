class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Basic information: restaurant name is %s and cuisine type is %s" %(self.restaurant_name,self.cuisine_type))

    def open_restaurant(self):
        print("%s is openning now!" %self.restaurant_name)

new_restaurant = Restaurant("xiangyun","chinese")
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
