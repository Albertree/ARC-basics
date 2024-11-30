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
    