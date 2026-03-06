def calculate_bmi(weight, height, unit_system='metric'):
    if unit_system.lower() == 'metric':
        # Weight in kg, height in meters
        bmi = weight / (height ** 2)
    else:
        # Weight in lbs, height in inches
        bmi = (weight / (height ** 2)) * 703
    return round(bmi, 2)

def get_category(bmi):
    if bmi < 18.5: return "Underweight"
    elif 18.5 <= bmi < 25: return "Normal weight"
    elif 25 <= bmi < 30: return "Overweight"
    else: return "Obesity"

# Example Usage
w = float(input("Enter weight: "))
h = float(input("Enter height: "))
system = input("Metric or Imperial? ").strip()

result = calculate_bmi(w, h, system)
print(f"Your BMI is: {result} ({get_category(result)})")