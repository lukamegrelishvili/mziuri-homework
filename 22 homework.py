class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Person(name={self.name}, deposit={self.deposit}, loan={self.loan})"

    def buy_house(self, house):
        if house.status == 'available' and self.deposit >= house.price:
            self.deposit -= house.price
            house.owner = self
            house.status = 'sold'
        elif house.status != 'available':
            print("House is not available.")
        else:
            print("Not enough deposit to buy the house.")

    def take_loan(self, amount):
        self.loan += amount
        self.deposit += amount


class House:
    def __init__(self, house_id, price):
        self.ID = house_id
        self.price = price
        self.owner = None
        self.status = 'available'

    def __str__(self):
        owner_name = self.owner.name if self.owner else "No owner"
        return f"House(ID={self.ID}, price={self.price}, owner={owner_name}, status={self.status})"


person1 = Person("Alice")
house1 = House(1, 900)

print(person1)
print(house1)

person1.buy_house(house1)

print(person1)
print(house1)
