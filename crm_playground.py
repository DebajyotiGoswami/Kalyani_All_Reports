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

def prepare_df_master(filename):
    '''
    this function takes a excel file i.e. appl_details and create a dataframe out of it
    and then creates some customized columns also
    
    argument -- text
    return -- DataFrame
    '''
    master_df = pd.read_excel(filename)
    print("\nDataframe of {} details created".format(filename))
    return master_df

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
    os.chdir(new_path)
    print("\nWe are now in : {} folder\n".format(os.getcwd()))

def modify_df(df):
    '''
    this functon modifies the crm_data dataframe with some customized columns 
    like ccc_name , procedure-a/b , pole/nonpole , days since collection
    
    argument -- dataframe
    return -- dataframe
    '''
    df['SUPP_OFF'] = df['SUPP_OFF'].str[-7 : ] #+ df['SUPP_OFF'].str[-8 : -7] + df['SUPP_OFF'].str[ : -8]
    return df

def ccc_wise_file_creation(crm_data):
    '''
    this function search different ccc name in mother datafeame and create separate files
    based on those ccc name and rename them with ccc name , date , time

    argument -- DataFrame
    return -- None
    '''
    # crm_data = modify_df(crm_data)

    new_path = os.path.join(os.getcwd() , "ccc_wise_master")
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    for each_ccc in list(set(crm_data['SUPP_OFF'])):
        ccc_name = each_ccc.replace(" ","_").replace("-","_")
        fullname = os.path.join(os.path.abspath(new_path) , "application_details_" + ccc_name + ".xlsx")
        df = crm_data[crm_data['SUPP_OFF'] == each_ccc]
        df.to_excel(fullname)
        print("\n{} file created in {} folder".format(fullname , new_path))
    print("\nDifferent ccc wise master files created\n")

def prob_wise_file_creation(crm_data):
    '''
    this function search different prob_type in mother datafeame and create separate files

    argument -- DataFrame
    return -- None
    '''
    # crm_data = modify_df(crm_data)

    new_path = os.path.join(os.getcwd() , "prob_type_wise_master")
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    for each_prob_type in list(set(crm_data['PROB_TYPE'])):
        prob_name = each_prob_type.replace(" ","_")             #+ "_" + str(datetime.now())[:-7].replace(":","_").replace(" ","_").replace("-","_")
        fullname = os.path.join(os.path.abspath(new_path) , prob_name + '.xlsx')
        df = crm_data[crm_data['PROB_TYPE'] == each_prob_type]
        df.to_excel(fullname)
        print("\n{} file created under {} folder".format(fullname , new_path))
    print("\nDifferent problem wise files created\n")
    
    # new_path = os.path.join(os.getcwd() , "ccc_wise_master")
    # if not os.path.exists(new_path):
    #     os.makedirs(new_path)
    # for each_ccc in list(set(crm_data['SUPP_OFF'])):
    #     ccc_name = each_ccc.replace(" ","_").replace("-","_")
    #     fullname = os.path.join(os.path.abspath(new_path) , "application_details_" + ccc_name + ".xlsx")
    #     df = crm_data[crm_data['SUPP_OFF'] == each_ccc]
    #     df.to_excel(fullname)
    #     print("\n{} file created in {} folder".format(fullname , new_path))
    # print("\nDifferent ccc wise master files created\n")

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
    nsc_coll_df = nsc_df[nsc_df['COLLECTION_DATE'].between(first_date , last_date)]
    nsc_conn_df = nsc_df[nsc_df['METER_INSTALL_DATE'].between(first_date , last_date)]
    nsc_coll_df.to_excel(os.path.join(os.path.abspath(new_path) ,'nsc_collection_last_month.xlsx'))
    nsc_conn_df.to_excel(os.path.join(os.path.abspath(new_path) ,'nsc_connection_last_month.xlsx'))
    print("\nNSC collection and NSC connection files created\n")

