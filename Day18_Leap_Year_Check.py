def Leap_year_check():
    year=int(input("Enter the Year:"))
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print(f"It is a Leap Year:{year}")
            else:
                print(f"It is not a leap Year:{year}")
        else:
            print(f"It is a leap Year:{year}")
    else:
        print(f"It is not a leap Year:{year}")
Leap_year_check()