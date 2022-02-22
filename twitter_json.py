"""
Module for navigation of json file
"""
import json
import sys


def get_dict(file_name):
    """
    Function that makes dictionary from json file.
    """
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data


def file_navigation(data: dict) -> str:
    """
    Function that navigates through json file.
    """
    dict_keys = data.keys()
    print("Here you can see some options: " + ", ".join(dict_keys) +
          ".\n\nPlease, type in what would you like to see:")
    user_input = str(input())
    if user_input == "exit":
        sys.exit()
    elif user_input in dict_keys:
        if isinstance(data[user_input], dict):
            file_navigation(data[user_input])
        elif isinstance(data[user_input], list):
            print("The chosen data is a list.\n"
                  "You can type 'show all' to see the whole list or type sequence number of item.\n"
                  f"There are {len(data[user_input])} items.")
            second_user_input = input()
            if second_user_input == "exit":
                sys.exit()
            elif second_user_input.isnumeric():
                list_case(data, user_input, second_user_input, len(data[user_input]))
                sys.exit()
            elif second_user_input == 'show all':
                print(data[user_input])
            else:
                print("Invalid input. Please try again.")
                file_navigation(data)
        else:
            print(f"Here is your result:\n{data[user_input]}.")
    else:
        print("Invalid input. Please try again.\n")
        file_navigation(data)


def list_case(data, user_input, second_user_input, length):
    """
    Function that helps navigating through json file and is used 
    in case when user's choice is a list.
    """
    num = int(second_user_input) - 1
    if num < 0 or num > length:
        print("Invalid input. Please try again.")
        last_user_input = input()
        list_case(data, user_input, last_user_input, length)
    elif isinstance(data[user_input][num], dict):
        file_navigation(data[user_input][num])
    list_of_bool = [True for elem in data[user_input][num]
                    if isinstance(elem, dict)]
    if any(list_of_bool):
        file_navigation(data[user_input][num])
    else:
        print(f"Here is your result:\n {data[user_input][num]}.")


def main():
    """
    Main function
    """
    data = get_dict('twitter2.json')
    print("Hello, this program will help you in navigating through the json file.\n\n"
          "You can type 'exit' any time if you no longer want to use this program.\n\n"
          "What do you want to examine?\n")
    file_navigation(data)


if __name__ == "__main__":
    main()
