'''Utility functions for Strapwn.'''
from os import system, name

def cls() -> None:
    '''Clear the screen.'''
    system('cls' if name=='nt' else 'clear')

def display_motd() -> None:
    '''Display the MOTD.'''
    print("-" * 20)
    print("Welcome to Strapwn")
    print("Version: 1.0.0")
    print("Author: @Shadawks")
    print("-" * 20)