"""
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]
"""

def group(strs):
    """
    iterate through original list
        - sort_s = ''.join(sorted(s))
        - add to hashmap {key : lst}
        return values of hashmap
    """
    d={}
    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s in d:
            d[sorted_s].append(s)
        else:
            d[sorted_s] = [s]
    return list(d.values())

assert group(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
assert group([""]) == [[""]]
assert group(["a"]) == [["a"]]
print('all tests passed!')