years = int(input("Enter number of years: "))

choice = input("""Select your choice:
1 - Days
2 - Weeks
3 - Hours
""")
if choice == "1":
    print(years*365)
elif choice == "2":
    print(years*52)
elif choice == "3":
    print(years*365*24)