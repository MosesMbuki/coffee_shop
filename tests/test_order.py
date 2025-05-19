import pytest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder:
    def test_order_initialization(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 4.5)
        
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 4.5

    def test_price_validation(self):
        customer = Customer("Bob")
        coffee = Coffee("Espresso")
        
        with pytest.raises(ValueError):
            Order(customer, coffee, 0.9)  # Too low
        with pytest.raises(ValueError):
            Order(customer, coffee, 10.1)  # Too high
        with pytest.raises(ValueError):
            Order(customer, coffee, "5")  # Not a float

    def test_customer_property(self):
        customer = Customer("Charlie")
        coffee = Coffee("Mocha")
        order = Order(customer, coffee, 5.0)
        
        with pytest.raises(ValueError):
            order.customer = "Not a customer"

    def test_coffee_property(self):
        customer = Customer("Dave")
        coffee = Coffee("Flat White")
        order = Order(customer, coffee, 4.0)
        
        with pytest.raises(ValueError):
            order.coffee = "Not a coffee"