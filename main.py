import os

print("--------------- DaTa Insights --------------- \n")
print("This software is made by Varun Banka \n")
print("Loading......\n")


def mainApp(): # dont read this, read from line 43

"""
the following block of code, takes the input value from the command, for example:
main.py test
here test is the input 
"""

    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Enter the name of csv file (without extension) : ")
    # code by Varun Banka
    args = parser.parse_args()
    input_value = args.input
    input_value = input_value + ".csv"

    try:
        df = pd.read_csv(file)
        profile = ProfileReport(df, minimal=True)
        profile.to_file(output_file="report.html")

    except Exception as e:
        # code by Varun Banka
        print(f"Error: {e}")


def restart():  # this func is for restarting the software
    restart = input("Would you like to restart? (y/n)   ")
    if restart == "y" or restart == "Y":
        mainApp()
    elif restart == "n":
        exit()
    else:
        print("Thanks for using DataHive")
        exit()


try:
    import pandas as pd
    from ydata_profiling import ProfileReport
    import argparse
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
            os.system("pip install argparse")
            os.system("clear")
            import pandas as pd
            from ydata_profiling import ProfileReport
            mainApp()

            while (True):
                restart()

        # code by Varun Banka
        except Exception as e:
            print(f"Error: {e}")
            input("Press any key to exit...")
            exit()

    else:
        input("Apart from power key, press any key to exit...")
        exit()
