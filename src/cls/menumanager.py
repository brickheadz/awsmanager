"""Includes"""
from lib import command


class Menu:
    __DEFAULT_REGEX = [
        'EDIT_THIS_LINE'
    ]
    _command_manager = None

    def __init__(self):
        self._command_manager = command.CommandManager()

    def print_default_regex_menu(self, error=False):
        # Clean console output
        self._command_manager.clear_console()
        if error:
            print("Invalid option provided, please choose another one..\n\n")
        print('######################################################')
        print('#                        OPTIONS                     #')
        print('######################################################')
        print("\n# List of default regex:\n")
        if self.__DEFAULT_REGEX:
            key = 0
            for item in self.__DEFAULT_REGEX:
                print(str(key) + ') ' + item)
        print("\n# Other options:\n")
        print("- Type *none* to show all instances without any filter")
        print("- Type *close* close this script")

    def validate_regex_option(self, choosed):
        if choosed == 'none':
            return None
        elif choosed == 'close':
            print("Script ended.\nBye!")
            exit()
        else:
            try:
                # Convert choosed to int and return the regex
                return self.__DEFAULT_REGEX[int(choosed)]
            except Exception:
                return False

    def print_instance_found(self, running, stopped, error=False):
        self._command_manager.clear_console()
        if error:
            print("Invalid option provided, please choose another one..\n\n")
        print('######################################################')
        print('#                  FILTERED INSTANCES                #')
        print('######################################################')
        print('\n')
        i = 0

        if running:
            print('################# RUNNING INSTANCES ##################')
            print('\n')
            for inst in running:
                print('- ' + str(i) + ') ' + inst.name)
                i = i + 1
            print('\n')

        if stopped:
            print('################# STOPPED INSTANCES ##################')
            print('\n')
            for inst in stopped:
                print('- ' + str(i) + ') ' + inst.name)
                i = i + 1

        i = i - 1
        print('\n')
        print('- Type 0 to ' + str(i) + ' to show server options')
        print('- Type *all* to open an SSH into ALL RUNNING server')
        print('- Type *refresh* to refresh instances with the same filter')
        print('- Type *restart* to go back to the first menu')
        print('- Type *close* to close this script')
        print('\n')

    def print_single_instance_options(self, instance):
        length = 4 + len(instance.get_name())
        print('#' * length)
        print('# ' + ('None' if not self.name else self.name) + ' #')
        print('#' * length)
        print("\n")
        print('- Type *ssh* to open an ssh connection to the server')
        print('- Type *close* to close this menu')
