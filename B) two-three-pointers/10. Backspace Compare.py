"""
Given two strings containing backspaces (identified by the character #), check if the two strings are equal.


Input: str1="xy#z", str2="xzz#"
Output: true
Explanation: After applying backspaces the strings become "xz" and "xz" respectively.

Input: str1="xy#z", str2="xyz#"
Output: false
Explanation: After applying backspaces the strings become "xz" and "xy" respectively.

Input: str1="xp#", str2="xyz##"
Output: true
Explanation: After applying backspaces the strings become "x" and "x" respectively.
In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.

Input: str1="xywrrmp", str2="xywrrmu#p"
Output: true
Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.
"""
def backspace_compare(str1, str2):
  s1, s2 = [], []
  for i in range(len(str1)):
    if s1 and str1[i] == '#':
      s1.pop()
    else:
      s1.append(str1[i])

  for i in range(len(str2)):
    if s2 and str2[i] == '#':
      s2.pop()
    else:
      s2.append(str2[i])

  return set(s1) == set(s2)

assert backspace_compare(str1="xy#z", str2="xzz#") == True
assert backspace_compare(str1="xy#z", str2="xyz#") == False
assert backspace_compare(str1="xp#", str2="xyz##") == True
assert backspace_compare(str1="xywrrmp", str2="xywrrmu#p") == True
print("all tests past!")