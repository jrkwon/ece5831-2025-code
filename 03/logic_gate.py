# %% [markdown]
# # Logic Gate 
# 
# by Jaerock Kwon


# ## Logic Gate class

# %%
class LogicGate:
    def __init__(self, w1, w2, theta):
        self.w1 = w1
        self.w2 = w2
        self.theta = theta

    def and_gate(self, x1, x2):
        tmp = x1 * self.w1 + x2 * self.w2
        if tmp > self.theta:
            return 1
        return 0




if __name__ == "__main__":
    print("This is a logic gate module written by Jaerock Kwon.")

