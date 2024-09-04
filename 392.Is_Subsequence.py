class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0

        # loop string s
        for i in s:
            # boundary condition
            if index >= len(t):
                return False

            # otherwise, continue to search for the next i
            if t[index:].find(i) != -1:
                index += t[index:].find(i)
            else:
                return False

            index += 1

        return True
