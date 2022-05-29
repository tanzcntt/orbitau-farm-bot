# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from func.farm import *


def run_bot(name):
    # start_idle_farm()
    # exit()
    # Use a breakpoint in the code line below to debug your script.
    while True:

        # start_farm_account2()
        try:
            start_farm_account3()
            start_farm_account2()
            start_farm_account1()
        except Exception:
            reload_and_login(account=1)
        finally:
            pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_bot('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
