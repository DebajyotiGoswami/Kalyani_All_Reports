from crm_playground import file_exists , prepare_df_master , create_folder , ccc_wise_file_creation
from datetime import datetime
import os


def defective_meter(df):
    '''
    function to create different defective meter reports like total defective , 
    3 phase defective , 2kw defective , new defective etc
    
    argument -- dataframe
    return -- None
    '''
    print(os.getcwd())

def conventional_meter(df):
    '''
    function to create different conventional meter reports like total conventional , 
    3 phase conventional , 2kw conventional etc
    
    argument -- dataframe
    return -- None
    '''
    print(os.getcwd())

def hybrid_meter(df):
    '''
    function to create different hybrid meter reports like total hybrid , 
    3 phase hybrid , 2kw hybrid etc
    
    argument -- dataframe
    return -- None
    '''
    print(os.getcwd())

def other_report(df):
    '''
    function to create different meter reports like warranty period meters , 
    g20_g21 meters , new installed meters etc
    
    argument -- dataframe
    return -- None
    '''
    print(os.getcwd())

def main():
    filename = "meter_status_report.xlsx"
    foldername = 'ALL_METER_FILES'
    file_exists(filename)  #check if the file exists or send error message
    master_df = prepare_df_master(filename) #create the datafram of the total master data
    create_folder(foldername + "-" + str(datetime.today())[:10]) #create folder , if not exits , and cd into it
    ccc_wise_file_creation(master_df , "CCC_CODE") #problem wise and ccc wise master data creation
    defective_meter(master_df) #different defective meter reports creation
    conventional_meter(master_df) #different conventional meter reports creation
    hybrid_meter(master_df) #different hybrid meter reports creation
    other_report(master_df) #other meter reports creation

if __name__ == '__main__':
    main()