def main():
    print("Starting The Code Challenge")
  # Declare Any main() Variables - (Not Global)

    sports = ["soccer", "football", "baseball", "basketball","hockey", "tennis", "cricket", "rugby"]
    for x in sports:
        print(x)
        if x == "baseball":
            continue
        if x == "tennis":
            break
    for x in range(2, 6):
        print("apple")
    else:
        print("finally finished")
    fav = ["1", "2", "3"]
    teams = ["warriors", "Barcelona", "Giants", "49ers", "Sharks", "Royal Challengers", "Bucs"," Clippers"]
    for x in fav:
        for y in teams:
            print(x, y)
    print("Ending The Code Challenge")

main()