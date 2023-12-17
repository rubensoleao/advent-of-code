import os
import sys

from functools import lru_cache

sys.setrecursionlimit(10000000)
print(os.getcwd())

f = open("16test-in.txt",'r')
# f = open("16a-in.txt",'r')
inp = f.read()
inp = inp.split('\n')
inp = inp[:-1]
maxY = len(inp)
maxX = len(inp[0])
print(maxX, maxY)
f.close()

paths = set()
paths_calculated = set()

def print_map(i=-1,j=-1):
    for y in range(maxY):
        for x in range(maxX):
            if (i,j) == (x,y):
               print("O", end="")
            elif (x,y) in paths:
                if inp[y][x] == ".":
                    print("X", end="")
                else:
                    print(inp[y][x],end="")
            else:
                print(inp[y][x], end="")
        print("")
    print(f"x={i},y{j}")


count_paths_cache = dict()

@lru_cache(maxsize=None)
def count_paths(x,y,d):
    os.system('cls' if os.name == 'nt' else 'clear')
    paths.add((x,y))
    if (x,y,d) in paths_calculated:
        return
    paths_calculated.add((x,y,d))
    if PRINT:
        print_map(x,y)
        input()
    if y >= maxY or x >= maxX or y< 0 or x < 0:
        return
    curr_tile = inp[y][x]
    match curr_tile:
        case '.':
            # If the beam encounters empty space (.), it continues in the same direction.
            return 1 + count_paths(x+d[0], y+d[1], d)
        case '\\':
            match d:
                case (0,1):
                    new_d=(1,0)
                case (0,-1):
                    new_d=(-1,0)
                case (1,0):
                    new_d=(0,1)
                case (-1,0):
                    new_d=(0,-1)
                case _:
                    raise Exception()
            d = new_d
            return 1 + count_paths(x+d[0], y+d[1], d)
        case '/':
            match d:
                case (0,1):
                    new_d=(-1,0)
                case (0,-1):
                    new_d=(1,0)
                case (1,0):
                    new_d=(0,-1)
                case (-1,0):
                    new_d=(0,1)
                case _:
                    raise Exception()
            d = new_d
            return 1 + count_paths(x+d[0], y+d[1], d)
        case '|':
            match d:
                case (0,1) | (0,-1):
                    return 1 + count_paths(x+d[0], y+d[1], d)
                case (1,0) | (-1,0):
                    return 1 +  count_paths(x+0, y+1, (0,1)) + count_paths(x+0, y-1, (0,-1))
                case _:
                    raise Exception()
        case '-':
            match d:
                case (0,1) | (0,-1):
                    return 1 +  count_paths(x+1, y+0, (1,0)) + count_paths(x-1, y+0, (-1,0))
                case (1,0) | (-1,0):
                    return 1 + count_paths(x+d[0], y+d[1], d)
                case _:
                    raise Exception()
        case _:
            raise Exception("invalid input map")

PRINT = True
print(count_paths(0,0,(1,0)))
print(len(paths))
#max_result= -1
#max_config:None
#PRINT = False
#for yy in range(maxY):
#    # Left edge
#    paths = set()
#    paths_calculated = set()
#    count_paths(00,yy,(1,0))

#    total = len(paths)
#    if max_result < total:
#        max_result=total
#        max_config=(00,yy)

#    #Right edge
#    paths = set()
#    paths_calculated = set()
#    count_paths(00,maxY,(-1,0))
    
#    total = len(paths)
#    if max_result < total:
#        max_result=total
#        max_config=(00,maxY)
    
#    #top and bottom edge
#    if yy == 0 or yy==maxY-1:
#        if yy==0:
#            direction=(0,1)
#        else:
#            direction=(0,-1)
#        for xx in range(maxX):
#            paths = set()
#            paths_calculated = set()
#            count_paths(xx,yy,direction)

#            total = len(paths)
#            if max_result < total:
#                max_result=total
#                max_config=(xx,yy)
#    print(yy, '/', maxY)
#print(max_result, max_config)
