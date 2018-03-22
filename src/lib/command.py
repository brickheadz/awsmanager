########################################################################################################################
#   Include python library
########################################################################################################################
import os
import subprocess as sub
import time


class CommandManager:
    __USER_FOR_SSH = 'EDIT_THIS_USER'

    def test_aws_command(self):
        ''' Test if aws cli is installed '''
        p = sub.Popen(['aws', 'help'], stdout=sub.PIPE, stderr=sub.PIPE)
        output, errors = p.communicate()
        if errors:
            print('No AWS CLI found!')
            print('Please, follow this link in order to install and configure aws cli: https://aws.amazon.com/cli/')
            exit()
        else:
            print('Aws correctly loaded')

    def load_instances_from_aws(self):
        ''' List all valid instances, if a filter value is provided, made a search to remove all unwanted results '''
        print("\nStarting connection to AWS..")
        p = sub.Popen(['aws', 'ec2', 'describe-instances'], stdout=sub.PIPE, stderr=sub.PIPE)
        output, errors = p.communicate()
        if errors:
            ''' Manage error '''
            while True:
                print('Error during send request to aws.')
                print('Type *show* to see the error before close, anything else to close directly')
                try:
                    response = input('Input: ')
                    if response == 'show':
                        print(errors)

                    exit(1)
                except Exception:
                    print('Invalid input provided')
        else:
            return output

    def clear_console(self):
        os.system('clear')

    def open_server_through_ssh(self, instances):
        for instance in instances:
            ip = instance.get_public_ip()

            ''' Open new terminal with the ssh connection '''
            os.system(
                'x-terminal-emulator -e ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no '
                + self.__USER_FOR_SSH + '@' + ip +
                ' > /dev/null 2>/dev/null &'
            )

            ''' Sleep to avoid overlapping commands '''
            time.sleep(1)
