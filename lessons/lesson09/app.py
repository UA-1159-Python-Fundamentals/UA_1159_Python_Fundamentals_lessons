# import pygame
# from random import randint

# pygame.init()


# gameDisplay = pygame.display.set_mode((800, 600))

# pygame.display.set_caption("My first game")

# clock = pygame.time.Clock()


# rect = [50, 50, 11, 11]


# def resize_rect(new_size=-1):
#     if new_size == -1 and rect[2] < 10:
#         return
#     rect[2] = rect[2] + new_size
#     rect[3] = rect[3] + new_size


# class Circle:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y
#         self.r = randint(10, 100)
#         self.color = [randint(0, 255), randint(0, 255), randint(0, 255)]
#         self.up = randint(0, 1)

#     def get_center(self):
#         return (self.x, self.y)

#     def update(self):
#         if self.up:
#             if self.r < 250:
#                 self.r += 1
#             else:
#                 self.up = False
#         else:
#             if self.r > 20:
#                 self.r -= 1
#             else:
#                 self.up = True


# points = []
# circle = []
# DONE = False
# COLOR = (0, 0, 0)
# while not DONE:
#     for event in pygame.event.get():  # User did something
#         # print(event)
#         if event.type == pygame.QUIT:  # If user clicked close
#             # print(event)
#             DONE = True  # Flag that we are done so we exit this loop
#         elif event.type == pygame.KEYDOWN:
#             print("User pressed a key.", event)
#             key = event.dict.get("key")
#             match key:
#                 case 1073741906:
#                     rect[1] = rect[1] - 5
#                 case 1073741903:
#                     rect[0] = rect[0] + 5
#                 case 1073741905:
#                     rect[1] = rect[1] + 5
#                 case 1073741904:
#                     rect[0] = rect[0] - 5
#                 case 117:
#                     resize_rect(20)
#         elif event.type == pygame.KEYUP:
#             print("User let go of a key.", event)
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             print("User pressed a mouse button", event)
#             button = event.dict.get("button")
#             pos = event.dict.get("pos")
#             match button:
#                 case 1:

#                     points.append(pos)
#                 case 2:
#                     circle.append(Circle(*pos))
#                 case 3:
#                     points.pop()

#     gameDisplay.fill(COLOR)

#     if len(points) > 2:
#         pygame.draw.polygon(gameDisplay, (0, 255, 0), points)
#     pygame.draw.rect(gameDisplay, (255, 0, 0), rect)
#     resize_rect()

#     for c in circle:
#         c.update()
#         pygame.draw.circle(gameDisplay, c.color, c.get_center(), c.r, 5)

#     pygame.display.update()
#     # print(rect)
#     clock.tick(60)


def add(a, b):
    return a+b
def mult(a,b):
    return a*b

comands = [add, mult]
comands = {
    "add": add,
    "mult": mult
}

while True:
    a = int(input("a: "))
    b = int(input("b: "))
    for f in comands:
        print(a, b,f.__name__,  f(a,b), f.__call__(a,b))

