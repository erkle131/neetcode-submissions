import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length, width=None) -> int:
        result = 0
        if width is None:
            radius = length
            result = math.pi * (radius ** 2)
            return round(result, 2)
        return length * width
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
