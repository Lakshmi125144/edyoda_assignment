import random
class FoodItem: 
    def __init__(self, food_id, name, quantity, price, discount, stock): 
        self.food_id = food_id 
        self.name = name 
        self.quantity = quantity 
        self.price = price 
        self.discount = discount 
        self.stock = stock 
    def get_price(self):
        return self.price * (1 - self.discount)
    def is_in_stock(self):
        return self.stock > 0
class User: 
    def __init__(self, full_name, phone_number, email, address, password): 
        self.full_name = full_name 
        self.phone_number = phone_number 
        self.email = email 
        self.address = address 
        self.password = password 
        self.orders = []
    def place_order(self, food_items): 
        order = Order(self, food_items)
        self.orders.append(order)
        return order 
        
class Admin: 
    def __init__(self, username, password): 
        self.username = username 
        self.password = password 
    def add_food_item(self, food_item): 
        app.food_items.append(food_item)
        pass 
    def edit_food_item(self, food_id, food_item): 
        for i in range(len(app.food_items)):
            if app.food_items[i].food_id == food_id:
                app.food_items[i] == food_item 
                break   
        
    def view_food_items(self): 
        return app.food_items
         
    def remove_food_item(self, food_id): 
       for i in range(len(app.food_items)):
            if app.food_items[i].food_id == food_id:
                app.food_items[i] == food_item 
                break   
class FoodOrderingApp: 
    def __init__(self): 
        self.users = [] 
        self.food_items = [] 
        self.admins = [] 
    def register_user(self, user): 
        self.users.append(user) 
    def login_user(self, username, password): 
        for user in self.users: 
            if user.username == username and user.password == password: 
                return user 
            return None 
    def login_admin(self, username, password): 
        for admin in self.admins: 
            if admin.username == username and admin.password == password: 
                return admin 
            return None 
    def get_food_items(self): 
        return self.food_items 
    def place_order(self, user, food_items): 
        user.place_order(food_items) 
if __name__ == '__main__': 
    app = FoodOrderingApp() 
    
