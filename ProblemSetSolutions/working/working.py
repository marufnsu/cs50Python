import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    isCorrectFrmt = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if isCorrectFrmt:
        slices = isCorrectFrmt.groups()
        if int(slices[1]) > 12 or int(slices[5]) > 12:
            raise ValueError
        first_time = changed_format(slices[1], slices[2], slices[3])
        second_time = changed_format(slices[5], slices[6], slices[7])
        return first_time + " to " + second_time
    else:
        raise ValueError

def changed_format(hr, min, am_pm):
    if am_pm == "PM":
        if int(hr) == 12:
            new_hr = 12
        else:
            new_hr = int(hr) + 12
    else:
        if int(hr) == 12:
            new_hr = 0
        else:
            new_hr = int(hr)
    if min == None:
        new_min = ":00"
        new_time = f"{new_hr:02}" + new_min
    else:
        new_time = f"{new_hr:02}" + ":" + min
    return new_time

if __name__ == "__main__":
    main()
