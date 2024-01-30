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

def main():
    filename = "APPLICATION_DETAILS.xlsx"
    file_exists(filename)

if __name__ == '__main__':
    main()