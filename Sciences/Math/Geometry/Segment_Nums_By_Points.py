import argparse

def main():
    """
This program takes the number of points (or vertices) in a polygon to
calculate: the number of diagonals, the number of external segments, and
the total number of segments 
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("numPoints",
        help="numPoints is the number of points of the polygon",type=int)
    args = parser.parse_args()
    numPoints = args.numPoints

    print("The number of external segments is:",external_segments(numPoints))
    print("The number of diagonal segments is:",diagonal_segments(numPoints))
    print("The total number of segments is:",total_segments(numPoints))
    
def external_segments(numPoints):
    """The number of external segments equals the number of points"""
    return numPoints

def diagonal_segments(numPoints):
    """with n points, the diagonals are (n-3)*n/2"""
    return (numPoints-3)*numPoints/2

def total_segments(numPoints):
    """The total number of segments is the sum of external and diagonals"""
    return external_segments(numPoints) + diagonal_segments(numPoints)

if __name__ == '__main__':
    main()