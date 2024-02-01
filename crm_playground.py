import pandas as pd
import numpy as np
from pandas import Series , DataFrame
import os
from datetime import datetime
import datetime as datetime_module



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
        print("\n{} folder Created\n".format(foldername))
    else:
        print("\n{} folder already exists\n".format(foldername))

def prob_ccc_wise_file_creation(foldername , filename):
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
    new_path = os.path.join(os.getcwd() , "nsc_class_wise_master")
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    
    nsc_df[nsc_df['CONN_CLASS'] == 'A'].to_excel(os.path.join(os.path.abspath(new_path) ,'agri_nsc_master.xlsx'))
    nsc_df[nsc_df['CONN_CLASS'] == 'I'].to_excel(os.path.join(os.path.abspath(new_path) ,'ind_nsc_master.xlsx'))
    nsc_df[nsc_df['CONN_CLASS'] == 'EV'].to_excel(os.path.join(os.path.abspath(new_path) ,'ev_nsc_master.xlsx'))
    nsc_df[nsc_df['CONN_CLASS'].isin(['G' , 'GS'])].to_excel(os.path.join(os.path.abspath(new_path) ,'govt_nsc_master.xlsx'))
    nsc_df[nsc_df['CONN_CLASS'] == 'D'].to_excel(os.path.join(os.path.abspath(new_path) ,'dom_nsc_master.xlsx'))
    nsc_df[nsc_df['CONN_CLASS'] == 'C'].to_excel(os.path.join(os.path.abspath(new_path) ,'comm_nsc_master.xlsx'))
    nsc_df[nsc_df['APPLIED_AS'] == "Promoter/Developer"].to_excel(os.path.join(os.path.abspath(new_path) ,'proc_b_nsc_master.xlsx'))
    tower_nsc_df_logic = ( nsc_df['NAME'].str.contains('SUMMIT') ) |( nsc_df['NAME'].str.contains('RELIANCE GIO') ) |\
    ( nsc_df['NAME'].str.contains('RELIANCE JIO') ) | ( nsc_df['NAME'].str.contains('INDUS TOWER') ) | ( nsc_df['NAME'].str.contains('INDUSTOWER') )
    nsc_df[tower_nsc_df_logic].to_excel(os.path.join(os.path.abspath(new_path) ,'tower_nsc_master.xlsx'))
    print("\nbase class wise , govt , tower nsc master files created in nsc_class_wise_master folder\n")

def last_months_date():
    '''
    this function gets the first day and last day of previous months
    
    argument -- None
    return -- Tuple
    '''
    today = datetime_module.date.today()
    first_day_curr_month = today.replace(day = 1)
    last_month_end_day = first_day_curr_month - datetime_module.timedelta(days=1)
    last_month_first_day = last_month_end_day.replace(day = 1)
    date_1 = last_month_first_day.strftime("%Y-%m-%d")
    date_2 = last_month_end_day.strftime("%Y-%m-%d")
    return date_1 , date_2

def different_nsc_reports(nsc_df):
    '''
    this function creates different NSC related reports except NSC master report and NSC pending reports
    like nsc_collection , nsc_connection , nsc_witheld
    
    argument -- pandas dataframe
    return -- None
    '''
    new_path = os.path.join(os.getcwd() , "nsc_other_reports")
    if not os.path.exists(new_path):
        os.makedirs(new_path)

    first_date , last_date = last_months_date()
    print(first_date , last_date , type(first_date) , type(last_date))
    nsc_coll_df = nsc_df[nsc_df['COLLECTION_DATE'].between(first_date , last_date)]
    nsc_conn_df = nsc_df[nsc_df['METER_INSTALL_DATE'].between(first_date , last_date)]
    nsc_coll_df.to_excel(os.path.join(os.path.abspath(new_path) ,'nsc_collection_last_month.xlsx'))
    nsc_conn_df.to_excel(os.path.join(os.path.abspath(new_path) ,'nsc_connection_last_month.xlsx'))

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
    # class_wise_nsc_master(nsc_df)
    different_nsc_reports(nsc_df)

    os.chdir(actual_path)

def main():
    filename = "APPLICATION_DETAILS.xlsx"
    foldername = 'ALL_CRM_FILES'
    # file_exists(filename)
    # create_folder(foldername)
    prob_ccc_wise_file_creation(foldername , filename)
    # new_connection(foldername , ) 


if __name__ == '__main__':
    main()