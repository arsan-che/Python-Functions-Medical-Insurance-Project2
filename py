# Create calculate_insurance_cost() function to estimate insurance costs
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name):
    # Calculate the estimated insurance cost using the given formula
    estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

    # Print the estimated insurance cost with the person's name
    print(f"The estimated insurance cost for {name} is {estimated_cost} dollars.")
    
    # Return the estimated cost
    return estimated_cost
# Estimate Maria's insurance cost by calling the function with her details
maria_insurance_cost = calculate_insurance_cost(age=28, sex=0, bmi=26.2, num_of_children=3, smoker=0, name='Maria')

# Estimate Omar's insurance cost by calling the function with his details
omar_insurance_cost = calculate_insurance_cost(age=35, sex=1, bmi=22.2, num_of_children=0, smoker=1, name='Omar')

# Estimate Ivar's insurance cost by calling the function with their details
ivar_insurance_cost = calculate_insurance_cost(age=20, sex=0, bmi=22.2, num_of_children=0, smoker=0, name='Ivar')

# Create calculate_cost_difference() function to find the difference between two insurance costs
def calculate_cost_difference(cost1, cost2):
    # Calculate the absolute difference between the two costs
    difference = abs(cost1 - cost2)
    
    # Print the difference in insurance costs
    print(f"The difference between Maria's and Omar's insurance costs is {difference} dollars.")
    
    # Return the difference
    return difference
    
# Calculate the difference between Maria's and Omar's insurance costs
difference_between_costs = calculate_cost_difference(cost1=maria_insurance_cost, cost2=omar_insurance_cost)
