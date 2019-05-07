import random

class Solution(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.rows = n_rows
        self.cols = n_cols
        self.rand = random.randrange(n_rows * n_cols)
        self.reset()


    def flip(self):
        """
        :rtype: List[int]
        """
        print(self.rand)
        r = self.rand // self.cols
        c = self.rand % self.cols - 1
        if c < 0:
            r -= 1
            c = self.cols - 1
        self.matrix[r][c] = 1
        return [r,c]


    def reset(self):
        """
        :rtype: None
        """
        self.matrix = [[0] * self.cols] * self.rows

# Your Solution object will be instantiated and called as such:
obj = Solution(5, 3)
print(obj.matrix)
print(obj.flip())
# obj.reset()
