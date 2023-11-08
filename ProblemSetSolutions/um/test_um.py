from um import count

def test_lowercase():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_word():
    assert count("yummi") == 0

def test_space_surronded():
    assert count("Hello um world") == 1
    assert count("um?") == 1
