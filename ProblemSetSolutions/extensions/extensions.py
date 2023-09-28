fileExt = input("Provide the file name with extensions: ")
fileExt = fileExt.lower().strip()

if "." in fileExt:
    lst = fileExt.split(".")
    l = len(lst)
    first = lst[0]
    last = lst [l-1]
    match last:
        case "gif" | "png":
            print(f"image/{last}")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "pdf" | "zip":
            print(f"application/{last}")
        case "txt":
            print(f"text/{first}")
        case _:
            print("application/octet-stream")
else:
    print("application/octet-stream")
