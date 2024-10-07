class calculator:
    
    @staticmethod
    def sub(a, b):
        return a - b
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multi(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b== 0:
            return "Error: Division by zero is not allowed."
        return round(a / b, 2)

org = 2730000
my_plan = 950000
k = calculator.sub(org, my_plan)
my_use = 1700000
j = calculator.sub(k, my_use)
bonus = 30000
l = calculator.add(j, bonus)
print(l)