months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

while True:
    try:
        userIn = input("Enter the date in month-day-year order: ")
        if "/" in userIn:
            m, d, y = userIn.strip().split("/")
            mUpdated = int(m) - 1
            if months[mUpdated] in months and int(d) in range(1, 32):
                if userIn.startswith(d) and m != d:
                    continue
                else:
                    print(f"{y}-{int(m):02}-{int(d):02}")
                    break
        elif "," in userIn:
            first, y = userIn.strip().split(", ")
            m, d = first.split(" ")
            if m in months and int(d) in range(1, 32):
                if userIn.startswith(d):
                    continue
                else:
                    mnthIndex = int(months.index(m)) + 1
                    print(f"{y}-{mnthIndex:02}-{int(d):02}")
                    break

    except (ValueError, IndexError):
        pass