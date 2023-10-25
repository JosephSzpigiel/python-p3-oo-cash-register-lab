#!/usr/bin/env python3
# import ipdb

class CashRegister:
  
  def __init__(self, discount = 0):
    self.total = 0
    self.items = []
    self.discount = discount
    self.last_transaction = 0

  def add_item(self, title, price, quantity=1):
    self.total += (price*quantity)
    self.last_transaction = (price*quantity)
    for num in range(quantity):
      self.items.append(title)

  def apply_discount(self):
    if self.discount == 0:
      print('There is no discount to apply.')
    else:
      self.total = self.total - (self.total*self.discount/100)
      print(f'After the discount, the total comes to ${int(self.total)}.')

  def void_last_transaction(self):
    self.total = self.total - self.last_transaction

# ipdb.set_trace()