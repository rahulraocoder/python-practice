from converter import convert_temperature

def test_celsius_conversions():
    assert convert_temperature(0, 'C', 'F') == 32.0
    assert convert_temperature(100, 'C', 'F') == 212.0
    assert convert_temperature(0, 'C', 'K') == 273.15
    assert convert_temperature(-273.15, 'C', 'K') == 0.0

def test_fahrenheit_conversions():
    assert convert_temperature(32, 'F', 'C') == 0.0
    assert convert_temperature(212, 'F', 'C') == 100.0
    assert convert_temperature(32, 'F', 'K') == 273.15

def test_kelvin_conversions():
    assert convert_temperature(273.15, 'K', 'C') == 0.0
    assert convert_temperature(373.15, 'K', 'F') == 212.0

def test_invalid_scales():
    assert convert_temperature(0, 'X', 'C') is None
    assert convert_temperature(0, 'C', 'X') is None
    assert convert_temperature(0, 'F', 'F') == 0.0  # Same scale
