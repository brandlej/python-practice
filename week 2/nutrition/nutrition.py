def main():
    # normalize input
    fruit = input("Item: ").lower().strip()

    # get cals for given fruit
    fruit_calories = get_fruit_calories(fruit)

    # if defined, print
    # check using pythonic "is not" - more idiomatic
    if fruit_calories is not None:
        print(f"Calories: {fruit_calories}")
        
# helper
def get_fruit_calories(fruit: str):
    # define lookup
    fruit_cals_lookup = {
        "apple": 130,
        "avocado": 50,
        "sweet cherries": 100
    }

    # short circuit if it doesn't exist
    if fruit not in fruit_cals_lookup:
        return None

    # get using dictionary method
    return fruit_cals_lookup.get(fruit)

main()