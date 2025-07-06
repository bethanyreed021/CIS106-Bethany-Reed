def comp_mpg_cost(miles_travelled,gallons_used):
    mpg = miles_travelled / gallons_used
    cost_of_gas = gallons_used * 3
    return mpg, cost_of_gas

num_of_trips = 0
total_miles = 0
total_gas_cost = 0

response = input("Do you want to start this program (Yes or No)?")

while(response == 'Yes'):
    dest_city = input("Enter Destination City: ")
    miles_travelled = float(input("Enter miles travelled: "))
    gallons_used = float(input("Enter gallons used: "))
    values = comp_mpg_cost(miles_travelled,gallons_used)
    mpg = values[0]
    cost_of_gas = values[1]
    print("Destination city: ", dest_city)
    print("Miles travelled: ", miles_travelled)
    print("Miles per gallon: %.2f"% mpg)
    print("Cost of gas: $%.2f"% cost_of_gas)
    num_of_trips = num_of_trips + 1
    total_miles = total_miles + miles_travelled
    total_gas_cost = total_gas_cost + cost_of_gas
    response = input("Do you want to continue the program (Yes or No)?")

print("Number of trips entered: ", num_of_trips)
print("Total miles travelled: ", total_miles)
print("Total cost of gas: $%.2f"% total_gas_cost)