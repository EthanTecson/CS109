""" Module to do graph computations, including depth-first and
    breadth-first search.
    Author/copyright: Duncan Buell.  All rights reserved.
    Date: 20 November 2022
"""
#import sys
import random
from collections import defaultdict

#123456789 123456789 123456789 123456789 123456789 123456789 123456789
######################################################################
def bfs(start, visited, the_dict, component):
    """ Do BFS from 'start'.
        Parameters:
            start: the vertext to start from
            the_dict: the dict of the graph adjacencies
        Return value:
            none
    """
    sss = f'\nENTER BFS  {start} FOR COMP {component} AND VERTICES {str(the_dict[start])}'
    print(sss)
    sss = f'STATUS BFS {print_status(visited, the_dict)}'
    print(sss)
    queue = []
    visited[start] = component
    queue.append(start)
    sss = f'QUEUE BFS {str(queue)}'
    print(sss)
    sss = f'STATUS BFS {print_status(visited, the_dict)}'
    print(sss)
    while len(queue) != 0:
        vertex = queue[0]
        queue = queue[1:]
        visited[vertex] = component
        sss = f'\nVX AND QUEUE {vertex} {str(queue)}'
        print(sss)
        key = f'{vertex:>4s}'
        sss = f'\nVX DICT {key} {str(the_dict[key])}'
        print(sss)
#        for next_vertex in the_dict[vertex]:
        for next_vertex in the_dict[key]:
            sss = f'NEXT VX  {next_vertex} {str(queue)}'
            print(sss)
            if visited[next_vertex] == 0:
                visited[next_vertex] = component
                queue.append(next_vertex)
                sss = f'ADDED VX {next_vertex} {str(queue)}'
                print(sss)

    # Now do a new list of nodes that still need visiting.
    nodes_to_visit = []
    for node, vis in visited.items():
        if vis == 0:
            nodes_to_visit.append(node)

    return sorted(nodes_to_visit)

######################################################################
def compute_components(the_dict):
    """ Return the number of connected components.
        Parameters:
            visited: the dict of node->visited values
        Return:
            the number of connected components
    """
    node_count = len(the_dict.keys())
    visited = defaultdict(int)
    for key in the_dict.keys():
        visited[key] = 0

    component = 1
    start_node = get_start(visited)
    print('START FROM TOP', start_node)
    while start_node is not None:
#       print('TOP', unvisited)
        #  Do a BFS on the graph.
#       print('UNB', unvisited)
#       start_node = unvisited[0]
        unvisited = bfs(start_node, visited, the_dict, component)
#       print('UNVISITEDA', unvisited)

        if unvisited != []:
            sss = f'UNVISITEDB {node_count:8d} {str(sorted(unvisited))}'
            print(sss)
            component += 1
            sss = f'COMPONENT NOW {component:8d}'
            print(sss)

        max_comp = max(visited.values())
        for comp in range(1, max_comp+1):
            the_comp = []
            for node in sorted(the_dict.keys()):
                if visited[node] == comp:
                    the_comp.append(node)
            sss = f'COMPONENT {comp:4d}: {node_count:8d} {str(the_comp)}'
            print(sss)
            print()

        start_node = get_start(visited)
        print('START FROM BOT', start_node, ' FOR COMP', component)

    return component

######################################################################
def compute_degrees(the_dict):
    """ Compute, print, and plot the histogram of degrees of nodes
        Parameters:
            visited: the dict of node->visited values
        Return:
            none
    """
    degrees = defaultdict(int)
    for node, links in the_dict.items():
        degree = len(links)
        degrees[degree] += 1

    for degree, freq in sorted(degrees.items()):
        print(f'FREQ {degree:5d} {freq:6d}')

######################################################################
def create_cross_refs(the_list):
    """ Create the cross ref dicts for the header line.
        Parameters:
            the_list: the list of node labels
        Return value:
            xrefvxtosub: the cheatsheet of subscripts for the vertices
            xrefsubtovx: the cheatsheet of subscripts for the vertices
    """
    xrefsubtovx = defaultdict(str)
    xrefvxtosub = defaultdict(int)
    for sub, vertex in enumerate(the_list):
        key = f'{vertex:>4s}'
        xrefsubtovx[sub] = key
        xrefvxtosub[key] = sub

    return xrefsubtovx, xrefvxtosub

