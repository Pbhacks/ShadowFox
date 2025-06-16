# -------------------------------
# TASK 1: VARIABLES
# -------------------------------

print("\n--- Task 1: Variables ---")

# 1. Create a variable named pi and check its data type
pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))

# 2. Create a variable called 'for' (this will raise an error if uncommented)
print("Trying to assign value to 'for' will raise SyntaxError since 'for' is a reserved keyword.")

# 3. Simple Interest calculation
P = 10000  # Principal
R = 5      # Rate of Interest
T = 3      # Time in years
simple_interest = (P * R * T) / 100
print("Simple Interest for 3 years is:", simple_interest)

# -------------------------------
# TASK 2: NUMBERS
# -------------------------------

print("\n--- Task 2: Numbers ---")

# 1. Format function with number and format specifier
def formatted_string(val, spec):
    try:
        return format(val, spec)
    except ValueError as e:
        return f"Error: {e}"

print("Formatted string (145 with 'o'):", formatted_string(145, 'o'))  # Octal

# 2. Area of circular pond and water content
radius = 84
pi_val = 3.14
pond_area = int(pi_val * (radius ** 2))
water_per_sqm = 1.4
total_water = int(pond_area * water_per_sqm)
print(f"Area of pond: {pond_area} sqm")
print(f"Total water in the pond: {total_water} liters")

# 3. Speed calculation
distance_m = 490
time_min = 7
speed_mps = int(distance_m / (time_min * 60))
print("Speed in m/s (without decimal):", speed_mps)

# -------------------------------
# TASK 3: LIST OPERATIONS
# -------------------------------

print("\n--- Task 3: Justice League List Operations ---")

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Original List:", justice_league)

# 1. Number of members
print("Number of members:", len(justice_league))

# 2. Add Batgirl and Nightwing
justice_league += ["Batgirl", "Nightwing"]
print("After adding Batgirl and Nightwing:", justice_league)

# 3. Move Wonder Woman to start
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman the leader:", justice_league)

# 4. Separate Aquaman and Flash by moving Superman between them
justice_league.remove("Superman")
index_flash = justice_league.index("Flash")
justice_league.insert(index_flash, "Superman")
print("After separating Aquaman and Flash with Superman:", justice_league)

# 5. Replace with new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Justice League team:", justice_league)

# 6. Sort and display new leader
justice_league.sort()
print("Sorted Justice League:", justice_league)
print("New leader (0th index):", justice_league[0])

# -------------------------------
# TASK 4: IF CONDITION
# -------------------------------

print("\n--- Task 4: BMI & City Country Matching ---")

# 1. BMI Category
try:
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kilograms: "))
    bmi = weight / (height ** 2)
    if bmi >= 30:
        print("Obesity")
    elif bmi >= 25:
        print("Overweight")
    elif bmi >= 18.5:
        print("Normal")
    else:
        print("Underweight")
except:
    print("Invalid height or weight input!")

# 2. City-Country Mapping
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name: ").strip()

if city in australia:
    print(f"{city} is in Australia")
elif city in uae:
    print(f"{city} is in UAE")
elif city in india:
    print(f"{city} is in India")
else:
    print("City not found in the given list.")

# 3. Check if two cities are in same country
city1 = input("Enter first city: ").strip()
city2 = input("Enter second city: ").strip()

def find_country(city):
    if city in australia:
        return "Australia"
    elif city in uae:
        return "UAE"
    elif city in india:
        return "India"
    else:
        return None

country1 = find_country(city1)
country2 = find_country(city2)

if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities not recognized.")

# -------------------------------
# TASK 5: FOR LOOP
# -------------------------------

print("\n--- Task 5: Dice Rolls & Workout Simulation ---")

# 1. Dice roll simulation
import random

dice_rolls = [random.randint(1, 6) for _ in range(20)]
count_6 = dice_rolls.count(6)
count_1 = dice_rolls.count(1)
count_double_6 = sum(1 for i in range(len(dice_rolls)-1) if dice_rolls[i] == 6 and dice_rolls[i+1] == 6)

print("Dice rolls:", dice_rolls)
print("Number of times 6 rolled:", count_6)
print("Number of times 1 rolled:", count_1)
print("Number of times two 6s rolled in a row:", count_double_6)

# 2. Jumping jacks simulation
total_jumping_jacks = 100
completed = 0
for i in range(10):
    completed += 10
    print(f"You have completed {completed} jumping jacks.")
    response = input("Are you tired? (yes/no): ").lower()
    if response in ["yes", "y"]:
        skip = input("Do you want to skip remaining sets? (yes/no): ").lower()
        if skip in ["yes", "y"]:
            break
        else:
            continue
if completed < total_jumping_jacks:
    print(f"You completed a total of {completed} jumping jacks.")
else:
    print("Congratulations! You completed the workout.")
