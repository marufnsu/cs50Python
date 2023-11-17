from seasons import check_birthday

def main():
    test_bidrthday()

def test_bidrthday():
    assert check_birthday("1992-07-18") == (1992, 7, 18)
    assert check_birthday("1992-7-1") == None
    assert check_birthday("July 18, 1992") == None

if __name__ == "__main__":
    main()
