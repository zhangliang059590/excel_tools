# coding=utf-8
# This is a sample Python script.
import os
import sys

from random_selector import selector

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # Use a breakpoint in the code line below to debug your script.
    file_path = sys.argv[1]
    file_list = os.listdir(file_path)
    for file_name in file_list:
        if file_name.startswith('.'):
            continue
        selector(file_path + '/' + file_name)
        try:
            pass
        except:
            print(file_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
