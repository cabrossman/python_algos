"""
    There are N tasks, labeled from 0 to N-1. 
    Each task can have some prerequisite tasks 
    which need to be completed before it can be scheduled. 
    
    Given the number of tasks and a list of prerequisite pairs, 
    find out if it is possible to schedule all the tasks.

    Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
    Output: true
    Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs 
    to finish before '2' can be scheduled. One possible scheduling of tasks is: [0, 1, 2] 

    Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
    Output: false
    Explanation: The tasks have a cyclic dependency, therefore they cannot be scheduled.

    Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
    Output: true
    Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5] 

"""
from collections import deque


def is_scheduling_possible(tasks, prerequisites):
    scheduled_tasks = []
    if tasks <= 0:
        return True
    
    #build graph & count_incoming
    graph = {i: [] for i in range(tasks)}
    cnt_incoming = {i : 0 for i in range(tasks)}

    #populate graphs
    for prereq in prerequisites:
        parent, child = prereq
        graph[parent].append(child)
        cnt_incoming[child] += 1

    #get tasks without dependancies
    # assumes some tasks have no dependancies
    sources = deque()
    for node, incoming in cnt_incoming.items():
        if incoming == 0:
            sources.append(node)


    #order tasks
    while sources:
        node = sources.popleft()
        scheduled_tasks.append(node)
        for child_node in graph[node]:
            cnt_incoming[child_node] -= 1
            if cnt_incoming[child_node] == 0:
                sources.append(child_node)
    
    return len(scheduled_tasks) == tasks


assert is_scheduling_possible(3, [[0, 1], [1, 2]]) == True
assert is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]]) == False
assert is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]]) == True
print('all tests have passed!')