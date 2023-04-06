import os

print("--------------- DataHive --------------- \n")
print("This software is made by Varun Banka \n")


def main():
    file = input("Enter the path of csv file: ")

    try:
        df = pd.read_csv(file)
        profile = ProfileReport(df, minimal=True)
        profile.to_file(output_file="report.html")

    except Exception as e:
        print(f"Error: {e}")

# code by Varun Banka
def restart():
    restart = input("Would you like to restart? (y/n)   ")
    if restart == "y":
        main()
    else:
        print("Thanks for using DataHive")
        break


try:
    import pandas as pd
    from ydata_profiling import ProfileReport
    main()
    while (True):
        restart()

except ImportError:
    install_dependencies = input(
        "Some dependencies aren't installed. Would you like to install them? (y/n) ")
    if install_dependencies.lower() == "y":
        try:
            os.system("pip install pandas")
            os.system("pip install ydata-profiling")
            os.system("clear")
            import pandas as pd
            from ydata_profiling import ProfileReport
            main()

            while (True):
                restart()

        except Exception as e:
            print(f"Error: {e}")
            input("Press any key to exit...")
            exit

    else:
        input("Press any key to exit...")
        exit











# code by Varun Banka