from numb3rs import validate

def test_range():
    assert validate(r"127.1.1.1") == True
    assert validate(r"256.21.21.21") == False
    assert validate(r"25.265.21.21") == False
    assert validate(r"25.21.265.21") == False
    assert validate(r"25.21.21.265") == False

def test_format():
    assert validate(r"255.1.1.1") == True
    assert validate(r"255.1.1") == False
    assert validate(r"25.1") == False
    assert validate(r"56") == False
