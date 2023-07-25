""" Program to do connectedness testing on random graphs of various
    sizes.
    Author/copyright: Duncan Buell.  All rights reserved.
    Date: 3 December 2022
"""
#import sys
import random
from collections import defaultdict
import graphlib

#123456789 123456789 123456789 123456789 123456789 123456789 123456789
######################################################################
def main():
    """ Main program for testing connectedness on random graphs.
        This uses BFS to determine if the graph is connected.
    """
    random.seed(10)

    # 'probtimes' is the percent probability of a random arc
    probtimesupper = 30
    trial_count = 10

    node_count_lower = 50
    node_count_upper = 1001

    node_count_lower = 10
    node_count_upper = 25

    #  Outer loop on probability of connections.
    #      Next loop on number of nodes.
    #          Then loop on number of trials.
    for probtimes100 in range(probtimesupper, 0, -1):
        prob = probtimes100/100.0
        for node_count in range(node_count_lower, node_count_upper, 1):
            connected = trial_count
            for trial in range(trial_count):
                the_dict, matrix = graphlib.generate_graph(node_count, prob)
                graphlib.print_dict(the_dict)
                unvisited = []
                for sub in range(node_count):
                    unvisited.append(sub)
#                sss = f'TEST {node_count:8d} {prob:10.4f} {str(unvisited)}'
#                print(sss)


                visited = defaultdict(int)
                for key in the_dict.keys():
                    visited[key] = 0

                #  Do a BFS on the graph.
                start_node = unvisited[0]
                unvisited = graphlib.bfs(start_node, visited, the_dict, 1)

                # If any nodes are not yet visited, the graph is not
                # connected, and we decrement our counter.
                if unvisited != []:
                    sss = f'UNCONNECTED {trial:4d} {node_count:8d}'
                    sss += f' {int(probtimes100):8d} {str(sorted(unvisited))}'
                    print(sss)
                    connected -= 1
                else:
                    sss = f'CONNECTED   {trial:4d} {node_count:8d}'
                    sss += f' {int(probtimes100):8d} {str(sorted(unvisited))}'
                    print(sss)

            sss = 'CONNCOUNT   (NODES, PROB, TRIALS, NUMCONN)'
            sss += f' {node_count:4d} {int(probtimes100):8d}'
            sss += f' {trial_count:6d} {connected:6d}'
            if connected != trial_count:
                sss += ' ZORK'
            print(sss)

######################################################################
main()
