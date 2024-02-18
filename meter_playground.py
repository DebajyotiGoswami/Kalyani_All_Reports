from crm_playground import file_exists , prepare_df_master , create_folder
from datetime import datetime



def main():
    filename = "meter_status_report.xlsx"
    foldername = 'ALL_METER_FILES'
    file_exists(filename)  #check if the file exists or send error message
    master_df = prepare_df_master(filename) #create the datafram of the total master data
    create_folder(foldername + "-" + str(datetime.today())[:10]) #create folder , if not exits , and cd into it
    # prob_ccc_wise_file_creation(master_df) #problem wise and ccc wise master data creation
    # new_connection(master_df[master_df['PROB_TYPE'] == 'New Connection']) #nsc related different reports

if __name__ == '__main__':
    main()