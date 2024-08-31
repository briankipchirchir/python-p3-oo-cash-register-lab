#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        """
        Initialize the CashRegister class.
        :param discount: The discount percentage to be applied to the total (default is 0).
        """
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        """
        Add an item to the cash register.
        :param title: The name of the item.
        :param price: The price of the item.
        :param quantity: The quantity of the item (default is 1).
        """
        self.last_transaction_amount = price * quantity
        self.total += self.last_transaction_amount
        
        # Store each item with quantity in the items list
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        """
        Apply the discount to the total and return the discounted total.
        """
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}."
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        """
        Void the last transaction, removing its amount from the total.
        """
        self.total -= self.last_transaction_amount
        self.last_transaction_amount = 0