def pending_nsc_reports(nsc_df):
    '''
    this function creates pending nsc , pending master card reports details and summary
    
    argument -- pandas dataframe
    return -- None
    '''
    new_path = os.path.join(os.getcwd() , "nsc_pending_reports")
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    
    pending_nsc_logic = (nsc_df['APPL_STATUS'] == 'PROCESSED') & (nsc_df['INSTALLATION_NO'] == '(null)') & \
    (~nsc_df['SR_MAIN_STATUS'].isin(['REJECTED'])) & (nsc_df['COLLECTION_STATUS'] == 'Completed') &\
    (nsc_df['COLLECTION_DATE']!='(null)') & (~nsc_df['SERV_CONN_STATUS'].isin(['Completed','Witheld','Rejected','Cancelled','Closed','Disputed']))

    columns = ['SUPP_OFF' , 'APPL_NO' , 'CON_ID' , 'NAME' , 'ADDRESS' , 'CONN_CLASS' , 'CONN_PHASE' , 'LOAD_APPLIED' , 'POLE_REQUIRED' , \
               'COLLECTION_DATE' , 'WON_ASSIGNED' , 'APPLIED_AS' ]
    
    pending_nsc_df  = nsc_df[pending_nsc_logic][columns]
    pending_nsc_df.to_excel(os.path.join(os.path.abspath(new_path) , 'pending_nsc_details.xlsx'))

def pending_master_card(nsc_df):
    '''
    this function prepares the pending master card report
    
    argument -- DataFrame
    return -- None
    '''
    new_path = os.path.join(os.getcwd() , "nsc_pending_reports")
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    
    pending_master_card_logic = (~nsc_df['SR_MAIN_STATUS'].isin(['DUPLICATE' , 'REJECTED'])) &  (nsc_df['APPL_STATUS'].isin(['PROCESSED' ,'SAP_INSERTED' , 'DCC_INSERTED'])) & \
    (nsc_df['SERV_CONN_STATUS'] == 'Completed') & (nsc_df['SERV_CONN_DATE'] != '(null)') & (nsc_df['METER_ISSUE_STATUS'] == 'Completed') & \
    (nsc_df['METER_INSTALL_DATE'] != '(null)') & (nsc_df['INSTALLATION_NO'] == '(null)') 

    columns = ['SUPP_OFF' , 'APPL_NO' , 'CON_ID' , 'NAME' , 'ADDRESS' , 'CONN_CLASS' , 'CONN_PHASE' , 'LOAD_APPLIED' , 'POLE_REQUIRED' , \
               'COLLECTION_DATE' , 'WON_ASSIGNED' , 'APPLIED_AS' ]
    
    pending_master_card  = nsc_df[pending_master_card_logic][columns]
    pending_master_card.to_excel(os.path.join(os.path.abspath(new_path) , 'pending_master_card.xlsx'))
    print("\nPending master card file created in {}".format(new_path))

def new_connection(nsc_df):
    '''
    this function take care of all NSC related reports like pending nsc , pending master card , 
    collection in this month , connection in this month , witheld , class wise nsc master etc.
    
    argument -- DataFrame
    return -- None
    '''
    # new_path = os.path.join(os.path.abspath(os.getcwd()) , "prob_type_wise_master" , filename)
    # # if not os.path.exists(filename):
    # if not os.path.exists(new_path):
    #     print("Filename {} does not exists . Create the file and try again".format(filename))
    #     exit(1)
    # nsc_df = pd.read_excel(new_path)
    class_wise_nsc_master(nsc_df)
    different_nsc_reports(nsc_df)
    pending_nsc_reports(nsc_df)
    pending_master_card(nsc_df)

    # os.chdir(actual_path)

def main():
    filename = "APPLICATION_DETAILS_TEMP.xlsx"
    foldername = 'ALL_CRM_FILES'
    file_exists(filename)  #check if the file exists or send error message
    master_df = prepare_df_master(filename) #create the datafram of the total master data
    master_df = modify_df(master_df) #modify the dataframe as per our requirements
    create_folder(foldername + "-" + str(datetime.today())[:10]) #create folder , if not exits , and cd into it
    prob_wise_file_creation(master_df) #problem wise master data creation
    ccc_wise_file_creation(master_df) #ccc wise master data creation
    new_connection(master_df[master_df['PROB_TYPE'] == 'New Connection']) #nsc related different reports 

if __name__ == '__main__':
    main()