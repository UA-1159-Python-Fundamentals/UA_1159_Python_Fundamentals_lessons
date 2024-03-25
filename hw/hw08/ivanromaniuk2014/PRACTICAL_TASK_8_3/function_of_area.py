from math import pow, pi

def area_of_rectangle( a:float, b:float ) -> float:
    """
    Calculates the area of a rectangle.

    Args:
        a (float): Length of one side of the rectangle.
        b (float): Length of the other side of the rectangle.

    Returns:
        float: Area of the rectangle.
    """
    return a * b

def area_of_triangle( h:float, a:float ) -> float:
    """
    Calculates the area of a triangle.

    Args:
        h (float): Height of the triangle.
        a (float): Length of its base.

    Returns:
        float: Area of the triangle.
    """
    return 0.5 * h * a 

def area_of_circle( r:float ) -> float:
    """
    Calculates the area of a circle.

    Args:
        r (float): Radius of the circle.

    Returns:
        float: Area of the circle.

    """
    return pi * pow(r, 2)
