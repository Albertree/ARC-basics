
### Previous version of node definition #########################################

class Pnode :
    def __init__(self, grid, i, j):
        self.color = grid[i][j]
        self.number = self.node_number(len(grid[0]), i, j)
        self.visual_coord = [3 * j, 3 * (len(grid) - i - 1)]  ## coordinate for visualize
        self.coordinate = [j,i]         ## coordinate from the grid
        self.input = 0
        self.output = 0
        self.type = "Pnode"
    def node_number (self, col, i, j): ## start from 0 to (col * row -1) # may not needed
        temp = i * (col) + j
        return temp
    def __str__(self):
        if self.input == 1:
            return f"Pnode: N:{self.number}, I"
        else :
            return f"Pnode: N:{self.number}, O"
        
class Onode:
    def __init__(self, obj, condition):
        Pnode_list = []
        color_set = set()
        number_set = set()
        for Pnode in obj:
            Pnode_list.append(Pnode)
            color_set.add(Pnode.color)
            number_set.add(Pnode.number)
        self.Pnode_list = Pnode_list
        self.color = color_set            ##questionalbe 
        self.number = number_set  
        self.coordinate = [0,0]
        self.input = 0
        self.output = 0
        self.type = "Onode"
        self.condition = condition
        # [get_coordinate(node) for node in get_center_nodes]    ##questionalbe -> need bbox function first and type will be {(int, int), (int, int) ...}
    def __str__(self):
        pnodes = []
#        for pnode in self.Pnode_list:
#            pnodes.append(pnode.__str__())
        if self.input == 1:
            return f"Onode: N:{self.number}, I"
        else :
            return f"Onode: N:{self.number}, O"
    
class Gnode:
    def __init__(self, node_list): # node_list should contain all the Pnode and Onode from the grid
        self.Node_list = node_list
        color_s = set()
        Pnode_list = []
        Onode_list = []
        for n in node_list:
            if isinstance(n, Pnode):
                color_s.add(n.color)
                Pnode_list.append(n)
            elif isinstance(n, Onode):
                Onode_list.append(n)
        self.color = color_s
        self.Pnode_list = Pnode_list
        self.Onode_list = Onode_list
        self.coordinate = [0,0]
        self.number = 0
        self.input = 0
        self.output = 0
        self.type = "Gnode"
        self.condition = "Gnode"
        # [get_coordinate(node) for node in get_center_nodes]       ## questionable # do we need coornidate for Gnode?
    def __str__(self):
        if self.input == 1:
            return f"Gnode: N:{self.number}, I"
        else :
            return f"Gnode: N:{self.number}, O"

class Vnode:
    def __init__(self, Gnode1, Gnode2): # node_list should contain all the Pnode and Onode from the grid
        self.Gnode_list = [Gnode1, Gnode2]
        self.type = "Vnode"
        self.input = 0
        self.output = 0
        self.color = Gnode1.color.union(Gnode2.color)
        self.Onode_list = [node for node in Gnode1.Onode_list] + [node for node in Gnode2.Onode_list]
        self.Pnode_list = [node for node in Gnode1.Pnode_list] + [node for node in Gnode2.Pnode_list]
    def __str__(self):
        return f"Vnode"
    



	

# EXAMPLE CODE for node design ########################################################

# class Pnode():
# 		def __init__(self, grid):
# 				# DSL that only requires one argument -> self pointing edge == features of pixel
# 				# each pixel represented like [[....[color, (coordx, coordy)]]]
# 				self.color = get_color(pixel) # -> grid[0][0][0] 
# 				self.coord = get_coord(pixel) # -> grid[0][0][1]
				
# 				# characteristic that could be found in pixel-wise observation
# 				# self.diff_color_neighbors = get_diff_color
				
# class Onode():
# 		def __init__(self, grid):
# 				# DSLs that only requires one argument -> self pointing edge == features of object
# 				self.color = get_color(grid) # -> (0, 1, 2, 5, 6)
# 				self.single_colored = is_single_color(grid) # -> False
# 				self.coord_list = get_coord_list(grid) # -> [(0,0), (0,1), ... (8,8)]
# 				self.relative_coord = get_relative_coord(grid) # -> [(0,0), (0,1), ... (8,8)]
# 				self.size = get_size(grid) # -> (9, 9)
# 				self.height = get_height(grid) # -> 9
# 				self.width = get_width(grid) # -> 9
# 				...
# 				self.hori_symm = is_hori_symmetric(grid) # -> True
# 				self.verti_symm = is_verti_symmetric(grid) # -> True
# 				self.rectangle = is_rectangle(grid) # -> True
# 				self.square = is_square(grid) # -> True
# 				...
# 				self.bbox = get_bbox(grid) # -> [(0,0), (9,9)]
# 				# conditional characteristic
# 				if self.rectangle:
# 						self.corner_list = get_corner_list() # corner
# 						self.edge_list = get_edge_list(grid) # edge
# 						self.margin_list = get_margin_list(grid) # margin(ring shape)
# 						self.inner_list = get_inner_list(grid) # nonmargin
# 						self.center_of_mass = get_center_of_mass(grid) # four types of center of mass expression
# 				...
				
# 				self.shape = get_shape(grid) # can be unique besides square, bar, cross, ring # need definition
				
# class Gnode():
# 		def __init__(self, grid):
# 				self.color = get_color(grid) # -> (0, 1, 2, 5, 6)
# 				self.single_colored = is_single_color(grid) # -> False
# 				self.size = get_size(grid) # -> (9, 9)
# 				self.height = get_height(grid) # -> 9
# 				self.width = get_width(grid) # -> 9
# 				...
				
# 				# a lot overlaping with Onode characteristics cuz Gnode is just a one kind of Onode.
				
				
# class Vnode():
# 		# Should Vnode take two grids or only one for node construction?
# 		def __init__(self, inpt_grid, output_grid): # OR (self, grid)
# 				# and what can be its characteristic?
# 				self.
				



if __name__ == "__main__":
	print("this is node definition file")