# Cameron Wood
# Daily Calorie Intake w/ Protein, Carbs, and Fat
# 06/01/2020

print("Welcome to your Daily Nutrition Tracker\n")

# BMI Calculator
def bmi():
    print("Select from the menu below as to what units you will be using:")
    print("1. Metric\n2. Customary")
    user_unit_selection = float(input("Enter Choice:\t"))

    if user_unit_selection == 1:
        weight = float(input("Please enter your weight in kilograms:\t"))
        height = float(input("Please enter your height in meters:\t"))

    elif user_unit_selection == 2:
        weight = float(input("Please enter your weight in pounds:\t"))
        height = float(input("Please enter your height in inches:\t"))

        weight = weight * 0.453592
        height = height * 0.0254

    height_sq = height * height
    bmi_calculated = weight / height_sq
    print("Your BMI is:\t" + str(bmi_calculated))

    # Test if normal weight

    if bmi_calculated < 18.5:
        print("You are underweight\t")
    elif bmi_calculated >= 18.5 and bmi_calculated < 24.9:
        print("You are normal weight\t")
    elif bmi_calculated >= 25 and bmi_calculated < 29.9:
        print("You are overweight\t")
    else:
        print("You are obese\t")


# Item Tracker
item_list = []
calorie_list = []
protein_list = []
carbs_list = []
fat_list = []

def item_info():
    new_item = input("Please give a name for the item:\t")
    print("\n")
    item_list.append(new_item)

    new_calorie = float(input("Please give a calorie count for the item:\t"))
    print("\n")
    calorie_list.append(new_calorie)

    new_protein = float(input("Please give a protein count for the item:\t"))
    print("\n")
    protein_list.append(new_protein)

    new_carbs = float(input("Please give a carbohydrate count for the item:\t"))
    print("\n")
    carbs_list.append(new_carbs)

    new_fat = float(input("Please give a fat count for the item:\t"))
    print("\n")
    fat_list.append(new_fat)

# Finding info and totals
def nutrition_summation():
    total_calorie = str(sum(calorie_list))
    total_protein = str(sum(protein_list))
    total_carbs = str(sum(carbs_list))
    total_fat = str(sum(fat_list))

    length_items = len(item_list)
    for n in range(length_items):
        print(str(item_list[n]) + "\t\t " + str(calorie_list[n]) + "\t\t " + str(protein_list[n]) + "\t\t " + str(carbs_list[n]) + "\t\t " +
              str(fat_list[n]))
    print("Totals:\t\t " + total_calorie + "\t\t " + total_protein + "\t\t " + total_carbs + "\t\t " + total_fat)


#Menu to select what to do next
def menu_choice():
    print("Please select from the following list as to what you would like to do:\n")
    print("1. Enter an item\n2. Print info and find totals\n3. BMI Calculator\n4. Exit\t")

    user_choice = int(input("Enter Choice:\t"))
    print("\n")
    if user_choice == 1:
        item_info()
        menu_choice()

    elif user_choice == 2:
        print("Item\t\t Calories\t Protein\t Carbs\t\t Fat")
        nutrition_summation()
        menu_choice()

    elif user_choice == 3:
        bmi()
        menu_choice()

menu_choice()