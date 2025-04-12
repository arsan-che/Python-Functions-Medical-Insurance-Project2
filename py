# Create calculate_insurance_cost() function to estimate insurance costs
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name):
    # Calculate the estimated insurance cost using the given formula
    estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

    # Print the estimated insurance cost with the person's name
    print(f"The estimated insurance cost for {name} is {estimated_cost} dollars.")
    
    # Return the estimated cost
    return estimated_cost
