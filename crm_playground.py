import pandas as pd
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

def prob_wise_file_creation(foldername , filename):
    '''
    this function search different prob_type in mother file and create separate files
    based on those prob_type and rename them with prob_type , date , time

    argument -- text
    return -- None
    '''
    crm_data = pd.read_excel(filename) # main DataFrame 
    for each_prob_type in list(set(crm_data['PROB_TYPE'])):
        prob_name = each_prob_type.replace(" ","_")             #+ "_" + str(datetime.now())[:-7].replace(":","_").replace(" ","_").replace("-","_")
        fullname = os.path.join(os.path.abspath(foldername) , prob_name + '.xlsx')
        df = crm_data[crm_data['PROB_TYPE'] == each_prob_type]
        df.to_excel(fullname)
        print("{} file created under {} folder".format(fullname , foldername))

def class_wise_nsc_master(nsc_df):
    '''
    this function create class wise master file of new connection like
    agri_nsc , ind_nsc , govt_nsc , tower_nsc , proc_b_nsc etc.
    
    argument -- pandas dataframe
    return -- None
    '''
    agri_nsc_df = nsc_df[nsc_df['CONN_CLASS'] == 'A']
    ind_nsc_df = nsc_df[nsc_df['CONN_CLASS'] == 'I']
    ev_nsc_df = nsc_df[nsc_df['CONN_CLASS'] == 'EV']
    govt_nsc_df = nsc_df[nsc_df['CONN_CLASS'].isin(['G' , 'GS'])]
    dom_sc_df = nsc_df[nsc_df['CONN_CLASS'] == 'D']
    comm_nsc_df = nsc_df[nsc_df['CONN_CLASS'] == 'C']
    print(agri_nsc_df.shape , govt_nsc_df.shape , comm_nsc_df.shape)

def new_connection(foldername , filename = "New_Connection.xlsx"):
    '''
    this function take care of all NSC related reports like pending nsc , pending master card , 
    collection in this month , connection in this month , witheld , class wise nsc master etc.
    
    argument -- text as file name . default file name is New_Connection.xlsx
    return -- None
    '''
    actual_path = os.getcwd()
    os.chdir(foldername)

    if not os.path.exists(filename):
        print("Filename {} does not exists . Create the file and try again".format(filename))
        exit(1)
    nsc_df = pd.read_excel(filename)
    class_wise_nsc_master(nsc_df)

    os.chdir(actual_path)

def main():
    filename = "APPLICATION_DETAILS.xlsx"
    foldername = 'ALL_CRM_FILES'
    #file_exists(filename)
    #create_folder(foldername)
    #prob_wise_file_creation(foldername , filename)
    new_connection(foldername , ) 

if __name__ == '__main__':
    main()