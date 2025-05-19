import pytest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee:
    def test_coffee_initialization(self):
        coffee = Coffee("Latte")
        assert coffee.name == "Latte"

    def test_name_validation(self):
        with pytest.raises(ValueError):
            Coffee("A")  # Too short
        with pytest.raises(ValueError):
            Coffee(123)  # Not a string

    def test_orders_method(self):
        coffee = Coffee("Espresso")
        customer = Customer("Alice")
        order1 = Order(customer, coffee, 3.5)
        order2 = Order(customer, coffee, 4.0)
        
        assert len(coffee.orders()) == 2
        assert order1 in coffee.orders()
        assert order2 in coffee.orders()

    def test_customers_method(self):
        coffee = Coffee("Latte")
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        
        Order(customer1, coffee, 4.0)
        Order(customer1, coffee, 4.5)  # Same customer, different order
        Order(customer2, coffee, 3.5)
        
        assert len(coffee.customers()) == 2  # Should be unique

    def test_num_orders(self):
        coffee = Coffee("Cappuccino")
        customer = Customer("Charlie")
        
        assert coffee.num_orders() == 0
        Order(customer, coffee, 5.0)
        assert coffee.num_orders() == 1

    def test_average_price(self):
        coffee = Coffee("Americano")
        customer = Customer("Dave")
        
        Order(customer, coffee, 2.0)
        Order(customer, coffee, 4.0)
        assert coffee.average_price() == 3.0