from bank import value

def test_with_lower_case():
    assert value("Hello World") == 0

def test_with_upper_case():
    assert value("Hi Maruf") == 20

def test_with_number():
    assert value("1234") == 100