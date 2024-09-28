calculation_to_seconds = 24 * 60 * 60
yes = "seconds"

def day_per_seconds(number_of_days):
  return f"{number_of_days} days are {number_of_days * calculation_to_seconds} {yes}"

user_input=input("enter the number of days and i will convert it to seconds : ")
user_input_number= int(user_input)
calculation= day_per_seconds(user_input_number)
print(calculation)
