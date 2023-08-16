def compare_dicts(dict1, dict2):
    if set(dict1.keys()) == set(dict2.keys()):
        for key in dict1:
            if dict2[key] < dict1[key]:
                return False
        return True
    else:
        return False


def min_window(s, t):
    left = 0
    freq, t_freq = {}, {}
    for ch in t:
        t_freq[ch] = t_freq.get(ch,0) + 1
    min_substr = s
    for right in range(len(s)):
        if s[right] in t_freq:
            freq[s[right]] = freq.get(s[right],0) + 1
        while compare_dicts(t_freq, freq):
            if len(min_substr) > len(s[left:right + 1]):
                min_substr = s[left:right + 1]
            if s[left] in freq:
                v = freq.get(s[left],0)
                v = max(0, v-1)
                freq[s[left]] = v
            left += 1
    return min_substr
        

assert min_window("ABCD","ABC") == "ABC"
assert min_window("ABXYZJKLSNFC", "ABC") == "ABXYZJKLSNFC"
assert min_window("XYZYX" , "XYZ") == "XYZ" #order doesnt matter
print('all tests past!')
