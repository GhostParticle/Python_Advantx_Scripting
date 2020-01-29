
import subprocess
import sys
modules_path = r'C:\Python_Scripts\Advantx_Script\Modules'
sys.path.append(modules_path)
import time
import openpyxl
import User_Data
import Database_List
import Logs
import mainLoop
'''
import Add_IgnoreUser
import Single_User_Term
import Add_Password_Reset
import Add_Update_Access
import Add_ActivateUser
'''
import Functions

template = r'C:\Python_Scripts\Advantx_Script\Template_ADVMain.xlsx'
wb = openpyxl.load_workbook(template)
sheet = wb['Users']
sheet_2 = wb['DBs']
users = []

def get_user_setup():
    print('\n'
          'This Script runs for multiple or single users across multiple databases.\n'
          'Please check and make sure you have filled out the template first before selecting a program\n'
          '\n')
    print('Please Enter the Number of the Action Requested\n'
          '1. User Account Creations/Update (Creates accounts that done exist or updates existing accounts)\n'
          '2. User Account Terminations\n'
          '\n')
    numberA = int(input())
    print(numberA)

    if numberA == 1:
        print('\n'
          'If a user already exists, please enter the number for the action taken\n'
          '1. Ignore User Account (Bypasses existing account)\n'
          '2. Update User Account (UserID, Password, Access Level, Job Title)\n'
          '\n')
        numberB = int(input())
        if numberB == 2:
            print('\n'
                  'What type of update would you like to do\n'
                  '1. All fields except password\n'
                  '2. User Name Only\n'
                  '3. Password Only\n'
                  '4. Access Level Only\n'
                  '5. Activate Existing User (Updates Job Title, Access Level, And Re-Activates Account\n'
                  '\n')
            numberC = int(input())
            if numberC == 1:
                req = 'Add_UpdateAll'
                return req
            if numberC == 2:
                req = 'Add_UpdateUserName'
                return req
            if numberC == 3:
                req = 'Add_ChangePassword'
                return req
            if numberC == 4.:
                req = 'Add_UpdateAccessLevel'
                return req
            if numberC == 5:
                req = 'Add_ActivateUser'
                return req
            else:
                print('Incorrect Input, this program will now close')
                Functions.terminate_program()
        if numberB == 1:
            req = 'Add_IgnoreUser'
            return req
        else:
            print('Incorrect Input, this program will now close')
            Functions.terminate_program()
    if numberA == 2:
        req = 'Terminate_User'
        return req
    else:
        print('Incorrect Input, this program will now close')
        Functions.terminate_program()


# Main Program Start
def main():
    request = get_user_setup()
    # Folder And File Structure Creation
    print('\n'
          'COLLECTING USER DATA\n')
    user_data = User_Data.get_user_data_2(sheet)  # Gets all users data in list form
    db_list = Database_List.get_database_list(sheet_2)  # Gets all DBs in list form
    Ticket = sheet["A2"].value
    time.sleep(2)
    print('\n'
          'CREATING DIRECTORY AND LOG FILES\n')
    log_path = Logs.make_directory(Ticket)  # Creates Main Log Folder Path
    error_path = Logs.make_directory_login_error(log_path)  # Creates Error Folder Path
    completed_path = Logs.make_directory_completed(log_path)  # Creates Completed Folder Path
    user_log = Logs.create_user_log(log_path, Ticket)  # Creates User Log File
    login_fail_log = Logs.create_login_fail(log_path, Ticket) # Creates Login Fail Log File
    completed_log = Logs.create_completed_log(completed_path, Ticket)  # Creates Completed Log File
    error_log = Logs.create_error_log(error_path, Ticket)  # Creates Error Log File
    Logs.users_data_log(user_log, user_data)  # Writes User data to User Log File
    time.sleep(3)

    print('Your Request has been selected : {}\n'.format(request))
    if request == 'Add_UpdateAll':
        print('RUNNING ADD USERS OR UPDATE EXISTING ACCOUNT')
    if request == 'Add_UpdateUserName':
        print('RUNNING ADD USERS OR UPDATE USERNAME ONLY')
        mainLoop.run(user_data, db_list, completed_log, error_log, login_fail_log, Ticket, request)
    if request == 'Add_ChangePassword':
        print('RUNNING ADD USERS OR CHANGE PASSWORD ONLY')
        mainLoop.run(user_data, db_list, completed_log, error_log, login_fail_log, Ticket, request)
    if request == 'Add_IgnoreUser':
        print('RUNNING ADD USERS AND IGNORE ACTIVE ACCOUNTS')
        mainLoop.run(user_data, db_list, completed_log, error_log, login_fail_log, Ticket, request)
    if request == 'Terminate_User':
        print('RUNNING USER ACCOUNT TERMINATION PROCESS')
        mainLoop.run(user_data, db_list, completed_log, error_log, login_fail_log, Ticket, request)
    if request == 'Add_UpdateAccessLevel':
        print('RUNNING ADD USER OR CHANGE ACCESS LEVEL')
        mainLoop.run(user_data, db_list, completed_log, error_log, login_fail_log, Ticket, request)
    if request == 'Add_ActivateUser':
        print('RUNNING ADD USER OR ACTIVATE USER ACCOUNT')
        mainLoop.run(user_data, db_list, completed_log, error_log, login_fail_log, Ticket, request)

if __name__ == '__main__':
    main()