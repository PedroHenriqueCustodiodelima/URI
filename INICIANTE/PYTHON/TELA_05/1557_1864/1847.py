temp1, temp2, temp3 = map(int, input().split())
if temp1 > temp2:
    if temp3 >= temp2:
        print(":)")
    else:
        if temp2 - temp3 < temp1 - temp2:
            print(":)")
        else:
            print(":(")
else:
    if temp1 < temp2:
        if temp3 <= temp2:
            print(":(")
        else:
            if temp3 - temp2 < temp2 - temp1:
                print(":(")
            else:
                print(":)")
    else:
        if temp3 > temp2:
            print(":)")
        else:
            print(":(")
