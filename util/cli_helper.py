"""Util functions for the script"""
import sys


def get_all_user_names():
    """Returns all the usernames given as parameter"""
    usernames = []
    if len(sys.argv) < 2:
        sys.exit('- Please provide at least one username!\n')
    for username in sys.argv[1:]:
        usernames.append(username)
    return usernames

def get_all_user_names_from_file():
    """Returns all the usernames from file given as parameter"""
    usernames = []
    if len(sys.argv) != 2:
        sys.exit('- Please provide one file path!\n')
    with open(sys.argv[1], "r") as f:
        usernames = f.readlines()
    return usernames
