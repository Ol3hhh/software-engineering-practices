def Add(number):
    if number == "":
        return 0
    result = 0
    number = number.replace("\n", ",")
    parts = number.split(",")

    for x in parts:
        if x == "":
            raise ValueError("Bad String!!!")
        
        result += int(x)
    

    return result