from twttr import shorten

def test_with_lower_case():
    assert shorten("twitter") == "twttr"

def test_with_upper_case():
    assert shorten("SKY") == "SKY"
    assert shorten("HELLO") == "HLL"

def test_with_number():
    assert shorten("1234") == "1234"

def test_with_punctuation():
    assert shorten("@!") == "@!"