# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import multiprocessing
import os
import sys

from func.farm import *

def run_bot(screen='screen1'):
    # start_idle_farm()
    # exit()
    # Use a breakpoint in the code line below to debug your script.
    while True:
        try:
            accounts = settings[screen]['farm']
            print(accounts)
            for account in accounts:
                start_farm_account(screen=screen, account=account)

        except Exception as e:
            print(e)
            traceback.print_exc()
        finally:
            pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        run_bot(screen="screen1")
        #p1 = multiprocessing.Process(target=run_bot, args=('screen1',))
        #p2 = multiprocessing.Process(target=run_bot, args=('screen2',))
        #p1.start()
        # starting process 2
        #p2.start()
    except KeyboardInterrupt:
        print('Interrupted')
        #p1.terminate()
        #p2.terminate()
        #p1.join()
        #p2.join()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
