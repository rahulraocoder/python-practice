from date_validator import validate_date

def test_valid_dates():
    assert validate_date("2023-02-28") == True
    assert validate_date("2020-02-29") == True  # Leap year
    assert validate_date("1999-12-31") == True

def test_invalid_dates():
    assert validate_date("2023-13-01") == False  # Invalid month
    assert validate_date("2023-02-30") == False  # Invalid day
    assert validate_date("23-02-28") == False    # Wrong format
    assert validate_date("2023/02/28") == False  # Wrong format
    
def test_edge_cases():
    assert validate_date("0001-01-01") == True   # Min valid date
    assert validate_date("9999-12-31") == True   # Max valid date
    assert validate_date("2023-00-01") == False  # Invalid month
    assert validate_date("2023-01-00") == False  # Invalid day
