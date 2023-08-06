"""
    There are N tasks, labeled from 0 to N-1. 
    Each task can have some prerequisite tasks which need to be 
    completed before it can be scheduled. 
    
    Given the number of tasks and a list of prerequisite pairs, 
    write a method to find the ordering of tasks we should pick to finish all tasks.

    Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
    Output: [0, 1, 2]
    Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs
    to finish before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2] 

    Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
    Output: []
    Explanation: The tasks have a cyclic dependency, therefore they cannot be scheduled.

    Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
    Output: [0 1 4 3 2 5] 
    Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5] 

"""
from collections import deque


def is_scheduling_possible(tasks, prerequisites):
    scheduled_tasks = []
    if tasks <= 0:
        return scheduled_tasks
    
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
    
    return scheduled_tasks


assert is_scheduling_possible(3, [[0, 1], [1, 2]]) == [0, 1, 2]
assert is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]]) == []
assert is_scheduling_possible(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]) == [0, 1, 4, 3, 2, 5]
print('all tests have passed!')