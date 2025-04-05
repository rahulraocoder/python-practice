from calculator import SimpleCalculator

def test_basic_operations():
    calc = SimpleCalculator()
    assert calc.calculate(5, '+', 3) == 8
    assert calc.calculate(10, '-', 4) == 6
    assert calc.calculate(3, '*', 7) == 21
    assert calc.calculate(10, '/', 2) == 5
    assert calc.calculate(2, '**', 3) == 8
    assert calc.calculate(10, '%', 3) == 1

def test_error_handling():
    calc = SimpleCalculator()
    assert calc.calculate(5, '/', 0) is None  # Division by zero
    assert calc.calculate(5, 'x', 3) is None  # Invalid operator
    assert calc.calculate('a', '+', 1) is None  # Invalid number

def test_history():
    calc = SimpleCalculator()
    calc.calculate(1, '+', 1)
    calc.calculate(2, '*', 2)
    assert len(calc.get_history()) == 2
    assert ('1 + 1', 2) in calc.get_history()
