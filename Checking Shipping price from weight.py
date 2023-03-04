weight= float(input("Enter the weight of yourn product(Lbs): "))

#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20.00
elif weight <= 6:
  cost_ground = weight * 3 + 20.00
elif weight <= 10:
  cost_ground = weight * 4 + 20.00
else:
  cost_ground = weight * 4.75 + 20.00
print("Ground Shipping cost: $" + str(cost_ground))

cost_ground_premium = 125
print("Ground Shipping Premium: $" +str(cost_ground_premium))

#Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9
elif weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25
print("Drone Shipping cost: $" + str(cost_drone))