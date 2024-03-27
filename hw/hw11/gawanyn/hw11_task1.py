# # # Task 1
# # # Variant 1
# while True:
#     age = int(input("Enter your age: "))

#     try:
#         if age < 0:
#             raise ValueError("Age cannot be negative")
        
#         if age % 2 == 0:
#             print("Your age is even.")
#             break
#         else:
#             print ("Your age is odd.")
#             break
#     except ValueError as ve:
#         print("Error:", ve)

# # Task 1
# # Variant 2
# def check_age():

#     age = int(input("Enter your age: "))

#     try:
#         if age < 0:
#             raise ValueError("Age cannot be negative")
        
#         if age % 2 == 0:
#             print("Your age is even.")
#         else:
#             print("Your age is odd.")
#     except ValueError as ve:
#         print("Error", ve)

# check_age()

# Task 2

def check_day(day):
    
    try:
        day = int(day)
        if 1 < day > 7:
            raise ValueError
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return days[day - 1]
    except ValueError:
        print("Error, enter correct index.")

print(check_day(2))

