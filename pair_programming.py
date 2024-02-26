# Julia's comments: Function doc string looks great, very detailed and explains what the function does along with an example. You could maybe shorten the description a little shorter but it's not necessary c:
def polar_to_cart(r, theta):
    """Converts coordinates from polar to cartesian.
    
    Takes a given input of a coordinate point in polar form, where theta is given in radians, and returns the same point for the cartesian coordinate system.
    
    Parameters
    ----------
    r: int or float
        Input data for the r part of the polar coordinate.
    
    theta: int or float
        Input data for the theta part of the polar coordinate, in radians.
    
    Returns
    -------
    cartesian_pt : list (of floats)
        A cartesian point in list form following: [x, y].
        
    Examples
    -------
    >>> import math 
    >>> polar_to_cart(4, math.pi/3)
    [2.0000000000000004, 3.4641016151377544]
    
    >>> import math
    >>> polar_to_cart(2, math.pi)
    [-2.0, 2.4492935982947064e-16]
    """

    # Julia's comments: documentation looks great! Code is very clear and you explain what you are doing and why very well. The use of white space is also very nice. No changes needed here!
    # import math module
    import math # Julia's comments: math needs to be imported outside of the function
    
    # calculate x and y
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    
    # place the coordinate point in a list to format it nicely
    cartesian_pt = [x, y]
    
    return cartesian_pt

# Julia's test function:
def test_polar_to_cart():
    # test case 1
    result1 = polar_to_cart(4, math.pi/3)
    assert result1 == [2.0000000000000004, 3.4641016151377544]
    
    # test case 2
    result2 = polar_to_cart(2, math.pi)
    assert result2 == [-2.0, 2.4492935982947064e-16]
    
    print("All tests passed.")

# call function
test_polar_to_cart()
    