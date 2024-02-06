import os
import time
import sys
import itertools
import threading
def nmap_only_port_scan(ip):
    os.system(f"nmap -Pn {ip}")

def nmap_easy(ip):
    print("------starting namp--------")
    os.system(f"nmap -p- -T4 {ip} -vv")
    print("scan ended")

def nmap_medium(ip):
    print("------starting namp--------")
    os.system(f"nmap -p- -A -T4 {ip} -vv -sS ")
    print("scan ended")

def nmap_hard(ip):
    print("------starting namp--------")
    os.system(f"nmap -p- -A -sC -T4 -sS {ip} -vv -oX test.txt")
    print("scan ended")

def specific_port_nmap_easy(ip,port):
    print("------starting namp--------")
    os.system(f"nmap -p{port} {ip} -vv")
    print("scan ended")

def specific_port_nmap_medium(ip,port):
    print("------starting namp--------")
    os.system(f"nmap -p{port} -T4 -A {ip} -vv -sS ")
    print("scan ended")

def specific_port_nmap_hard(ip,port):
    print("------starting namp--------")
    os.system(f"nmap -p{port} -A -T4 -sC -sS {ip} -vv -oX test.txt")
    print("scan ended")

def main_scanning_perform():
    print("")
    print("what type of terminology do you want to use "
          "\n1-first scan only port and see each port privately "
          "\nor "
          "\n2-start with full port scanning from basic only")
    only_scan = input("what type of method do you want to perform(1or2)-")
    if only_scan == '1':
        while_loop1 = True
        while while_loop1:
            hello = input("do you want to scan any specific port?(yes/no)")
            if hello == 'yes':
                port = input("what is port number that you have seen open in starting?")
                tu = input("which one e-easy/m-medium/h-hard")
                if tu == 'e':
                    specific_port_nmap_easy(ip_input, port)
                elif tu == 'm':
                    specific_port_nmap_medium(ip_input, port)
                elif tu == 'h':
                    specific_port_nmap_hard(ip_input, port)
                else:
                    print("wrong input")
            elif hello == 'no':
                print("thanks for using automated nmap tool")
                start_ffu = input("want to start ffuf?(y/n)")
                if start_ffu =='y':
                   scanning_ffuf(ip_input)
                elif start_ffu =='n':
                    while_loop1 = False
                    print("thanks for runnnig automated script")
                else:
                    print("wrong input")


    elif only_scan=='2':
        nmap_type_input = input("enter what type of scan do you want to scan?(e-easy/m-medium/h-hard)")
        if nmap_type_input == 'e':
            nmap_easy(ip_input)
            start_ffuf = input("want to start ffuf?(y/n)")
            if start_ffuf == 'y':
                scanning_ffuf(ip_input)
            elif start_ffuf == 'n':
                print("thanks for running automated script")
            else:
                print("wrong input")
                scanning_ffuf(ip_input)
        elif nmap_type_input == 'm':
            nmap_medium(ip_input)
            start_ffuff = input("want to start ffuf?(y/n)")
            if start_ffuff == 'y':
                scanning_ffuf(ip_input)
            elif start_ffuff == 'n':
                print("thanks for running automated script")
            else:
                print("wrong input")
                scanning_ffuf(ip_input)
        elif nmap_type_input == 'h':
            nmap_hard(ip_input)
            start_ffufff = input("want to start ffuf?(y/n)")
            if start_ffufff == 'y':
                scanning_ffuf(ip_input)
            elif start_ffufff == 'n':
                print("thanks for running automated script")
            else:
                print("wrong input")
                scanning_ffuf(ip_input)
        else:
            again = input("wrong input want to try again?(y/n)")
            if again=="y":
                scanning_ffuf(ip_input)
            elif again=='n':
                print("")
            else:
                print("wrong input try again.")
                scanning_ffuf(ip_input)
    else:
        main_scanning_perform()



def basic_directory_ffuf_scan(ip):
    directory = input("enter full directory path of list for ffuf scan that you want to scan on it-")
    os.system(f"ffuf -u http://{ip}/FUZZ -w {directory} -v -c")


def extention_ffuf_scan(ip):
    directory = input("enter full directory path of list for ffuf scan that you want to scan on it-")
    extention = ' .txt,.php'
    os.system(f"ffuf -u http://{ip}/FUZZ -w {directory} -v -c -e{extention}")


def sub_directory_ffuf_enumenation(ip):
    main_directory = input("what is the main directory that you have found?")
    directory = input("enter the subirectory that you have to find out")
    os.system(f"ffuf -u http://{ip}/{main_directory}/FUZZ -w {directory} -v -c ")


def sub_ki_sub_directory_ffuf_enumenation(ip):
    main_directory = input("what is the main directory that you have found?")
    main_directory2 = input("what is the main directory 2 that you have found?")
    directory = input("enter full directory path of list for ffuf scan that you want to scan on it-")
    os.system(f"ffuf -u http://{ip}/{main_directory}/{main_directory2}/FUZZ -w {directory} -v -c ")

def any_other_ffuf_attack():
    hello = input("want to enumerate more?(y/n)")
    if hello=='y':
        scanning_ffuf(ip_input)
    elif hello=='n':
        print("thanks for running ffuf")
        exit()
    else:
        print("wrong input")
        scanning_ffuf(ip_input)


def scanning_ffuf(ip):
    print("what type of ffuf attack do you want to do?"
          "\n1-single directory attack?"
          "\n2-sub directory attack?"
          "\n3-put a extention in single directory?"
          "\n4-double sub directory attack?"
          "\n5-exit")
    type_of_ffuf = input("enter what type of attack you want to attack?(1/2/3/4)")
    on = True
    while on:
        if type_of_ffuf=='1':
            basic_directory_ffuf_scan(ip_input)
            any_other_ffuf_attack()
        elif type_of_ffuf=='2':
            sub_directory_ffuf_enumenation(ip_input)
            any_other_ffuf_attack()
        elif type_of_ffuf=='3':
            extention_ffuf_scan(ip_input)
            any_other_ffuf_attack()
        elif type_of_ffuf=='4':
            sub_ki_sub_directory_ffuf_enumenation(ip_input)
            any_other_ffuf_attack()
        elif type_of_ffuf=="5":
            print("thanks for running ffuf.")
            on = False
        else:
            print("wrong input")
            scanning_ffuf(ip_input)

def animation():
    done = False

    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rloading ' + c)
            sys.stdout.flush()
            time.sleep(0.1)

    t = threading.Thread(target=animate)
    t.start()

    # long process here
    time.sleep(5)
    done = True


TGREEN = '\033[34m'
TWHITE = '\033[31m'
print(TWHITE, TGREEN)
print("this tool is currently for scanning network and directory enumenation")
animation()
ip_input = input("\nenter ip address-")
print("please wait for sometime as it initially find all port that is open on server")
time.sleep(2)

print("nmap starting...................")
time.sleep(2)

nmap_only_port_scan(ip_input)
print("\n  ---------------------------warning for medium and hard scan your system should be in root---------------------------               ")
main_scanning_perform()






