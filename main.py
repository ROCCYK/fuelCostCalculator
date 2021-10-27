Trip_Distance = float(input('Trip Distance: '))
Fuel_Efficiency = float(input('Fuel Efficiency in Liters per 100km: '))/100
Gas_Fuel_Price = float(input('Gas Price: '))

fuel_cost = Trip_Distance * Fuel_Efficiency * Gas_Fuel_Price

print(f'This trip will require {round((Fuel_Efficiency * 100), 2)} liters of fuel, which amounts to a fuel cost of ${round(fuel_cost,2)}')