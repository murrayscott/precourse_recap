# Coffee milk percentage calculator
units = "ml"
vessel_volume = input("Enter vessel Volume in " + units +": ")
milk_qty = input("Enter Milk Volume in " + units + ": ")

def calc_percentage (total, portion):
  return ((portion/total)*100)

result = calc_percentage (float(vessel_volume), float(milk_qty))
print ("Percentage of milk in your drink is " + str(result) + " %")