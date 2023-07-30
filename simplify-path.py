class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        pa = ""
        for x in path + "/":
            if x == "/":
                if pa == "..":
                    if stack:
                        stack.pop()
                elif pa != "" and pa !=".":
                    stack.append(pa)
                pa = ""
            else:
                pa += x

        return "/" + "/".join(stack)
