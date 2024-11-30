from DSL.hodel_utils import *

class Pnode():
    def __init__(self, Gnode, row, col):
        self.id = row * Gnode.width + col + 1
        # self.io = "Input"
        self.type = "pixel"
        self.row = self.get_row(row)
        self.col = self.get_col(col)
        self.coord = self.get_coord() 
        self.color = self.get_color(Gnode, row, col) # -> grid[0][0][0] 

        # characteristic that could be found in pixel-wise observation
        # self.diff_color_neighbors = get_diff_color
    
    def get_row(self, row):
        return row
    
    def get_col(self, col):
        return col
    
    def get_coord(self):
        return (self.row, self.col)

    def get_color(self, Gnode, row, col):
        return Gnode.grid[row][col]
    
    def __str__(self):
        return f"{self.type} node, id = {self.id}, coord = {self.coord}, color = {self.color}"






class Onode():
    def __init__(self, Gnode, o, object):
        self.id = Gnode.width * Gnode.height + o + 1
        self.type = "object"
        self.colcoord = object
        self.grid = self.get_grid()
        self.color = self.get_color(object) # -> (0, 1, 2, 5, 6)
        self.single_colored = self.is_single_color() # -> False
        self.coords = self.get_coord() # -> frozenset({(0,0), (0,1), ... (8,8)})
        self.bbox = self.get_bbox() # -> [(0,0), (9,9)]
        self.size = self.get_bbox_size() # -> (9, 9)
        self.height = self.get_bbox_height() # -> 9
        self.width = self.get_bbox_width() # -> 9
        self.relative_coord = self.get_relative_coord() # -> [(0,0), (0,1), ... (8,8)]
        self.relative_colcoord = self.get_relative_colcoord() # -> frozenset({(0,0), (0,1), ... (8,8)})
        
        self.hori_symm = self.is_hori_symmetric() # -> True
        self.verti_symm = self.is_verti_symmetric() # -> True

        self.margin_coord = self.get_margin_coord() # margin(ring shape)
        self.inner_coord = self.get_inner_coord() # nonmargin
        self.corner_coord = self.get_corner_coord() # corner
        self.edge_coord = self.get_edge_coord() # edge
        
        self.center = self.get_center() # four types of center of mass expression


        ## do it later
        # self.diag_symm = self.is_diag_symmetric() # -> True
        # self.rdiag_symm = self.is_rdiag_symmetric() # -> True

        # self.rectangle = self.is_rectangle() # -> True
        # self.square = self.is_square() # -> True
        # self.cross = self.is_cross() # -> True
        # self.ring = self.is_ring() # -> True
        # self.shape = self.get_shape(Gnode) # can be unique besides square, bar, cross, ring # need definition

    def get_grid(self):
        return togrid(self.colcoord)

    def get_color(self, object):
        color_set = set()
        for colcoord in object:
            color_set.add(colcoord[0])
        return color_set
    
    def is_single_color(self):
        return True if len(self.color) == 1 else False
    
    def get_coord(self):
        coord_list = []
        for colcoord in self.colcoord:
            coord_list.append(colcoord[1])
        return coord_list
    
    def get_bbox(self):
        row_list = []
        col_list = []
        for colcoord in self.colcoord:
            row_list.append(colcoord[1][0])
            col_list.append(colcoord[1][1])
        return [(min(row_list), min(col_list)), (max(row_list), max(col_list))]
    
    def get_bbox_size(self):
        return (self.bbox[1][0] - self.bbox[0][0] + 1, self.bbox[1][1] - self.bbox[0][1] + 1)
    
    def get_bbox_height(self):
        return self.size[0]
    
    def get_bbox_width(self):
        return self.size[1]
    
    def get_relative_coord(self):
        relative_coord = []
        for coord in self.coords:
            relative_coord.append((coord[0] - self.bbox[0][0], coord[1] - self.bbox[0][1]))
        return relative_coord

    def get_relative_colcoord(self):
        relative_colcoord = []
        for colcoord in self.colcoord:
            relative_colcoord.append((colcoord[0], (colcoord[1][0] - min(self.coords)[0], colcoord[1][1] - min(self.coords)[1])))
        return relative_colcoord

    def is_hori_symmetric(self):
        hori_symm = True
        top_half = self.grid[:self.height // 2]
        bottom_half = self.grid[-(self.height // 2):]
        
        if top_half != bottom_half[::-1]:  # Reverse bottom half for comparison
            hori_symm = False
        return hori_symm
    
    def is_verti_symmetric(self):
        verti_symm = True
        for row in self.grid:
            left_half = row[:self.width // 2]
            right_half = row[-(self.width // 2):]
            if left_half != right_half[::-1]:  # Reverse right half for comparison
                verti_symm = False
                break
        return verti_symm

    def get_margin_coord(self):
        margin_coord = []
        for coord in self.relative_coord:
            if coord[0] == 0 or coord[0] == self.height or coord[1] == 0 or coord[1] == self.width:
                margin_coord.append(coord)
        return margin_coord
    
    def get_inner_coord(self):
        inner_coord = []
        for coord in self.relative_coord:
            if coord not in self.margin_coord:
                inner_coord.append(coord)
        return inner_coord
    
    def get_corner_coord(self):
        corner_coord = []
        for coord in self.relative_coord:
            if coord == (0, 0) or coord == (0, self.width) or coord == (self.height, 0) or coord == (self.height, self.width):
                corner_coord.append(coord)
        return corner_coord
        
    def get_edge_coord(self):
        edge_coord = []
        for coord in self.relative_coord:
            if coord in self.margin_coord and coord not in self.corner_coord:
                edge_coord.append(coord)
        return edge_coord

    def get_center(self):
        center = []
        # even * even -> 2 * 2 center
        if self.size[0] % 2 == 0 and self.size[1] % 2 == 0:
            center.append((self.size[0] // 2-1, self.size[1] // 2-1))
            center.append((self.size[0] // 2-1, self.size[1] // 2))
            center.append((self.size[0] // 2, self.size[1] // 2-1))
            center.append((self.size[0] // 2, self.size[1] // 2))
            return center
        
        # even * odd -> 2 * 1 center
        if self.size[0] % 2 == 0 and self.size[1] % 2 != 0:
            center.append((self.size[0] // 2-1, self.size[1] // 2))
            center.append((self.size[0] // 2, self.size[1] // 2))
            return center

        # odd * even -> 1 * 2 center
        if self.size[0] % 2 != 0 and self.size[1] % 2 == 0:
            center.append((self.size[0] // 2, self.size[1] // 2-1))
            center.append((self.size[0] // 2, self.size[1] // 2))
            return center
        
        # odd * odd -> 1 * 1 center
        if self.size[0] % 2 != 0 and self.size[1] % 2 != 0:
            center.append((self.size[0] // 2, self.size[1] // 2))
            return center


    def __str__(self):
        return f"{self.type} node, id = {self.id}, color = {self.color}"
    





class Gnode():
    def __init__(self, grid):
        self.id = 0
        self.grid = grid
        self.type = "grid"
        
        self.height = self.get_height(grid)
        self.width = self.get_width(grid)
        self.color = self.get_color(grid) # -> (0, 1, 2, 5, 6)
        self.single_colored = self.is_single_color() # -> False
        self.colcoord = self.get_colcoord()
        self.size = self.get_size() # -> (9, 9)
        
    def get_height(self, grid):
        return len(grid)
    
    def get_width(self, grid):
        return len(grid[0])
    
    def get_color(self, grid):
        color_set = set()
        for row in grid:
            color_set.update(set(row))
        return color_set
    
    def is_single_color(self):
        return True if len(self.color) == 1 else False
        # a lot overlaping with Onode characteristics cuz Gnode is just a one kind of Onode.

    def get_colcoord(self):
        colcoord = []
        for row in range(self.height):
            for col in range(self.width):
                colcoord.append((self.grid[row][col], (row, col)))
        return frozenset(colcoord)
    
    def get_size(self):
        return (self.height, self.width)
    
    def __str__(self):
        return f"{self.type} node, id = {self.id}, size = {self.size}, color = {self.color}"
				







# class Vnode():
#     # Should Vnode take two grids or only one for node construction?
#     def __init__(self, inpt_grid, output_grid): # OR (self, grid)
#         # and what can be its characteristic?
#         self.
        



if __name__ == "__main__":
	print("this is node definition file")