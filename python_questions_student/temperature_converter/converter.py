"""
Temperature Converter Problem

Objective:
Create a function that converts between Celsius, Fahrenheit and Kelvin.

Requirements:
1. Support conversions between all three scales:
   - Celsius ↔ Fahrenheit
   - Celsius ↔ Kelvin  
   - Fahrenheit ↔ Kelvin
2. Input: (value, from_scale, to_scale)
3. Return converted value rounded to 2 decimal places
4. Handle invalid scale inputs gracefully

Conversion Formulas:
- C to F: (C × 9/5) + 32
- F to C: (F - 32) × 5/9
- C to K: C + 273.15
- K to C: K - 273.15
"""

def convert_temperature(value, from_scale, to_scale):
    """
    Convert temperature between Celsius, Fahrenheit and Kelvin
    
    Args:
        value (float): Temperature value to convert
        from_scale (str): Original scale ('C', 'F' or 'K')
        to_scale (str): Target scale ('C', 'F' or 'K')
        
    Returns:
        float: Converted temperature value
        None: If invalid scale provided
    """
    # TODO: Implement temperature conversion
    pass
