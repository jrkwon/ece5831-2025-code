import numpy as np

class LogicGate:
    def __init__(self):
        pass


    def _is_over_threshold(self, w1, w2, theta, x1, x2):
        x = np.array([x1, x2])
        w = np.array([w1, w2])
        return 1 if np.sum(x*w) - theta > 0 else 0
    

    def and_gate(self, x1, x2):
        w1, w2, theta = 0.5, 0.2, 0.6
        return self._is_over_threshold(w1, w2, theta, x1, x2)


    def nand_gate(self, x1, x2):
        w1, w2, theta = -0.5, -0.2, -0.6
        return self._is_over_threshold(w1, w2, theta, x1, x2)


    def or_gate(self, x1, x2):
        w1, w2, theta = 2, 2, 1.8
        return self._is_over_threshold(w1, w2, theta, x1, x2)


    def nor_gate(self, x1, x2):
        w1, w2, theta = -2, -2, -1.8
        return self._is_over_threshold(w1, w2, theta, x1, x2)
    

    def xor_gate(self, x1, x2):
        s1 = self.nand_gate(x1, x2)
        s2 = self.or_gate(x1, x2)
        y = self.and_gate(s1, s2)
        return y


    def test(self):
        inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
        print('-----')
        for input in inputs:
            print(f'{input[0]} AND {input[1]} = {self.and_gate(input[0], input[1])}')
        
        print('-----')
        for input in inputs:
            print(f'{input[0]} NAND {input[1]} = {self.nand_gate(input[0], input[1])}')
        
        print('-----')
        for input in inputs:
            print(f'{input[0]} OR {input[1]} = {self.or_gate(input[0], input[1])}')
        
        print('-----')
        for input in inputs:
            print(f'{input[0]} NOR {input[1]} = {self.nor_gate(input[0], input[1])}')   

        print('-----')
        for input in inputs:
            print(f'{input[0]} XOR {input[1]} = {self.xor_gate(input[0], input[1])}') 


if __name__ == "__main__":
    print("This is a logic gate module (numpy version) written by Jaerock Kwon.")
