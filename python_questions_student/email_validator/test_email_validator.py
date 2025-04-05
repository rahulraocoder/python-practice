from email_validator import validate_email

def test_valid_emails():
    assert validate_email("user@example.com") == True
    assert validate_email("user.name@domain.co") == True
    assert validate_email("user+tag@example.com") == True

def test_invalid_emails(): 
    assert validate_email("user@.com") == False
    assert validate_email("@domain.com") == False
    assert validate_email("user@domain..com") == False
    assert validate_email("user@example.c") == False

def test_edge_cases():
    assert validate_email("") == False
    assert validate_email("invalid") == False
    assert validate_email("user@domain") == False
