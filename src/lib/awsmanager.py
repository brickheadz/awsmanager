########################################################################################################################
#   Include python library
########################################################################################################################
import json
import re

########################################################################################################################
#   Include personal library
########################################################################################################################
from cls import awsinstance
from lib import command


class Aws:
    _instances = []
    _command_manager = None

    def __init__(self):
        self._command_manager = command.CommandManager()
        self._command_manager.test_aws_command()

    def list_instances(self, regex_filter=None):
        output = self._command_manager.load_instances_from_aws()
        ''' Parse aws cli response '''
        return self.__filter_response(output, regex_filter)

    def get_instance_list(self):
        return self._instances

    def __filter_response(self, results, regex_filter=None):
        ''' If a filter is provided, extract only needed data '''
        decoded_results = json.loads(results.decode('utf8'))
        decoded_results = decoded_results.get('Reservations')
        ''' Reset instance list '''
        self._instances = []
        for v in decoded_results:
            ''' Base data for all instance '''
            for data in v.get('Instances'):
                ''' If a regex is provided, check into tags for match'''
                if regex_filter is not None:
                    tags = data.get('Tags')
                    for t in tags:
                        if t.get('Key') == 'Name':
                            match = re.search(regex_filter, t.get('Value'), re.IGNORECASE)
                            if match:
                                ''' Found match '''
                                self._instances.append(self.__manage_instance_data(data))
                else:
                    self._instances.append(self.__manage_instance_data(data))
        if not self._instances:
            return False
        else:
            return True

    def __manage_instance_data(self, obj):
        return awsinstance.Instance(obj)
