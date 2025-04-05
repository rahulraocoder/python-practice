"""
Sales Tax Calculator Problem

Objective:
Calculate total price after tax given:
- Base price (float)
- State code (2 letters)
- Category (food/electronics/clothing/other)

Tax Rules:
- Food: no tax
- Electronics: 8% + $5 surcharge
- Clothing: 4% (no tax if price < $100)
- Other: 6%
- CA has additional 1% tax

Returns total rounded to 2 decimal places
"""

def calculate_total(price, state, category):
    """
    Calculate total price after applying appropriate taxes
    
    Args:
        price (float): Base price
        state (str): 2-letter state code
        category (str): Product category
        
    Returns:
        float: Total price after tax
    """
    # TODO: Implement the tax calculation
    pass