######################################################################
def create_matrix(the_dict, xrefvxtosub):
    """ Create an adjacency matrix from a dictionary listing arcs.
        Parameters:
            the_dict:    the dictionary from which to create the matrix
            xrefvxtosub: the cheatsheet of subscripts for the vertices
        Return value:
            the matrix
    """
    mat_size = len(the_dict.keys())
    matrix = []
    for row_sub in range(mat_size):
        row = [0] * mat_size
        matrix.append(row)

    for vertex, arc_list in sorted(the_dict.items()):
        for arc in arc_list:
            row_sub = xrefvxtosub[vertex]
            col_sub = xrefvxtosub[arc]
            matrix[row_sub][col_sub] = 1
            matrix[col_sub][row_sub] = 1

    return matrix

######################################################################
def dfs(start, visited, the_dict, component):
    """ Do DFS from 'start'.
        Parameters:
            start: the vertext to start from
            the_dict: the dict of the graph adjacencies
        Return value:
            none
    """
    sss = f'\nENTER DFS  {start} AND VERTICES {str(the_dict[start])}'
    print(sss)
    sss = f'STATUS DFS {print_status(visited, the_dict)}'
    print(sss)
    visited[start] = component
    for vertex in the_dict[start]:
        sss = f'VISITED? {vertex} {visited[vertex]}'
        print(sss)
        if visited[vertex] == 0:
            dfs(vertex, visited, the_dict, component)
            sss = f'\nRETURN DFS {start} AND VERTICES {str(the_dict[start])}'
            print(sss)
            sss = f'STATUS DFS {print_status(visited, the_dict)}'
            print(sss)

#    # Now do a new list of nodes that still need visiting.
#    nodes_to_visit = []
#    for node, vis in visited.items():
#        if vis == 0:
#            nodes_to_visit.append(node)
#
#    return sorted(nodes_to_visit)

######################################################################
def generate_graph(how_many_nodes, connectedness):
    """ This generates a random graph and produces an adjacency
        matrix and an adjacency dictionary.
        Parameter:
            how_many_nodes: the number of nodes
            connectedness:  the percent likelihood of connecting
        Returns:
            the dictionary and the matrix
    """
    # In this case we have to initialize 'graph_dict' so all
    # the keys will exist.
    graph_dict = defaultdict(set)
    for node1 in range(how_many_nodes):
        graph_dict[node1] = set()

    for node1 in range(how_many_nodes):
        for node2 in range(node1+1, how_many_nodes):
            conn = random.random()
#            yes_conn = False
            if conn < connectedness:
                graph_dict[node1].add(node2)
                graph_dict[node2].add(node1)
#                yes_conn = True
#            sss = f'GENERATE {node1:5d} {node2:5d} {conn:10.4f} {connectedness:10.4f} {yes_conn}'
#            print(sss)

#    for node in range(how_many_nodes):
#        sss = f'FROMGEN {how_many_nodes:4d} {connectedness:10.4f}'
#        sss += f' {node:4d} {str(sorted(graph_dict[node]))}'
#        print(sss)
    headerlist = []
    for nnn in range(how_many_nodes):
        headerlist.append(nnn)
    xrefsubtovx, xrefvxtosub = create_cross_refs(headerlist)
    for key, value in sorted(xrefsubtovx.items()):
        print('SUBTOVX', key, value)
    for key, value in sorted(xrefvxtosub.items()):
        print('VXTOSUB', key, value)

    adj_matrix = create_matrix(graph_dict, xrefvxtosub)

    return graph_dict, adj_matrix

######################################################################
def get_start(visited):
    """ Get the first instance of an unvisited node.
        Parameters:
            visited: the 'visited' dictionary to be searched
        Return value:
            the node to visit next as a start node
    """
    for node, component in sorted(visited.items()):
#        print('GET', node, component)
        if component == 0:
            return node

    return None

######################################################################
def isconnected(visited):
    """ Print an adjacency dictionary.
        Parameters:
            visited: the 'visited' dictionary to be searched
        Return value:
            True or False
    """
    for key, value in sorted(visited.items()):
        sss = f'ISCONN {key:>4s} {str(value)}'
        print(sss)
    values = visited.values()

    if 0 in values:
        return False
    return True

