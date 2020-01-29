
import sys
modules_path = r'C:\Python_Scripts\Advantx_3.0\Modules'
sys.path.append(modules_path)
import Functions
import Logs
import Login
import time
import Error_Checking
import Open_Database

def Add_IgnoreUser(gng, DB, user_info, completed_log, error_log):
    if gng == 0:
        Functions.add_user(DB, user_info)
        Logs.log_complete(DB, user_info, completed_log)
    else:
        Logs.user_already_exist(DB, user_info, error_log)
        Functions.user_exists()

def Add_ChangePassword(gng, DB, user_info, completed_log):
    if gng == 0:
        Functions.add_user(DB, user_info)
        Logs.log_complete(DB, user_info, completed_log)
    else:
        Functions.password_update(user_info)
        Logs.log_complete(DB, user_info, completed_log)

def Terminate_User(gng, DB, user_info, error_log, Ticket, completed_log):
    if gng == 0:
        Functions.user_not_exist()
        Logs.user_does_not_exist(DB, user_info, error_log)
    else:
        Functions.terminate_user(Ticket)
        Logs.user_terminated(DB, user_info, completed_log)

def Add_UpdateAccessLevel(gng, DB, user_info, completed_log):
    if gng == 0:
        Functions.add_user(DB, user_info)
        Logs.log_complete(DB, user_info, completed_log)
    else:
        Functions.update_access_level(user_info)
        Logs.log_complete(DB, user_info, completed_log)

def Add_ActviateUser(gng, DB, user_info, completed_log):
    if gng == 0:
        Functions.add_user(DB, user_info)
        Logs.log_complete(DB, user_info, completed_log)
    else:
        Functions.activate_user(user_info)
        Logs.log_complete(DB, user_info, completed_log)

def Update_Username(gng, DB, user_info, completed_log):
    if gng == 0:
        Functions.add_user(DB, user_info)
        Logs.log_complete(DB, user_info, completed_log)
    else:
        Functions.update_username(user_info)
        Logs.log_complete(DB, user_info, completed_log)

def run(user_data, db_list, completed_log, error_log, login_fail_log, Ticket, request):
    for DB in db_list:
        db_login = Open_Database.open_ADV(DB, login_fail_log)
        if db_login == 1:
            Login.login()
            error = Error_Checking.get_Errors(DB, login_fail_log)
            if error == 9:
                Functions.open_userTables()
                for user_info in user_data:
                    user = user_info[1] + "," + user_info[0]
                    gng = Functions.find_user(user, user_info)
                    if request == 'Add_IgnoreUser':
                        Add_IgnoreUser(gng, DB, user_info, completed_log, error_log)
                    if request == 'Add_ChangePassword':
                        Add_ChangePassword(gng, DB, user_info, completed_log)
                    if request == 'Terminate_User':
                        Terminate_User(gng, DB, user_info, error_log, Ticket, completed_log)
                    if request == 'Add_UpdateAccessLevel':
                        Add_UpdateAccessLevel(gng, DB, user_info, completed_log)
                    if request == 'Add_ActivateUser':
                        Add_ActviateUser(gng, DB, user_info, completed_log)
                    if request == 'Add_UpdateUserName':
                        Update_Username(gng, DB, user_info, completed_log)

            else:
                Logs.login_failed(DB, login_fail_log)
            Functions.close_app()
            time.sleep(2)
        if db_login == 0:
            pass