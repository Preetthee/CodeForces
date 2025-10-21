while True:
    try:
        s = input()
    except EOFError:
        s = ""
    if s == "Is it rated?":
            print("NO")
    else:
         break