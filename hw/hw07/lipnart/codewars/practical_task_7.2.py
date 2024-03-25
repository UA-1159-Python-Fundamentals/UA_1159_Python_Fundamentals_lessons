# I. Jenny's secret message
# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     else:
#         return "Hello, {name}!".format(name=name)
    

# # II. Find The Distance Between Two Points
# def distance(x1, y1, x2, y2):
#     dis = ((x2 - x1)**2 + (y2-y1)**2)**0.5
#     dis = round(dis, 2)
#     return dis


# III. No yelling!

def filter_words(st):

    st = st.split()
    st = ' '.join(st)
    st = st.capitalize()
    
    return st

a = 'This    will    not    pass '
print(filter_words(a))