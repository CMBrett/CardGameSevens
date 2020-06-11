'''
Created on 11 Jun 2020

@author: Chris
'''
from colorama import Fore
from colorama.initialise import init

def info(output_str):
    '''
    '''
    init()
    print(Fore.BLUE + output_str + Fore.RESET)

def request_input(output_str):
    '''
    '''
    print(Fore.MAGENTA + output_str + Fore.RESET)

def warning(output_str):
    '''
    '''
    print(Fore.YELLOW + output_str + Fore.RESET)
    
def error(output_str):
    '''
    '''
    print(Fore.RED + output_str + Fore.RESET)

def notice(output_str):
    '''
    '''
    print(output_str)