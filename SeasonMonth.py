def check_Season():
    month = input("Enter your desired Month - ").lower()
    
    seasons = {
        "Winter": ['december', 'january', 'february'],
        "Spring": ['march', 'april', 'may'],
        "Summer": ['june', 'july', 'august'],
        "Autumn": ['september', 'october', 'november']
    }
    
    for season, months in seasons.items():
        if month in months:
            print(f"The Season is {season.capitalize()}.")
            return
    
    print("Invalid Month. Try again")

check_Season()