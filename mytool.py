import os, time, random, socket

R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
C = '\033[96m'
W = '\033[97m'

os.system('clear')
print(f"{R}  _   _   _    ____ _  __ _____ ____    __  __  ___  ____  _____ ")
print(f" | | | | / \  / ___| |/ /| ____|  _ \  |  \/  |/ _ \|  _ \| ____|")
print(f" | |_| |/ _ \| |   | ' / |  _| | |_) | | |\/| | | | | | | |  _|  {G}")
print(f" |  _  / ___ \ |___| . \ | |___|  _ <  | |  | | |_| | |_| | |___ ")
print(f" |_| |_/_/   \_\____|_|\_\|_____|_| \_\ |_|  |_|\___/|____/|_____|{W}")
print(f"{C}                    [ Created by Mohmad - Elite Edition ]{W}\n")

name = input(f"{Y}الاسم بتاعك: {W}")
print(f"\n{G}مرحبا {name}، أهلا بيك في عالم الهكر!{W}")
time.sleep(1)

while True:
    print(f"\n{C}==== قائمة الأدوات ===={W}")
    print(f"{W}[1] فحص الـ IP بتاعي")
    print(f"[2] مولد باسورد قوي")
    print(f"[3] تشفير النص")
    print(f"[0] خروج")
    
    choice = input(f"\n{Y}اختار رقم: {W}")
    
    if choice == "1":
        try:
            ip = socket.gethostbyname(socket.gethostname())
            print(f"{G}[+] الـ IP المحلي: {ip}{W}")
            print(f"{G}[+] اسم الجهاز: {socket.gethostname()}{W}")
        except:
            print(f"{R}ما قدرت اجيب الـ IP{W}")
            
    elif choice == "2":
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%"
        pwd = "".join(random.choice(chars) for _ in range(12))
        print(f"{G}[+] الباسورد القوي: {pwd}{W}")
        
    elif choice == "3":
        txt = input("اكتب النص: ")
        enc = txt[::-1]
        print(f"{G}[+] النص المشفر: {enc}{W}")
        
    elif choice == "0":
        print(f"{R}وداعا يا {name} يا هكر!{W}")
        break
    else:
        print(f"{R}اختيار غلط!{W}")				
