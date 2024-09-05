

# functions that are used to construct KG
# like make node list and node, make edge list and edge
# in construct_KG function, each function is called in order

def Make_NodeList (grid):     ## this function now generate Pnode list from grid
    node_list = []
    if type(grid[0]) == list :
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp_node = Pnode(grid, i, j)
                temp_node.color = grid[i][j]
                node_list.append(temp_node)
    return node_list

def Concat_node_list (node_list1, node_list2):
    return node_list1 + node_list2

def Make_Onode (node_list, color_same, dist_dsl, edge_list):
    condition = []
    def edge_list_to_graph(edges):
        graph = {}
        for edge in edges:
            node1, node2 = edge.node_set
            if node1 not in graph:
                graph[node1] = []
            if node2 not in graph:
                graph[node2] = []
            graph[node1].append(node2)
            graph[node2].append(node1)
        return graph
    
    if color_same == True:
        same_color = lambda x1, x2 : True if x1.color == x2.color else False
        node_list1 = node_list
        condition.append("single_color")
    else :
        same_color = lambda x1, x2 : True
        condition.append("multi_color")
        node_list1 = get_background_color_removed(node_list)
    if dist_dsl != None:
        dist_1 = lambda x1, x2 : True if dist_dsl(x1, x2) == 1 else False
        condition.append(dist_dsl.__name__)
    else :
        dist_1 = lambda x1, x2 : True
        condition.append("no_distance")
    same_color_and_dist1 = lambda x1, x2: True if (same_color(x1,x2) == True and dist_1(x1,x2) == True) else False
    s_d_edge_list = Make_edge_list(node_list1, same_color_and_dist1)
    graph = edge_list_to_graph(s_d_edge_list)

    condition = tuple(condition)
    tag = ("get_onode", condition)

    for node in node_list1:
        # if isinstance(node, Onode):
        #     continue
        if node not in graph.keys():
            graph[node] = []
    
    def cluster_graph(graph):
        clusters = []
        visited = set()

        def dfs(node, cluster):
            visited.add(node)
            cluster.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, cluster)

        for node in graph:
            if node not in visited:
                new_cluster = set()
                dfs(node, new_cluster)
                clusters.append(new_cluster)
                
        return clusters

    clusters = cluster_graph(graph)

    Onode_list = []
    # tag = ("get_onode", None)
    for obj in clusters:
        onode = Onode(obj, condition)
        Onode_list.append(onode)
        for pnode in obj:
            e = Edge(tag, pnode, onode)
            edge_list.append(e)



    return Onode_list, edge_list 

def Make_Gnode (node_list, edge_list):
    gnode = Gnode(node_list)
    gnode_list = []
    tag = ("get_gnode", None)
    for node in node_list:
        e = Edge(tag, gnode, node)
        edge_list.append(e)
    gnode_list.append(gnode)
    return node_list + gnode_list, edge_list

def Make_Vnode (node_list, edge_list):
    gnode_list = []
    for n in node_list:
        if isinstance(n, Gnode):
            gnode_list.append(n)
    assert len(gnode_list) == 2
    vnode = [Vnode(gnode_list[0], gnode_list[1])]
    tag = ("get_vnode", None)
    e1 = Edge(tag, vnode[0], gnode_list[0])
    e2 = Edge(tag, vnode[0], gnode_list[1])
    edge_list.append(e1)
    edge_list.append(e2)
    return node_list + vnode, edge_list

def create_edge_list ():
    return []


    
def create_edge (get_dsl, node1, node2):   ## no self connecting edge
    is_dsl = get_to_is(get_dsl) 
    result = is_dsl(node1, node2)   ## result = (bool (dsl_name, taget))
    if result[0] == False :
        return None
    else :
        tag = result[1]
        edge = Edge(tag, node1, node2)
        return edge



def Make_edge_list (node_list, dsl) :
    edge_list = create_edge_list()
    try :
        if isinstance (dsl(node_list[0]), bool) == True: ## dsl is is_dsl with only one param
            # print("dsl is returning bool type with 1 param")
            tag = (dsl.__name__, None)
            for n1 in node_list:
                if dsl(n1) == True :
                    e = Edge(tag, n1, n1)
                    edge_list.append(e)
            return edge_list
        else :
            pass
    except :
        pass
    try :
        if isinstance (dsl(node_list[0], node_list[0]), bool) == True : ## dsl is is_dsl with two param
            # print("dsl is returning bool type with 2 param")
            tag = (dsl.__name__, None)
            for n1 in node_list:
                for n2 in node_list:
                    if dsl(n1, n2) == True and n1 != n2 :
                        e = Edge(tag, n1, n2)
                        edge_list.append(e)
            return edge_list
    except: 
        pass
    ## dsl is get_dsl
    # print("dsl is get_dsl")
    for n1 in node_list:
        for n2 in node_list:
            e = create_edge(dsl, n1, n2)
            if e != None and n1 != n2:
                edge_list.append(e)
                # print(e)
    return edge_list

def Concat_edge_list (edge_list1, edge_list2):
    return edge_list1 + edge_list2


def construct_KG (grid, dsl_list):
    node_list = Make_NodeList(grid)
    edge_list = create_edge_list()
    for dsl in dsl_list:
        edge_list = Make_edge_list(node_list, dsl)
    node_list, edge_list = Make_Gnode(node_list, edge_list)
    node_list, edge_list = Make_Vnode(node_list, edge_list)
    node_list, edge_list = Make_Onode(node_list, True, None, edge_list)
    return node_list, edge_list