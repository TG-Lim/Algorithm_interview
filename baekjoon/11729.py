class Hanoi:
    def __init__(self):
        self.process = []

    def function_a(self, n):
        # 1-> 2
        if n == 1:
            self.process.append('1 2')
        if n >= 2:
            self.function_b(n-1) # 1 -> 3
            self.function_a(1) # 1 -> 2
            self.function_f(n-1) # 3 -> 2

    def function_b(self, n):
        # 1-> 3
        if n == 1:
            self.process.append('1 3')
        if n >= 2:
            self.function_a(n-1) # 1 -> 2
            self.function_b(1) # 1 -> 3
            self.function_e(n-1) # 2 -> 3

    def function_c(self, n):
        # 2 -> 1
        if n == 1:
            self.process.append('2 1')
        if n >= 2:
            self.function_e(n-1) # 2 -> 3
            self.function_c(1) # 2 -> 1
            self.function_d(n-1) # 3 -> 1

    def function_d(self, n):
        # 3 -> 1
        if n == 1:
            self.process.append('3 1')
        if n >= 2:
            self.function_f(n-1) # 3 -> 2
            self.function_d(1) # 3 -> 1
            self.function_c(n-1) # 2 -> 1

    def function_e(self, n):
        # 2 -> 3
        if n == 1:
            self.process.append('2 3')
        if n >= 2:
            self.function_c(n-1) # 2 -> 1
            self.function_e(1) # 2 -> 3
            self.function_b(n-1) # 1 -> 3

    def function_f(self, n):
        # 3 -> 2
        if n == 1:
            self.process.append('3 2')
        if n >= 2:
            self.function_d(n-1) # 3 -> 1
            self.function_f(1) # 3 -> 2
            self.function_a(n-1) # 1 -> 2

n = int(input())
hanoi = Hanoi()
hanoi.function_b(n)
print(len(hanoi.process))
print('\n'.join(hanoi.process))