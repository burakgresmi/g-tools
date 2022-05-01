import os

def menu():

    print(""" 
                                                                       
   .oooooo.            ooooooooooooo   .oooooo.     .oooooo.   ooooo         .oooooo..o 
 d8P'  `Y8b           8'   888   `8  d8P'  `Y8b   d8P'  `Y8b  `888'        d8P'    `Y8 
888                        888      888      888 888      888  888         Y88bo.      
888                        888      888      888 888      888  888          `"Y8888o.  
888     ooooo 8888888      888      888      888 888      888  888              `"Y88b 
`88.    .88'               888      `88b    d88' `88b    d88'  888       o oo     .d8P 
 `Y8bood8P'               o888o      `Y8bood8P'   `Y8bood8P'  o888ooooood8 8""88888P'  
                                                                                                                                                                          
========================================
Coded by Burak Gökkaya
Telegram: t.me/androedit
İnstagram: instagram.com/burakgresmi
Versiyon: 31.0
----
BURAK GÖKKAYA | @burakgresmi
----
==========================================
00. Yararlı Tooları Tek Komutla İndirin.
------------------------------------------
1.  Kurulum: Nmap 
2.  Kurulum: Hydra
3.  Kurulum: SQLMap
4.  Kurulum: Metasploit
5.  Kurulum: ngrok
6.  Kurulum: Kali Nethunter
7.  Kurulum: angryFuzzer
8.  Kurulum: Red_Hawk
9.  Kurulum: Weeman
10. Kurulum: IPGeoLocation
11. Kurulum: Cupp
12. Instagram Bruteforcer (instahack)
13. Twitter Bruteforcer   (TwitterSniper)
14. Kurulum: Ubuntu
15. Kurulum: Fedora
16. Kurulum: viSQL
17. Kurulum: Hash-Buster
18. Kurulum: D-TECT
19. Kurulum: routersploit
------------------------------------------
99. Çıkış
==========================================
""")

loop = True

