"""
Simple Calculator Problem

Objective:
Create a calculator that supports:
- Addition (+)
- Subtraction (-) 
- Multiplication (*)
- Division (/)
- Power (**)
- Modulus (%)

Requirements:
1. Handle basic arithmetic operations
2. Validate inputs (numbers and operators)
3. Handle division by zero
4. Return both result and calculation history
"""

class SimpleCalculator:
    def __init__(self):
        self.history = []

    def calculate(self, num1, operator, num2):
        """
        Perform calculation and store result in history
        
        Args:
            num1 (float): First number
            operator (str): Math operator
            num2 (float): Second number
            
        Returns:
            float: Calculation result
            None: If invalid input or operation
        """
        # TODO: Implement calculator
        pass

    def get_history(self):
        """Return list of past calculations"""
        return self.history
