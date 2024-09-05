# Previous version of edge definition #########################################

class Edge:
    def __init__(self, tag, node1, node2 = None):
        if node2 == None :
            self.node_set = [node1]
        else :
            self.node_set = [node1, node2]
        self.tag = tag       
    def __str__(self):
        n_set = []
        for n in self.node_set:
            n_set.append(n.__str__())
        return f"{n_set, self.tag}"    
    
if __name__ == "__main__":
    print("Edge class definition")