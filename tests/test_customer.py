import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def test_customer_initialization(self):
        customer = Customer("Alice")
        assert customer.name == "Alice"

    def test_name_validation(self):
        with pytest.raises(ValueError):
            Customer("")  # Too short
        with pytest.raises(ValueError):
            Customer("A" * 16)  # Too long
        with pytest.raises(ValueError):
            Customer(123)  # Not a string

    def test_create_order(self):
        customer = Customer("Bob")
        coffee = Coffee("Latte")
        order = customer.create_order(coffee, 5.0)
        assert order in customer.orders()
        assert order in coffee.orders()
        assert order.price == 5.0

    def test_coffees_method(self):
        customer = Customer("Charlie")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Espresso")
        Order(customer, coffee1, 4.0)
        Order(customer, coffee1, 4.5)  # Same coffee, different order
        Order(customer, coffee2, 3.5)
        
        assert len(customer.coffees()) == 2  # Should be unique

    def test_most_aficionado(self):
        coffee = Coffee("Cappuccino")
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        
        Order(customer1, coffee, 4.0)
        Order(customer1, coffee, 5.0)
        Order(customer2, coffee, 3.0)
        
        assert Customer.most_aficionado(coffee) == customer1