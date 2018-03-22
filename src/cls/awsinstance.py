class Instance:

    def __init__(self, response):
        self.status = str(response.get('State').get('Name'))
        self.monitoring = str(response.get('Monitoring').get('State'))
        self.name = self.__get_name_from_tags(response.get('Tags'))
        self.launch_time = str(response.get('LaunchTime'))
        self.ena_support = str(response.get('EnaSupport'))
        self.instance_type = str(response.get('InstanceType'))

        self.public_dns = str(response.get('PublicDnsName'))
        self.public_ip = str(response.get('PublicIpAddress'))
        self.private_dns = str(response.get('PrivateDnsName'))
        self.private_ip = str(response.get('PrivateIpAddress'))
        self.zone = str(response.get('Placement').get('AvailabilityZone'))

        try:
            self.groups = []
            for groups in response.get('SecurityGroups'):
                self.groups.append(str(groups.get('GroupName')))
        except Exception:
            ''' ntd '''

        self.root_device = str(response.get('RootDeviceName'))

        try:
            self.additional_device = []
            for hdd in response.get('BlockDeviceMappings'):
                delete = 'TRUE' if hdd.get('Ebs').get('DeleteOnTermination') else 'FALSE'
                tmp = [str(hdd.get('DeviceName')), str(hdd.get('Ebs').get('Status')), delete]
                self.additional_device.append(tmp)
        except Exception:
            ''' ntd '''
        pass

    ''' Parse tags to get instance name '''

    def __get_name_from_tags(self, tags):
        ''' Parse all tags to find the instance name '''
        name = 'No name'
        for t in tags:
            if t.get('Key') == 'Name':
                name = str(t.get('Value'))
        return name

    ''' Print formatted instance details '''

    def print_instance_information_and_options(self):
        name = ('Name not available' if not self.name else self.name)
        lenght = 4 + len(name)
        print('#' * lenght)
        print('# ' + name + ' #')
        print('#' * lenght)
        print("\n")
        print("# Base informations")
        print('- Status: ' + ('None' if not self.status else self.status))
        print('- Monitoring: ' + ('None' if not self.monitoring else self.monitoring))
        print('- Launched: ' + ('None' if not self.launch_time else self.launch_time))
        print('- Type: ' + ('None' if not self.instance_type else self.instance_type))
        print('- Ena supported: ' + ('TRUE' if self.instance_type else 'FALSE'))
        print('\n')
        print("# Network informations")
        print('- Zone: ' + ('None' if not self.zone else self.zone))
        print('- Public IP: ' + ('None' if not self.public_ip else self.public_ip))
        print('- Public DNS: ' + ('None' if not self.public_dns else self.public_dns))
        print('- Private IP: ' + ('None' if not self.private_ip else self.private_ip))
        print('- Private DNS: ' + ('None' if not self.private_dns else self.private_dns))
        print('\n')
        if self.groups:
            print("# Security groups name")
            i = 0
            for g in self.groups:
                print('- ' + str(i) + ') ' + ('None' if not g else g))
                i = i + 1
            print('\n')
        print('# Device informations')
        print('- Root Device: ' + ('None' if not self.root_device else self.root_device))
        if self.additional_device:
            i = 0
            print('\n')
            print('# Devices list')
            for ad in self.additional_device:
                print('- ' + str(i) + ') ')
                print('    - Name: ' + ('None' if not ad[0] else ad[0]))
                print('    - Status: ' + ('None' if not ad[1] else ad[1]))
                print('    - Delete On Termination: ' + ('None' if not ad[2] else ad[2]))
                i = i + 1
        print("\n")
        print('- Type *ssh* to open an ssh connection to the server')
        print('- Type *close* to close this script')
        print('- Press ENTER to go back to the previous menu')
        print("\n")
        pass

    ########################################################################################################################
    # GET
    ########################################################################################################################

    def get_public_ip(self):
        return self.public_ip

    def get_name(self):
        return 'Name not available' if not self.name else self.name
