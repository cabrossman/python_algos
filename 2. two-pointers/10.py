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
  s1_idx = len(str1) - 1
  s2_idx = len(str2) - 1

  while s1_idx > 0 or s2_idx > 0:

    s1_c = 0
    s2_c = 0
    while str1[s1_idx - s1_c] == "#":
      s1_c = s1_c + 1
    s1_idx = s1_idx - s1_c*2

    while str2[s2_idx - s2_c] == "#":
      s2_c = s2_c + 1
    s2_idx = s2_idx - s2_c*2

    chr1 = str1[s1_idx]
    chr2 = str2[s2_idx]
    if s1_idx < 0 and s1_idx < 0:
      return True
    if s1_idx < 0 or s2_idx < 0:
      return False
    if chr1 != chr2:
      return False

    s1_idx = s1_idx - 1
    s2_idx = s2_idx - 1 

  return True

assert backspace_compare(str1="xy#z", str2="xzz#") == True
assert backspace_compare(str1="xy#z", str2="xyz#") == False
assert backspace_compare(str1="xp#", str2="xyz##") == True
assert backspace_compare(str1="xywrrmp", str2="xywrrmu#p") == True
print("all tests past!")