import datetime

goal = input("Please enter your goal: ")
deadline = input("Please enter the deadline by which you think you will be ready to achieve your goal (dd.mm.yyyy): ")

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_till = deadline_date - today_date

print(f"Time remaining for your goal: {goal} is {time_till}")
