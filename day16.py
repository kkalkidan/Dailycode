"""
@Question
You are given a list of rectangles represented by min and max x- and y-coordinates. 
Compute whether or not a pair of rectangles overlap each other. If one rectangle completely
covers another, it is considered overlapping.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}

return true as the first and third rectangle overlap each other.

"""

def compute_dimensions(i, rectangles):
    xi_min = rectangles[i]["top_left"][0]
    xi_max = xi_min + rectangles[i]["dimensions"][0]
    yi_max = rectangles[i]["top_left"][1]
    yi_min = yi_max - rectangles[i]["dimensions"][1]
    return xi_min, xi_max, yi_min, yi_max 

def Overlaps(rectangles):

    for i in range(len(rectangles)-1):
        xi_min, xi_max, yi_min, yi_max  = compute_dimensions(i, rectangles)  
        for j in range(i+1, len(rectangles)): 
            xj_min, xj_max, yj_min, yj_max = compute_dimensions(j, rectangles)
            if(
                min(yi_max, yj_max) - max(yi_min, yj_min) > 0 
                and
                min(xi_max, xj_max) - max(xi_min, xj_min) > 0
            ):return True

    return False


assert Overlaps([{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}])

assert not Overlaps([{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},])