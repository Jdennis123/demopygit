import random
soups = ['Onions', 'Potato','Chicken','Corn','Pumpkin', 'Bean', 'Pea']
salads = ['Veggie', 'Cabbage', 'Greek', 'Lettuce', 'Caesar', 'Tomato']
main = ['Crab cake', 'Salmon', 'Ribs', 'Chopped Liver', 'Meat Balls']
beverage = ['Wine', 'Rum', 'Irish cream', 'Red bull', 'Whiskey', 'Beer']

print('Welcome to cafe del Jamie, the menu for today is:')
print(f"Soups: {random.choice (soups)}")
print(f"Salads: {random.choice (salads)}")
print(f"Main: {random.choice (main)}")
print(f"Beverages: {random.choice (beverage)}")