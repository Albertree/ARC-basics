from .dsl import *
from .hodel_utils import *

def find_all_objects(grid):
    grid = totuple(grid)
    frozen_object_list = []
    # 1. single color, diagonal, background
    for obj in objects(grid, True, True, True):
        if obj not in frozen_object_list:
            frozen_object_list.append(obj)
    
    # 2. single color, diagonal, no background
    for obj in objects(grid, False, True, True):
        if obj not in frozen_object_list:
            frozen_object_list.append(obj)

    # 3. single color, not diagonal, background
    for obj in objects(grid, True, False, True):
        if obj not in frozen_object_list:
            frozen_object_list.append(obj)

    # 4. single color, not diagonal, no background
    for obj in objects(grid, False, False, True):
        if obj not in frozen_object_list:
            frozen_object_list.append(obj)

    # 5. multiple color, diagonal, background
    for obj in objects(grid, True, True, False):
        if obj not in frozen_object_list:
            frozen_object_list.append(obj)

    # 6. multiple color, diagonal, no background
    for obj in objects(grid, False, True, False):
        if obj not in frozen_object_list:
            frozen_object_list.append(obj)

    # 7. multiple color, not diagonal, background
    for obj in objects(grid, True, False, False):
        if obj not in frozen_object_list:
            frozen_object_list.append(obj)

    # 8. multiple color, not diagonal, no background
    for obj in objects(grid, False, False, False):
        if obj not in frozen_object_list:
            frozen_object_list.append(obj)

    # sort objects with length
    frozen_object_list.sort(key=lambda x: (len(x)))#, list(x)[0][1]))
    return frozen_object_list


def find_all_objects_sort(grid):
    all_objects = find_all_objects(grid)

    # convert frozenset to list
    all_objects_list = []
    for obj in all_objects:
        all_objects_list.append(list(obj))

    # sort each object
    for sublist in all_objects_list:
        sublist.sort(key=lambda x: x[1])

    all_objects_list.sort(key=lambda sublist: (len(sublist), sublist[0][1]))

    return all_objects_list


def find_all_objects_sort_grid(grid):
    all_objects_list = find_all_objects_sort(grid)

    # convert colcoord to grid
    all_objects_sort_grid = []
    for obj in all_objects_list:
        grid = togrid(obj)
        all_objects_sort_grid.append(grid)

    return all_objects_sort_grid