while loop:
    menu()
    what = input("#: ")
    if what == "00":
        print("================================")
        print("Tek Tıklamayla İndırin: nmap, hydra, sqlmap, metasploit, ngrok, crazyFuzzer, red_hawk, weeman, IPGeoLocation, cupp, instahack, TwitterSniper, Hash-Buster, D-TECT, routersploit ve viSQL ")
        print("----------------")
        hm = input("[?] Do you want to continue? (y/n): ")
        print("================================")
        if hm == "y":
            print("========================================================")
            print("[+] Bekleyiniz...")
            print("Çünkü bu uzun zaman alacaktır.")
            print("========================================================")
            os.system("pkg update")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pkg install -y python2")
            os.system("pkg install -y wget")
            os.sysetm("pkg install -y nmap")
            os.system("pkg install -y hydra ")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg install wget")
            os.system("cd /data/data/com.termux/files/home && wgethttps://github.com/rapid7/metasploit-framework")
            os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
            os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
            os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
            os.system("cd /data/data/com.termux/files/home && bundle install")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/inconshreveable/ngrok")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer")
            os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
            os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home && pip2 install requests")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y php")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y python2")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman")
            os.system("cd /data/data/com.termux/files/home && cd weeman")
            os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation")
            os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
            os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone hhttps://github.com/Mebus/cupp")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pkg install -y nano")
            os.system("pip install requests")
            os.system("pip install beautifulsoup4")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/rahnumaa18/https-github.com-avramit-Instahack")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pip install mechanicalsoup")
            os.system("pkg install -y nano")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ethicalhackeragnidhra/viSQL")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/s0md3v/Hash-Buster")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/shawarkhanethicalhacker/D-TECT-1")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/threat9/routersploit")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            os.system("clear")
            print("========================================")
            print("[+] Her Şey Başarıyla Kuruldu")
            print("[+] Coded by Burak Gökkaya!!! Saygılarımla..")
            print("========================================")
        else:
            rmenu = input("[?] Ana Menüye Dön? (y/n): ")
            if rmenu == "y":
                menu()
            else:
                break
    if what == "1":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y nmap")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] nmap Başarıyla Kuruldu :)")
        print("[+] Başlatmak İçin 'nmap' Yazın")
        print("====================================")
        rmenu = input("[?] Ana Menüye Dön? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "2":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y hydra")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evildevill/Hydra_Termux")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] hydra Başarıyla Kuruldu :)")
        print("[+] Hydra_Termux klasörüne gidi başlamak için 'bash Hydra.sh' yazın")
        print("====================================")
        rmenu = input("[?] Ana Menüye Dön? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "3":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] SQLMap Başarıyla Kuruldu :)")
        print("[+] SQLMap Klasörüne Gidin ve Başlamak İçin 'python2 sqlmap.py' Yazın")
        print("====================================")
        rmenu = input("[?] Ana Menüye Dön? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "4":
        os.system("pkg install -y wget")
        os.system("cd /data/data/com.termux/files/home && wget https://github.com/rapid7/metasploit-framework")
        os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
        os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
        os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
        os.system("cd /data/data/com.termux/files/home && bundle install")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Metasploit Başarıyla Kuruldu :)")
        print("[+] Başlatmak İçin 'msfconsole' Yazın")
        print("====================================")
        rmenu = input("[?] Ana Menüye Dön? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "5":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/inconshreveable/ngrok")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] ngrok Başarıyla Kuruldu :)")
        print("[+] ngrok Klasörüne Gidin ve Başlamak İçin './ngrok http 80' Yazın.")
        print("====================================")
        rmenu = input("[?] Ana Menüye Dön? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "6":
        os.system("pkg update -y")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Hax4us/Nethunter-In-Termux")
        os.system("cd /data/data/com.termux/files/home && cd Nethunter-In-Termux && chmod +x kalinethunter")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Nethunter Başarıyla Kuruldu :)")
        print("[+] Nethunter-In-Termux Klasörüne Gidin ve Başlamak İçin './kalinethunter' Yazın.")
        print("====================================")
        rmenu = input("[?] Ana Menüye Dön? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "7":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer")
        os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
        os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home && pip2 install requests")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] angryFuzzer Başarıyla Kuruldu :)")
        print("[+] angryFuzzer klasörüne gidin ve başlamak için 'python2 angryFuzzer.py' yazın.")
        print("====================================")
        rmenu = input("[?] Ana Menüye Dön? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "8":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y php")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] RED_HAWK Başarıyla Kuruldu :)")
        print("[+] RED_HAWK klasörüne gidin ve başlamak için 'php rhawk.php' yazın.")
        print("====================================")
        rmenu = input("[?] Ana Menüye Dön? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "9":
        os.system("pkg update -y")
        os.system("pkg install -y python2")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman")
        os.system("cd /data/data/com.termux/files/home && cd weeman")
        os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] weeman Başarıyla Kuruldu :)")
        print("[+] Weeman klasörüne gidin ve başlamak için 'python2 weeman.py' yazın.")
        print("====================================")
        rmenu = input("[?] Ana Menüye Dön? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "10":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation")
        os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
        os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] IPGeoLocation Başarıyla Kuruldu :)")
        print("[+] IPGeoLocation klasörüne gidin ve başlamak için 'python ipgeolocation.py' yazın.")
        print("====================================")
        rmenu = input("[?] Ana Menüye Dön? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "11":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp")
        print("====================================")
        print("[+] Cupp Başarıyla Kuruldu :)")
        print("[+] Cupp klasörüne gidin ve başlamak için 'python cupp.py' yazın.")
        print("====================================")
        rmenu = input("[?] Ana Menüye Dön? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "12":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pkg install -y nano")
        os.system("pip install requests")
        os.system("pip install beautifulsoup4")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/rahnumaa18/https-github.com-avramit-Instahack")
        print("====================================")
        print("[+] Instahack Başarıyla Kuruldu :)")
        print("[+] instahack klasörüne gidin ve başlamak için 'python hackinsta.py' yazın.")
        print("====================================")
        rmenu = input("[?] Ana Menüye Dön? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "13":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pip install mechanicalsoup")
        os.system("pkg install -y nano")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper")
        print("====================================")
        print("[+] TwitterSniper Başarıyla Kuruldu :)")
        print("[+] Başlamak için TwitterSniper klasörüne gidin ve 'python TwitterSniper.py' yazın.")
        print("====================================")
        rmenu = input("[?] Ana Menüye Dön? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "14":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Neo-Oli/termux-ubuntu")
        os.system("cd /data/data/com.termux/files/home && cd termux-ubuntu && bash ubuntu.sh")
        print("====================================")
        print("[+] Ubuntu Başarıyla Kuruldu :)")
        print("[+] termux-ubuntu klasörüne gidin ve başlamak için './start.sh' yazın.")
        print("====================================")
        rmenu = input("[?] Ana Menüye Dön? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "15":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y wget")
        os.system("apt update && apt install wget -y && /data/data/com.termux/files/usr/bin/wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh")
        print("====================================")
        print("[+] Fedora Başarıyla Kuruldu :)")
        print("[+] Başlamak için 'sh termux-fedora.sh f26_arm64' veya 'sh termux-fedora.sh f26_arm' yazın.")
        print("====================================")
        rmenu = input("[?] Ana Menüye Dön? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "16":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ethicalhackeragnidhra/viSQL")
        print("====================================")
        print("[+] viSQL Başarıyla Kuruldu :)")
        print("[+] Başlamak için viSQL klasörüne gidin ve 'python2 viSQL.py --help' yazın.")
        print("====================================")
        rmenu = input("[?] Ana Menüye Dön? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "17":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/s0md3v/Hash-Buster")
        print("====================================")
        print("[+] Hash-Buster Başarıyla Kuruldu :)")
        print("[+] Hash-Buster klasörüne gidin ve başlamak için 'python2 hash.py' yazın.")
        print("====================================")
        rmenu = input("[?] Ana Menüye Dön? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "18":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/shawarkhanethicalhacker/D-TECT-1")
        print("====================================")
        print("[+] D-TECT-1 Başarıyla Kuruldu :)")
        print("[+] D-TECT-1 klasörüne gidin ve başlamak için 'python2 d-tect.py' yazın.")
        print("====================================")
        rmenu = input("[?] Ana Menüye Dön? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "19":    
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/threat9/routersploit")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            print("====================================")
            print("[+] routersploit Başarıyla Kuruldu :)")
            print("[+] Routersploit klasörüne gidin ve başlamak için 'python2 rsf.py' yazın.")
            print("====================================")
            rmenu = input("[?] Ana Menüye Dön? (y/n): ")
            if rmenu == "y":
                menu()
            else:
                break
    elif what == "99":
        print("Coded by BURAK GÖKKAYA!! SAYGILARIMLA..")
        break
