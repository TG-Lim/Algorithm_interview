while True:
    s = input().strip()
    if s != "0":
        s_reversed = s[::-1]
        if s == s_reversed:
            print("yes")
        else:
            print("no")
    else:
        exit()