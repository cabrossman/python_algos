"""
Given a string, sort it based on the decreasing frequency of its characters.

Input: "Programming"
Output: "rrggmmPiano"
Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.

Input: "abcbab"
Output: "bbbaac"
Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.

O(K * log K + (N−K) * log K) = O(N log K)
"""

from heapq import heappush, heappop

def find_k_frequent_numbers(letters):

    ### map counter
    m = {}
    for letter in letters:
        m[letter] = m.get(letter,0) + 1

    ## heap to find k largest
    max_heap = []
    for letter, count in m.items():
        heappush(max_heap, (-count, letter))


    ## return most frequent
    sorted_letters = []
    for _ in list(max_heap):
        letter = heappop(max_heap)
        for _ in range(abs(letter[0])):
            sorted_letters.append(letter[1])

    return ''.join(sorted_letters)
    




assert find_k_frequent_numbers('Programming') == 'ggmmrrPaino'
assert find_k_frequent_numbers('abcbab') == 'bbbaac'
print('all tests have passed!')
