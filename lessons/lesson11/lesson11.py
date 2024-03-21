

# while True:
#     try:
#         a = int(input("enter number a:"))
#         b = int(input("enter number b:"))
#         print(a/b)
#     except ZeroDivisionError as err:
#         print("b is 0", err)
#     except ValueError as err:
#         print("Error_1", err)
#     except NameError as err:
#         print("Error_2", err)
#     else:
#         print("win")
#         break
#     finally:
#         print("finally")

# def f():
#     try:
#         print(">>10")
#         return 10
#         print(">>10<<")
#     finally:
#         print("eturn 20")
    
# print(f())


from logconfig import logging



from models import Point, PointError
    
points = []
values = (1,2,3,4,"5", 5.6, 9.6, "aaa", [1,23,4])
while len(points) < 10:
    import random
    x = random.choice(values)
    y = random.choice(values)
    try:
        logging.debug(f"{x=}{y=}")
        point = Point(x, y)
    except ValueError as err:
        print(err)
    except PointError as err:
        logging.error(err)
        print(err)
    except:
        print(":(")
    else:
        points.append(point)

print(points)