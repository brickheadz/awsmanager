########################################################################################################################
#   Include personal library
########################################################################################################################

from cls import menumanager
from lib import command
from lib import awsmanager

########################################################################################################################
#   Main file
########################################################################################################################

''' Instance aws manager '''
aws_manager = awsmanager.Aws()
''' Instance menu manager '''
menu_manager = menumanager.Menu()
''' Instance command manager '''
command_manager = command.CommandManager()

''' If true, show an error message after clear into regex menu '''
filter_error = False
refresh = False

while True:
    if not refresh:
        menu_manager.print_default_regex_menu(filter_error)
        ''' Reset error '''
        filter_error = False
        print("\n")
        ''' Read keyboard input '''
        response = input('Option: ')
        filter = menu_manager.validate_regex_option(response)
    if filter == False:
        ''' Try another one '''
        filter_error = True
        continue
    else:
        refresh = False
        ''' Get all instances (eventually filtered) '''
        found = aws_manager.list_instances(filter)
        if not found:
            ''' No instance found.. maybe a configuration problem? '''
            if not filter:
                print('Warning, no instance found, check your AWS configuration!')
                exit()
            else:
                print('No instance found with filter: ' + filter)
                print('Type enter to retry with other filter, *close* to close this script')
                try:
                    error_handler = input('Choose: ')
                    if error_handler == 'close':
                        print('Script completed.\nBye!')
                        exit()
                except Exception:
                    continue
        else:
            found_instance_error = False
            while True:
                ''' Print instance list and options '''
                menu_manager.print_instance_found(aws_manager.get_instance_list(), found_instance_error)
                found_instance_error = False
                try:
                    choosed_option = input('Input: ')
                except Exception:
                    found_instance_error = True
                    refresh = False
                    continue
                if choosed_option == 'all':
                    ''' Start all ssh session '''
                    command_manager.open_server_through_ssh(aws_manager.get_instance_list())
                elif choosed_option == 'refresh':
                    ''' Refresh instances '''
                    refresh = True
                    break
                elif choosed_option == 'restart':
                    refresh = False
                    break
                elif choosed_option == 'close':
                    print('Script completed.\nBye!')
                    exit()
                else:
                    tmp_instance_list = aws_manager.get_instance_list()
                    try:
                        tmp_inst = tmp_instance_list[int(choosed_option)]
                        command_manager.clear_console()
                        tmp_inst.print_instance_information_and_options()
                        last = input('Input: ')
                        if last == 'close':
                            print('Script completed.\nBye!')
                            exit()
                        elif last == 'ssh':
                            print('Starting ssh session..')
                            command_manager.open_server_through_ssh([tmp_inst])
                        else:
                            continue
                    except Exception:
                        found_instance_error = True
                        continue
