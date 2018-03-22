# AWS EC2 cli manager (Python version)

Manage all your instances of aws ec2 without connecting to amazon web-panel.\
Useful for server without any GUI.

## Getting Started

After you downloaded this repo you need to configure your account for ssh connection, then you can install this script or launch directly (see **Installing** chapter for more informations). \
I'll update this script in the near future to add more options like (for e.g.):
- send command without open a shell
- change tags
- change the **ena support**

### Prerequisites

Working OS: Linux (will support all OSs).

Software needed:
- Python 3.x
- Aws Cli (https://aws.amazon.com/cli/)
- **Pip3** and **PyInstaller** (optional)

### Run

Legacy example:
```
python3 main.py
```

Binary example:
```
./awsmanager
```

### Installing

You have two choice: 
1) Run directly this script from src folder;
2) Create a binary from this script via PyInstaller (or similar).

#### Legacy installation step by step:

0 - Install aws cli (follow the official guide at https://aws.amazon.com/cli/) and configure your personal keys.

0.1 - Download this repository.\
0.2 - Edit **__USER_FOR_SSH** value into lib/command.py \
0.3 - Edit **__DEFAULT_REGEX** into cls/menumanager.py

1 - Go into src folder and type:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
```
$ python3 main.py
```

#### Binary installation step by step:

0 - Install aws cli (follow the official guide at https://aws.amazon.com/cli/) and configure your personal keys.

0.1 - Download this repository.\
0.2 - Edit **__USER_FOR_SSH** value into lib/command.py \
0.3 - Edit **__DEFAULT_REGEX** into cls/menumanager.py

2 - Install PyInstaller with:  \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
```
# pip3 install pyinstaller 
```

3 - Go into any folder and type  \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
```
$ pyinstaller -p ABSOLUTE_PATH/src/ -F ABSOLUTE_PATH/src/main.py -n EXECUTABLE_FILE_NAME
```
3.1 - Example: \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
```
$ pyinstaller -p /home/silver/git/tools/awsmanager/src/ -F /home/silver/git/tools/awsmanager/src/main.py -n awsmanager
```

4 - Move the binary and make usable from anywere (Optional):\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
```
# First move the binary into /usr/local/bin
sudo mv ./dist/awsmanager /usr/local/bin/
# Then make it executable
sudo chmod a+x /usr/local/bin/awsmanager  
```

### Example (binary version):
```
$ ./dist/awsmanager
```
Will provide:
```
######################################################
#                        OPTIONS                     #
######################################################
 
# List of default regex:
 
0) EDIT_THIS_LINE <= It's an example, you need to change this value
 
# Other options:
 
- Type *none* to show all instances without any filter
- Type *close* close this script
 

Options:
```
Then:
```
######################################################
#                  FILTERED INSTANCES                #
######################################################
 

- 0) INSTANCE 1
- 1) INSTANCE 2
- 2) INSTANCE 3
- 3) INSTANCE 4
- 4) INSTANCE 5
- 5) INSTANCE 6
- 6) INSTANCE 7
- 7) INSTANCE 8
- 8) INSTANCE 9
- 9) INSTANCE 10
 

- Type 0 to 9 to show server options
- Type *all* to open an SSH into ALL server
- Type *refresh* to refresh instances with the same filter
- Type *restart* to go back to the first menu
- Type *close* to close this script
 

Input:
```
And finally:
```
####################
#    INSTANCE 5    #
####################
 

# Base informations
- Status: running
- Monitoring: enabled
- Launched: 2018-01-08 15:29:03
- Type: c5.2xlarge
- Ena supported: TRUE
 

# Network informations
- Zone: us-west-2c
- Public IP: 0.0.0.0
- Public DNS: ec2-0-0-0-0.us-west-2.compute.amazonaws.com
- Private IP: 172.0.0.0
- Private DNS: ec2-0-0-0-0.us-west-2.compute.amazonaws.com
 

# Security groups name
- 0) group-1
 

# Device informations
- Root Device: /dev/sda1

 
# Devices list
- 0)
    - Name: /dev/sda1
    - Status: attached
    - Delete On Termination: TRUE
 

- Type *ssh* to open an ssh connection to the server
- Type *close* to close this script
- Press ENTER to go back to the previous menu
 

Input:
``` 

## Authors

* **Rossano Baldi** - *Initial work* - [silvergit](https://github.com/RB-Consulting)

## License

This project is licensed under the GPLv2 License - see the [LICENSE.md](LICENSE.md) file for details
