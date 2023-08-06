"""
Given a string path, which is an absolute path (starting with a slash '/') 
to a file or directory in a Unix-style file system,
 convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, 
a double period '..' refers to the directory up a level, 
and any multiple consecutive slashes (i.e. '//') are treated as 
a single slash '/'. 
For this problem, any other format of periods such as '...' 
are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.
"""

def cpath(path):
    # Splitting the path string by "/" gives a list of directories
    path = path.split("/")
    stack = []
    for i in path:
        if i == "..":
            if stack: # Going one directory means pop top directory from stack
                stack.pop()
        elif i not in {".",""}: # these represent current directory so ignore
            stack.append(i)
    conoical_path = "/" + "/".join(stack) #joining remaining for chanonical path
    return conoical_path

assert cpath("/home/") == "/home"
assert cpath("/../") == "/"
assert cpath("/home//foo/") == "/home/foo"
assert cpath("/a/./b/../../c/") == "/c"
assert cpath("/a/../../b/../c//.//") == "/c"
assert cpath("/a//b////c/d//././/..") == "/a/b/c"
assert cpath("/home/./.././home/.././../") == "/"
assert cpath("/...") == "/..."
assert cpath("/./../...") == "/..."
assert cpath("/a/b/c/../../../..") == "/"
assert cpath("/a/b/c/../../../../..") == "/"
assert cpath("/a/./b/./c/././../") == "/a/b"
assert cpath("/.././.././../") == "/"
assert cpath("/abc/def/../ghi") == "/abc/ghi"
