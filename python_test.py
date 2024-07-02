
import sys
import os
# import time
os.system('') # Added this to show color in windows terminal since windows doesn't use ANSI color codes
class bcolors:
    """
    Colors for console
    """
    HEADER = '\033[95m'
    YGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

def SN_search(file1, file2):
    # start = time.time()
    data = []
    with open(file1, 'r') as file1, open(file2, 'r') as file2:
        data1 = file1.readlines()
        data2 = file2.readlines()
    for each in data2:
        if each in data1:
                data.append(each)
    print('Do you want to save the matched SN list to a file (Y/N)?', end="")
    answer = input()
    if 'Y' in answer or 'y' in answer:
        with open('MATCHED_SN_LIST.txt', 'w') as matched_sn_list:
            matched_sn_list.writelines(data)
        print(f'Please check {bcolors.YGREEN}{os.getcwd()}{bcolors.ENDC} directory for {bcolors.YGREEN}MATCHED_SN_LIST.txt{bcolors.ENDC} file')
    else: 
        print('Too bad you did not save the list. Try again!')
    # end = time.time()
    # print(end-start)
    return

if __name__ == "__main__":
    file1 = sys.argv[1]
    file2 = sys.argv[2]
SN_search(sys.argv[1], sys.argv[2])


