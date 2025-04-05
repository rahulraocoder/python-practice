from password_strength import check_password

def test_strong_password():
    result = check_password("StrongPass1!")
    assert result['strength'] == 'Strong'
    assert result['issues'] == []

def test_medium_password():
    result = check_password("MediumPass1")
    assert result['strength'] == 'Medium'
    assert 'no special char' in result['issues']

def test_weak_password():
    result = check_password("weak")
    assert result['strength'] == 'Weak'
    issues = set(result['issues'])
    assert 'too short' in issues
    assert 'no uppercase' in issues
    assert 'no digit' in issues
    assert 'no special char' in issues
