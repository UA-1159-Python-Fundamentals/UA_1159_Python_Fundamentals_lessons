
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def day(num):
    try:
        num = int(num)
        if num<=0:
            return f"Error! There are no {num}day. Are you serious!?!"
        return days[num-1]
    except ValueError as e:
        return f"Error! {e}. The '{num}' is incorrect data!"
    except IndexError as e:
        return f"Error! {e}. There are no {num}day in the week!!!"

    

#Main cicle
while True:
    num = input("Please enter the number from 1 to 7 here: ")
    quit() if num=="q" else print(day(num))