######################################################################
def print_dict(the_dict):
    """ Print an adjacency dictionary.
        Parameters:
            the_dict: the dictionary to be printed
        Return value:
            none
    """
    #  Print the dictionary so we can verify we read correctly.
    for vertex, arc_list in sorted(the_dict.items()):
        sss = f'DICT {str(vertex):>4s} {str(arc_list)}'
        print(sss)

######################################################################
def print_matrix(matrix, xrefsubtovx):
    """ Pretty print an adjacency matrix.
        We assume a square matrix.
        Parameters:
            matrix: the matrix to be printed
        Return value:
            none
    """
    mat_size = len(matrix)
    # top line of labels
    sss = 'MATRIX          '
    for col_sub in range(mat_size):
        outvalue = str(xrefsubtovx[col_sub])
        sss += f'{outvalue:>4s}'

    # top line of subscripts
    print(sss)
    sss = 'MATRIX          '
    for col_sub in range(mat_size):
        sss += f'{col_sub:4d}'
    print(sss)

    # dots to separate header from matrix
    sss = 'MATRIX          '
    for col_sub in range(mat_size):
        sss += f'{"..":>4s}'
    print(sss)

    for row_sub, row in enumerate(matrix):
        outvalue = str(xrefsubtovx[row_sub])
        sss = f'MATRIX{outvalue:>4s}{row_sub:4d}: '
        for col_sub in range(mat_size):
            sss += f'{row[col_sub]:4d}'
        print(sss)

######################################################################
def print_status (visited, the_dict):
    """ Print the vertices and their visited status in one string.
        Parameters:
            visited:  a list of the visited status
            the_dict: the dictionary representing the graph
        Return value:
            the stringified version of vertices and visitedness
    """
    sss = ''
    for vertex in sorted(the_dict.keys()):
        sss += f' ({vertex} {visited[vertex]})'

    return sss

######################################################################
def read_facebook(filename):
    """ This is the main program for doing depth-first and
        breadth-first search on a graph.
    """
    face_dict = defaultdict(list)
    with open(filename) as infile:
        for line in infile:
            line = line.strip()
            lsplit = line.split()
            if len(lsplit) > 0:
                fromnode = f'{lsplit[0]:>4s}'
                tonode = f'{lsplit[1]:>4s}'
                face_dict[fromnode].append(tonode)
                face_dict[tonode].append(fromnode)
#                print('ADD TO', fromnode, ' LINK', tonode)

#    for fromnode, tonodes in sorted(face_dict.items()):
#        print('FROM', fromnode, ' TO', tonodes)

    return face_dict

######################################################################
def read_graph(filename):
    """ This reads a graph and produces an adjacency matrix and an
        adjacency dictionary.
        Data is assumed to be one vertex per line, with the first
            value in the line being the relevant vertex and the
            rest of the line being the adjacent vertices.
        Parameter:
            filename: the filename from which to read
        Returns:
            both the dictionary and the matrix
    """
    #  Read the file into a list of lines.
    with open(filename, encoding='utf-8') as infile:
        the_list = []
        for line in infile:
            the_list.append(line.strip())

    #  Parse the list and create the dictionary.
    first_line = True
    the_dict = defaultdict(list)
    for line in the_list:
        line = line.strip()
        lsplit = line.split()
        if first_line:
            xrefsubtovx, xrefvxtosub = create_cross_refs(lsplit)
            first_line = False
#            for key, value in sorted(xrefsubtovx.items()):
#                sss = f'SUBTOVX {key:4d} {value:>4s}'
#                print(sss)
#            for key, value in sorted(xrefvxtosub.items()):
#                sss = f'VXTOSUB {key:>4s} {value:4d}'
#                print(sss)

#        print('BEFORE', lsplit)
        lsplit = list(lsplit)
#        print('AFTERA', lsplit)
        for sub, item in enumerate(lsplit):
            new_item = f'{item:>4s}'
            lsplit[sub] = new_item
#        print('AFTERB', lsplit)
        the_dict[lsplit[0]] = []
        if len(lsplit) > 1:
            the_dict[lsplit[0]] = lsplit[1:]

#    #  Print the dictionary so we can verify we read correctly.
#    for vertex, arc_list in sorted(the_dict.items()):
#        print(vertex, arc_list)

    adj_matrix = create_matrix(the_dict, xrefvxtosub)
#    print_matrix(adj_matrix, xrefsubtovx, xrefvxtosub)
#    print()


    return the_dict, adj_matrix, xrefsubtovx, xrefvxtosub
