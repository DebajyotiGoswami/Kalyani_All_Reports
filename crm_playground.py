import pandas as pandas
import numpy as np
from pandas import Series , DataFrame
import os
from datetime import datetime


def file_exists(filename):
    '''
    this function checks whether a given filename exist in current directory or not
    argument -- text 
    return -- None
    '''
    if not os.path.exists(filename):
        print("Filename {} does not exists . Create the file and try again".format(filename))
        exit(1)

def create_folder(foldername):
    '''
    this function create a folder named "crm_files". Nothing else.
    argument -- text
    return -- None
    '''
    new_path = os.getcwd() + '//' + foldername
    if not os.path.exists(new_path):
        os.makedirs(new_path)
        print("{} folder Created".format(foldername))
    else:
        print("{} folder already exists".format(foldername))

def main():
    filename = "APPLICATION_DETAILS.xlsx"
    foldername = 'ALL_CRM_FILES'
    file_exists(filename)
    create_folder(foldername)

if __name__ == '__main__':
    main()