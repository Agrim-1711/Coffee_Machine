from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from replit import clear

cm = CoffeeMaker()
mm = MoneyMachine()
m = Menu()

is_on = True

while is_on:
  order = input(f"What would you like? ({m.get_items()}): ")
  
  if order == 'off':
    is_on = False
    clear()
  
  elif order == 'report':
    print(cm.report(),mm.report())

  elif order == 'top-up':
    cm.top_up()    
  
  else:
    m.find_drink(order)
    drink = m.find_drink(order)
    if cm.is_resource_sufficient(drink):
      cost = drink.cost
      mm.make_payment(cost)
      cm.make_coffee(drink)