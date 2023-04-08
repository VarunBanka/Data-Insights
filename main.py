import os  # this module is being used in line 38 so dont remove it

print("--------------- DaTa Insights --------------- \n")
print("This software is made by Varun Banka \n")
print("Loading......\n")


def mainApp():    # the code starts executing from line 30
    file = input("Enter the name of csv file (without extension) : ")
    file = file + ".csv"

    try:
        df = pd.read_csv(file)
        profile = ProfileReport(df, minimal=True)
        profile.to_file(output_file="report.html")

    except Exception as e:
        # code by Varun Banka
        print(f"Error: {e}")


def restart():  # this func is for restarting the software
    restart = input("Would you like to restart? (y/n)   ")
    if restart == "y":
        mainApp()
    elif restart == "n":
        exit()
    else:
        print("Thanks for using DataHive")
        exit()


try:
    import pandas as pd
    from ydata_profiling import ProfileReport
    mainApp()

    while (True):
        restart()


except ImportError:  # idk if the following code is required but i dont wanna remove it ffs
    install_dependencies = input(
        "Some dependencies aren't installed. Would you like to install them? (y/n) ")
    if install_dependencies.lower() == "y":
        try:
            os.system("pip install pandas")
            os.system("pip install ydata-profiling")
            os.system("clear")
            import pandas as pd
            from ydata_profiling import ProfileReport
            mainApp()

            while (True):
                restart()

        except Exception as e:
            print(f"Error: {e}")
            input("Press any key to exit...")
            exit()

    else:
        input("Apart from power key, press any key to exit...")
        exit()




# code by Varun Banka
