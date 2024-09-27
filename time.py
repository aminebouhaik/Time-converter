calculation_to_seconds = 24 * 60 * 60
yes = "seconds"

def day_per_seconds(number_of_days, message):
    print(f"{number_of_days} days are {number_of_days * calculation_to_seconds} {yes}")
    print(message)

day_per_seconds(20, "awesome!")
day_per_seconds(30, "looks good!")
