from crm_playground import file_exists , prepare_df_master , create_folder , ccc_wise_file_creation , create_folder_return_path , create_file_from_df
from datetime import datetime
import os


def defective_meter(df):
    '''
    function to create different defective meter reports like total defective , 
    3 phase defective , 2kw defective , new defective etc
    
    argument -- dataframe
    return -- None
    '''
    defective_df = df[(df['CURR_DEF_STATUS'] == 'X') & (df['CONN_STAT'] == 'LIVE')]
    defective_3ph_df = defective_df[defective_df['PHASE'] == 3]
    defetive_ind_df = defective_df[defective_df['BASE_CLASS'] == 'I']
    defective_2kw_df = defective_df[defective_df['CONN_LOAD'] > 2.35]

    create_file_from_df(foldername = "defective_meter_reports", filename = "defective_meter.xlsx" , df = defective_df)
    create_file_from_df(foldername = "defective_meter_reports", filename = "3ph_defective.xlsx" , df = defective_3ph_df)
    create_file_from_df(foldername = "defective_meter_reports", filename = "industry_defective.xlsx", df = defetive_ind_df)
    create_file_from_df(foldername = "defective_meter_reports", filename = "2kw_defective.xlsx" , df = defective_2kw_df)

def conventional_meter(df):
    '''
    function to create different conventional meter reports like total conventional , 
    3 phase conventional , 2kw conventional etc
    
    argument -- dataframe
    return -- None
    '''
    conven_df = df[(df['TYPE_OF_METER'] == 'ELECTROMAGNATIC') & (df['CONN_STAT'] == 'LIVE')]
    conven_3ph_df = conven_df[conven_df['PHASE'] == 3]
    conven_2kw_df = conven_df[conven_df['CONN_LOAD'] > 2.35]
    conven_1kw_df = conven_2kw_df[conven_2kw_df['CONN_LOAD'] > 1.17]
    conven_high_value_df = conven_df[conven_df['BASE_CLASS'].isin(['I' , 'A' , 'H' , 'W'])]
    conven_defective_df = conven_df[conven_df['CURR_DEF_STATUS'] == 'X']

    create_file_from_df(foldername = "conventional_meter_reports" , filename = "conventional_meter.xlsx" , df = conven_df)
    create_file_from_df(foldername = "conventional_meter_reports" , filename = "conven_3phase_meter.xlsx" , df = conven_3ph_df)
    create_file_from_df(foldername = "conventional_meter_reports" , filename = "conven_2kw_meter.xlsx" , df = conven_2kw_df)
    create_file_from_df(foldername = "conventional_meter_reports" , filename = "conven_1kw_meter.xlsx" , df = conven_1kw_df)
    create_file_from_df(foldername = "conventional_meter_reports" , filename = "conven_high_value.xlsx" , df = conven_high_value_df)
    create_file_from_df(foldername = "conventional_meter_reports" , filename = "conven_and_defective.xlsx" , df = conven_defective_df)
    
def hybrid_meter(df):
    '''
    function to create different hybrid meter reports like total hybrid , 
    3 phase hybrid , 2kw hybrid etc
    
    argument -- dataframe
    return -- None
    '''
    new_path = create_folder_return_path("hybrid_meter_reports")

def other_report(df):
    '''
    function to create different meter reports like warranty period meters , 
    g20_g21 meters , new installed meters etc
    
    argument -- dataframe
    return -- None
    '''
    new_path = create_folder_return_path("other_meter_reports")

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