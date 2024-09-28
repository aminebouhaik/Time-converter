calculation_to_seconds = 24 * 60 * 60
yes = "seconds"

def day_per_seconds(number_of_days):
    if number_of_days > 0:
        return f"{number_of_days} days are {number_of_days * calculation_to_seconds} {yes}"
    elif number_of_days == 0:
        return "you've entered 0 , please enter a positive number"
    else:
        return "You've entered a negative value, so smahana no conversion for you !"

user_input = input("Enter the number of days and I will convert it to seconds: ")
user_input_number = int(user_input)
calculation = day_per_seconds(user_input_number)
print(calculation)

