import time
class Employee:
    """A class that simulates an employee working in a restaurant"""

    def __init__(self,name,salary):
        self._name = name
        self._salary = salary

    def give_raise(self,percent):
        if 0.0 <= percent <= 10.0:
            return percent * self._salary + self._salary
        return "percent too low or too high"

    def __str__(self):
        return f"<{self._name} {self._salary}>"

    def __repr__(self):
        return f"<Employee: {self._name} {self._salary}>"

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary


class Chef(Employee):
    """A sub class of Employee which cooks food
    
    attr: 
         name: name of chef
         
         salary: base salary
         
         food: food chef makes"""

    def __init__(self, name, salary):
        super().__init__(name, salary)

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return f"<Chef: {self._name} {self._salary}>"

    def make_food(self,food):
        """makes food for customer in ten seconds"""
        print(f"{self._name} is making {food}...")
        time.sleep(10)
        print(f"{food} done and ready to serve")


class Server(Employee):
    """A sub class of Employee that takes order from customer"""

    def __init__(self, name, salary):
        super().__init__(name, salary)

    def take_order(self,customer,food):
        """takes the order from customer and send to chef to make"""
        print(f"{self._name} has taken order from {customer} and sending to chef")
        time.sleep(5)

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return f"<Server : {self._name} {self._salary}>"


class Customer:

    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name

    def place_order(self,food):
        """places order for food from server"""
        print(f"{self.name} is thinking...")
        time.sleep(10)
        print(f"{self.name} has ordered for {food}")

    def __repr__(self):
        return f"<Customer {self.name}>"


class Food:

    def __init__(self,food_name):
        self._food_name = food_name

    def __str__(self):
        return f"{self._food_name}"


class Restaurant:
    """A container and controller class that simulates a restaurant where a customer
    places order for a certain food and server serves food
    
    attr: 
    
    chef: the chef in the restaurant
    
    waiter: the server that takes order and deliver food
    
    customer: the customer that cmes to the restaurant to eat"""

    def __init__(self,name):
        self._name = name
        self.chef = Chef("John Doe",40000)
        self.waiter = Server("Bob Sue",25000)

    def order(self,food,customer):
        """simulates an ordering scenario where a customer orders for a food and a waiter takes the 
        order and sends to the chef.
        
        args: 
        
        food: a food object
        
        customer: A customer object"""
        if isinstance(customer,Customer):
            customer.place_order(food)
            self.waiter.take_order(customer.name,food)
            self.chef.make_food(food)

    def __str__(self):
        return "*" * len(self._name) + "\n" + self._name +  "\n" + "*" * len(self._name)


if __name__ == "__main__":
    cafe = Restaurant("Pizza Deluxé")
    rob = Customer("Rob")
    print(cafe)
    cafe.order("pizza",rob)         