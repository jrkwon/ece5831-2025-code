# %% [markdown]
# # Logic Gate 
# 
# by Jaerock Kwon


# ## Logic Gate class

# %%
class LogicGate:
    def __init__(self): #, w1, w2, theta):
        #self.w1 = w1
        #self.w2 = w2
        #self.theta = theta
        pass


    def _is_over_threshold(self, tmp, theta):
        return 1 if tmp > theta else 0


    def and_gate(self, x1, x2):
        w1, w2, theta = 0.5, 0.2, 0.6
        return self._is_over_threshold(x1 * w1 + x2 * w2, theta)


    def nand_gate(self, x1, x2):
        w1, w2, theta = -0.5, -0.2, -0.6
        return self._is_over_threshold(x1 * w1 + x2 * w2, theta)


    def or_gate(self, x1, x2):
        w1, w2, theta = 2, 2, 1.8
        return self._is_over_threshold(x1 * w1 + x2 * w2, theta)


    def nor_gate(self, x1, x2):
        w1, w2, theta = -2, -2, -1.8
        return self._is_over_threshold(x1 * w1 + x2 * w2, theta)


    def test(self):
        inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
        for input in inputs:
            print(f'{input[0]} AND {input[1]} = {self.and_gate(input[0], input[1])}')
        
        for input in inputs:
            print(f'{input[0]} NAND {input[1]} = {self.nand_gate(input[0], input[1])}')
        
        for input in inputs:
            print(f'{input[0]} OR {input[1]} = {self.or_gate(input[0], input[1])}')
        
        for input in inputs:
            print(f'{input[0]} NOR {input[1]} = {self.nor_gate(input[0], input[1])}')   




if __name__ == "__main__":
    print("This is a logic gate module written by Jaerock Kwon.")

