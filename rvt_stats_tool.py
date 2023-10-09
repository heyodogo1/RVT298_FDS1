import rvt_stats_module

def input_numbs():
    numb = []
    while True:
        try:
            value = input("enter a bunch of numbers won't cha?")
            if value.lower() == 'done':
                break
            numba = float(value)
            numb.append(numba)
        except ValueError:
            print("Invalid input, enter something thats forreal yo!")
    return numb

def menu_stuff():
    numb = []
    while True:
        print("\nMenu:")
        print("1. input new numbers.")
        print("2. get mean.")
        print("3. get variance.")
        print("4. get standard deviation.")
        print("5. get standard error.")
        print("6. get z score w/ new observation.")
        print("7. display summary.")
        print("8. quit.")
              
        choice = input("enter one of the menu options: ")
        if choice == '1':
            numb = input_numbs()
        elif choice == '2':
            print("mean is here thy:", get_mean(numb))
        elif choice == '3':
            print("heres the variance bro:", get_variance(numb))
        elif choice == '4':
            print("heres the std dev dood:", get_std_dev(numb))
        elif choice == '5':
            print("here is the std error wizard:", get_std_error(numb))
        elif choice == '6':
            try:
                obs = float(input("please my good sir, give me the obs number bro:"))
                print("Z-score is this:", get_z_score(obs, numb))
            except ValueError:
                print("that ain't right man...")
        elif choice == '7':
            print("\nSummary:")
            print("Heres the numbers:", numb)
            print("Mean:", get_mean(numb))
            print("variance:", get_variance(numb))
            print("std dev is this yo:", get_std_dev(numb))
            print("std error is here with a beer:", get_std_error(numb))
        elif choice == '8':
            print("BYE BYE BYE BYE BYE!")
            break
        else:
            print("invalid choice, you suck.")
            
        