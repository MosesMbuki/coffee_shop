# Coffee Shop Domain Modeling Challenge

A Python implementation modeling a coffee shop domain using object-oriented programming principles.

## Project Structure
coffee_shop/
├── coffee.py
|__customer.py
|__order.py
|
├── tests/
│ ├── init.py # Makes tests a Python package
│ ├── test_customer.py # Customer class tests
│ ├── test_coffee.py # Coffee class tests
│ └── test_order.py # Order class tests
├── debug.py # Example usage and debugging
└── README.md # This file


## Domain Model Overview

### Key Classes

1. **Customer**
   - Represents coffee shop customers
   - Attributes: `name` (string, 1-15 chars)
   - Relationships: Places many Orders, has many Coffees through Orders

2. **Coffee**  
   - Represents coffee varieties
   - Attributes: `name` (string, min 3 chars)
   - Relationships: Has many Orders, has many Customers through Orders

3. **Order**
   - Represents customer purchases
   - Attributes: `price` (float, 1.0-10.0)
   - Relationships: Belongs to one Customer and one Coffee

### Key Methods

- `Customer.create_order(coffee, price)` - Creates new order
- `Coffee.average_price()` - Calculates average order price
- `Customer.most_aficionado(coffee)` - Finds top spender for a coffee
- `Coffee.num_orders()` - Counts total orders for a coffee

## Installation

1. Clone the repository:
   ```bash
   git clone 
   cd coffee_shop

## Validation Rules
    Customer.name: String between 1-15 characters

    Coffee.name: String with minimum 3 characters

    Order.price: Float between 1.0 and 10.0

### Technical Requirements
    Python 3.7+

    pytest (for testing)


## Key Design Decisions
1. Single Source of Truth:

    Each class maintains its own relationship lists

    Orders automatically update customer and coffee records

2. Input Validation:

    Property decorators enforce type and value constraints

    Raises ValueError for invalid inputs

3. Circular Import Solution:

    All domain classes combined in models.py

    Eliminates circular dependency issues

### Future Enhancements
    Add inventory tracking

    Implement loyalty program

    Add time tracking for orders

    Extend with beverage customization options

License
MIT License
Copyright 2025 Moses Mbuki Mutitu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.