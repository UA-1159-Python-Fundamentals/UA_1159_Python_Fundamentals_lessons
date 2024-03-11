def destination(tuple_a, tuple_b):
    destination = ((tuple_a[0]-tuple_b[0])**2+(tuple_a[1]-tuple_b[1])**2)**0.5
    destination = round(destination, 2)

    return destination

print(destination((10,20), (20,30)))