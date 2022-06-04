# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import sys

from func.farm import *


def run_bot(name):
    # start_idle_farm()
    # exit()
    # Use a breakpoint in the code line below to debug your script.
    while True:

        # start_farm_account2()
        try:
            accounts = settings['farm']
            print(accounts)
            for account in accounts:
                start_farm_account(account=account)

        except Exception as e:
            print(e)
        finally:
            pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        run_bot('a')
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
