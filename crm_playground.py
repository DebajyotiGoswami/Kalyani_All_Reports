import pandas as pandas
import numpy as np
from pandas import Series , DataFrame
import os
from datetime import datetime


def file_exists(filename):
    '''
    this function checks whether a given filename exist in current directory or not
    argument -- text 
    return -- True / False
    '''
    return os.path.exists(filename)

def main():
    print("hello")
    filename = "APPLICATION_DETAILS.xlsx"
    flag = file_exists(filename)
    print(flag)

if __name__ == '__main__':
    main()