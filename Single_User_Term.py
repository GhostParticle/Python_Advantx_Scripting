

def run(user_data, db_list, completed_log, error_log, login_fail_log, Ticket):
    import sys
    modules_path = r'C:\Python_Scripts\Advantx_3.0\Modules'
    sys.path.append(modules_path)
    import Functions
    import Logs
    import Login
    import time
    import Error_Checking
    import Open_Database
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
                    if gng == 0:
                        Functions.user_not_exist()
                        Logs.user_does_not_exist(DB, user_info, error_log)
                    else:
                        Functions.terminate_user(Ticket)
                        Logs.user_terminated(DB, user_info, completed_log)
                Functions.close_app()
            else:
                pass
            time.sleep(2)
        if db_login == 0:
            pass