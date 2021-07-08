import time as t
from datetime import time
from graph import *
from priority_queue import *


def run(graph, key_node_start, key_node_goal, verbose=False, time_sleep=0):
    if key_node_start not in graph.getNodes() or key_node_goal not in graph.getNodes():
        print('Error: key_node_start \'%s\' or key_node_goal \'%s\' not exists!!' % (
            key_node_start, key_node_goal))
    else:
        # UCS uses priority queue, priority is the cumulative cost (smaller cost)
        queue = PriorityQueue()

        # expands initial node

        # get the keys of all successors of initial node
        keys_successors = graph.getSuccessors(key_node_start)

        # adds the keys of successors in priority queue
        for key_sucessor in keys_successors:
            weight = graph.getWeightEdge(key_node_start, key_sucessor)
            # each item of queue is a tuple (key, cumulative_cost)
            queue.insert((key_sucessor, weight), weight)

        reached_goal, cumulative_cost_goal = False, -1
        while not queue.is_empty():
            # remove item of queue, remember: item of queue is a tuple (key, cumulative_cost)
            key_current_node, cost_node = queue.remove()
            if(key_current_node == key_node_goal):
                reached_goal, cumulative_cost_goal = True, cost_node
                break

            if verbose:
                # shows a friendly message
                if cost_node > 60:
                    hours = int(cost_node)
                    minutes = (cost_node * 60) % 60
                    print('Expands node \'%s\' with cumulative time spent %s:%s ...' %
                          (key_current_node, str(hours), str(minutes)))
                    t.sleep(time_sleep)
                elif cost_node < 10:
                    hours = '00'
                    str_min = str(cost_node)
                    minutes = str_min.zfill(2)
                    print('Expands node \'%s\' with cumulative time spent %s:%s ...' %
                          (key_current_node, hours, minutes))
                    t.sleep(time_sleep)
                else:
                    hours = '00'
                    print('Expands node \'%s\' with cumulative time spent %s:%s ...' %
                          (key_current_node, hours, str(cost_node)))
                    t.sleep(time_sleep)

            # get all successors of key_current_node
            keys_successors = graph.getSuccessors(key_current_node)

            if keys_successors:  # checks if contains successors
                # insert all successors of key_current_node in the queue
                for key_sucessor in keys_successors:
                    cumulative_cost = graph.getWeightEdge(
                        key_current_node, key_sucessor) + cost_node
                    queue.insert((key_sucessor, cumulative_cost),
                                 cumulative_cost)

        if(reached_goal):
            if cumulative_cost_goal > 60:
                hours = int(cumulative_cost_goal)
                minutes = (cumulative_cost_goal * 60) % 60
                print('\nReached goal! Time: %s:%s ...' %
                      (str(hours), str(minutes)))
            elif cost_node < 10:
                hours = '00'
                str_min = str(cumulative_cost_goal)
                minutes = str_min.zfill(2)
                print('\nReached goal! Time: %s:%s ...' %
                      (hours, minutes))
            else:
                hours = '00'
                print('\nReached goal! Time: %s:%s ...' %
                      (hours, str(cumulative_cost_goal)))
        else:
            print('\nUnfulfilled goal.\n')


if __name__ == "__main__":

    # build the graph...

    # adds nodes in the graph
    graph = Graph()
    graph.addNode('S')  # start
    graph.addNode('a')
    graph.addNode('b')
    graph.addNode('c')
    graph.addNode('d')
    graph.addNode('e')
    graph.addNode('f')
    graph.addNode('G')  # goal
    graph.addNode('h')
    graph.addNode('p')
    graph.addNode('q')
    graph.addNode('r')
    # linking the nodes
    graph.connect('S', 'd', time(0, 3, 0))
    graph.connect('S', 'e', time(0, 9, 0))
    graph.connect('S', 'p', time(0, 1, 0))
    graph.connect('b', 'a', time(0, 2, 0))
    graph.connect('c', 'a', time(0, 2, 0))
    graph.connect('d', 'b', time(0, 1, 0))
    graph.connect('d', 'c', time(0, 8, 0))
    graph.connect('d', 'e', time(0, 2, 0))
    graph.connect('e', 'h', time(0, 8, 0))
    graph.connect('e', 'r', time(0, 2, 0))
    graph.connect('f', 'c', time(0, 3, 0))
    graph.connect('f', 'G', time(0, 2, 0))
    graph.connect('h', 'p', time(0, 4, 0))
    graph.connect('h', 'q', time(0, 4, 0))
    graph.connect('p', 'q', time(0, 15, 0))
    graph.connect('r', 'f', time(0, 1, 0))

    run(graph=graph, key_node_start='S',
        key_node_goal='G', verbose=True, time_sleep=2)
