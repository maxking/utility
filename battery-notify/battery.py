#############################################################
#Description:
#This files returns the remaining battery status to discharge
#from the input of command acpi
#
#Author:Abhilash Raj
#############################################################

import sys

def main():
    output = sys.argv
    bat_percent = output[4]
    bat_percent=bat_percent[0:-2]
    print bat_percent


if __name__=='__main__':
    main()
