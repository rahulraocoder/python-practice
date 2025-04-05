from sales_tax import calculate_total

def test_food_items():
    assert calculate_total(100, "NY", "food") == 100
    assert calculate_total(50, "CA", "food") == 50

def test_electronics():
    # Base tax 8% + $5 surcharge
    assert calculate_total(500, "CA", "electronics") == 545  # 500*1.09 + 5
    
def test_clothing():
    # 4% tax only above $100
    assert calculate_total(99, "TX", "clothing") == 99
    assert calculate_total(100, "TX", "clothing") == 104
    
def test_other_category():
    # 6% base tax + 1% for CA
    assert calculate_total(200, "NY", "other") == 212
    assert calculate_total(200, "CA", "other") == 214
