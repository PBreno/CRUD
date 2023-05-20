# This is a sample Python script.
from src.public.DAO import  *
from src.public.DAO.WorldDAO import WorldDAO


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    world = WorldDAO()
    world.selectCityID(1909)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
