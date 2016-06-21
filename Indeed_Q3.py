import sys
import os
import numpy as np

# orientation

north = np.array([0, 1])
south = np.array([0, -1])
east = np.array([1, 0])
west = np.array([-1, 0])


#assuming increasing in a clockwise
orientations = [north, east, south, west]



# 1<=sizeofcommands<=2500
def  doesCircleExists(commands):
    # need to get the final position of the robot after two executions.  If the distance is greater after two then no, else yes.
    position = origin = np.array([0,0])
    orientation = 0 #assume facing north at the start

    for command in commands:
        if command == "G":
            #move in the orientation specified
            position = position + orientations[orientation]

        else: #adjust the position
            if command == "L":
                orientation = (orientation - 1) % 4
            else:
                orientation = (orientation + 1) % 4

    """
    http://stackoverflow.com/questions/28967020/check-if-there-exists-a-circle
    This is true, but three of the runs are unnecessary. A run can be collapsed into a move and a rotate. If the rotate is 0 and the move is not 0, then the walk is unbounded. Otherwise the walk is bounded; after two or four runs, the origin and the rotation will be back to the original
    """
    if orientation == 0 and not np.array_equal(position, origin):
        return "NO"
    else:
        return "YES"

    """
        A way.  I looked up the agorithm and found a more accurate [?] way to determine
        # if both directions are of the same sign, then it will constantly go.
        # if they are different signs but of the same magnitude, they will constantly go

        delta = position - origin
        if delta[0] * delta[1] > 0:
            # they have the same sign
            return "NO"
        elif abs(delta[0])==abs(delta[1]): #catches 0,0 as well
            return "YES"
        else:
            return "NO"

    """



if __name__ == '__main__':
    commands = "L"
    print doesCircleExists(commands)

    commands = "GRGL"

    print doesCircleExists(commands)

    commands = "GRGRGRG"

    print doesCircleExists(commands)