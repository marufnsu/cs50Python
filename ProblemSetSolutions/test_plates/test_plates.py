from plates import is_valid

def test_begin():
    assert is_valid("AA") == True
    assert is_valid("11") == False

def test_length():
    assert is_valid("A") == False
    assert is_valid("AB") == True

def test_numbers():
    assert is_valid("ABC02") == False
    assert is_valid("ABC20") == True

def test_spec():
    assert is_valid("AA2A") == False
    assert is_valid("AB22") == True
    assert is_valid("AA@2") == False