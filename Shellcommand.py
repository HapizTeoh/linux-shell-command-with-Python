import os
import sys
import shutil

print("Welcome to ASEAN shell command menu")
print("\nPlease choose your preferred language \n \n1.Bahasa Malaysia \n2.Vietnam \n3.Philippines ")
language = {1: "Bahasa Malaysia", 2: " Vietnamese", 3: "Filipino"}
Bahasa =["Direktori semasa: ","\nTukar direktori ke: ","Berjaya! Direktori semasa: ","Fail dalam direktori: ","Fail untuk ditukar nama: ","Nama fail baru: ","Operasi Berjaya! "
    ,"Sumber direktori: ","Destinasi direktori : ","Operasi ke %s gagal!", "Operasi ke %s bejaya!","Membaca fail...","Destinasi fail: ","Menyusun isi fail...","Keluar program..."]
Vietnam =["Thư mục hiện tại: ","\nThay đổi thư mục thành: ","Sự thành công! Thư mục hiện tại: ",
"Tập tin trong thư mục: ","Tập tin được đổi tên: ","Tên tệp mới", "Hoạt động thành công!",
"thư mục nguồn: ","Danh mục nơi nhận","Hoạt động %s thất bại!","Hoạt động %s thành công",
"đọc tập tin...","tập tin đích: ","sắp xếp nội dung tập tin...","chương trình thoát..."]
Philippines = ["kasalukuyang direktoryo: ","baguhin ang direktoryo sa: ","Tagumpay! kasalukuyang direktoryo: ","mga file sa direktoryo: ","file na mapalitan ng pangalan: ",
	"Bagong pangalan ng file: ","tagumpay ng operasyon!","direktoryo ng mapagkukunan: ","direktoryo ng patutunguhan: ","nabigo ang operasyon %s",
	"tagumpay ng operasyon %s","Pagbabasa ng file...","Patutunguhan ng file: ","Pag-uuri ng nilalaman ng file...","Paglabas ng programa..."]
option = {1: Bahasa, 2: Vietnam, 3: Philippines}


def inputNumber(message):           #function to only accept input as integer
        while True:
            try:
                choice = int(input(message))
            except ValueError:
                print("Not an integer! Please reenter")
                continue
            else:
                return choice
                break

while True:         #loop to prompt input within range
    choice = inputNumber("\nSelect your language: ")
    if choice <1 or choice >3:
        print("Please choose between range!")
    else:
        break

print("Language select success! " + language[choice] + " is selected\n")   #acknowledge selected language

def menuselect (choice):  #function to provide menu option based on language selected
    Bahasa = ["1.Papar direktori","2.Tukar direktori","3.Tukar nama direktori","4.Salin direktori","5.Padam direktori","6.Cipta direktori","7.Papar isi file","8.Susun isi file","9.Keluar"]
    Philippines = ["1.direktoryo ng listahan", "2.baguhin ang direktoryo","3.palitan ang pangalan ng direktoryo","4. direktoryo ng kopya","5.alisin ang direktoryo","6.lumikha ng direktoryo","7.basahin ang nilalaman ng file","8.ayusin ang nilalaman ng file","9.labasan"]
    Vietnam = ["1.Danh sách thư mục","2.Thay đổi thư mục","3.đổi tên thư mục","4.sao chép thư mục","5.xóa thư mục","6.Tạo thư mục","7.đọc nội dung tập tin","8.dừng nội dung tập tin","9.lối ra"]
    menuLang = {1:"\nPilih dari menu: ", 2: "\nChọn từ menu: ",3: "\nPumili mula sa menu: "}
    errorLang = {1: "Pilihan luar rangkaian!", 2: "Vui lòng chọn giữa phạm vi!",3: "Mangyaring pumili sa pagitan ng saklaw!"}
    option = {1: Bahasa, 2: Vietnam, 3: Philippines}

    for i in option[choice]:
        print(i)

    while True:
        menu = inputNumber(menuLang[choice])
        if menu < 1 or menu > 9:
            print(errorLang[choice])
        else:
            break

    return menu

def copytree(src, dst, symlinks=False, ignore=None): #function for copying directories
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

while True:           #main loop for all cases of selected menu
    selected = menuselect(choice)
    if selected == 1:
        print(option[choice][0] + os.getcwd())
        print(os.system("ls"))
    elif selected == 2:
        print(option[choice][0] + os.getcwd())
        chg = input(option[choice][1])
        os.chdir(chg)
        print(option[choice][2] + os.getcwd())
    elif selected == 3:
        print(option[choice][0] + os.getcwd())
        print(option[choice][3])
        print(os.system("ls"))
        ren = input(option[choice][4])
        new = input(option[choice][5])
        os.rename(ren,new)
        print(option[choice][6])
    elif selected == 4:
        print(option[choice][0] + os.getcwd())
        print(option[choice][3])
        print(os.system("ls"))
        ori = input(option[choice][7])
        new = input(option[choice][8])
        try:
            copytree(ori,new)
        except OSError:
            print(option[choice][9] %new)
        else:
            print(option[choice][10] %new)
    elif selected == 5:
        path = input(option[choice][7])
        try:
            shutil.rmtree(path)
            print(option[choice][6])
        except OSError as e:
            print("Error: %s-%s." % (e.filename, e.strerror))
    elif selected == 6:
        path = input(option[choice][8])
        try:
            os.mkdir(path)
        except OSError:
            print(option[choice][9] %path)
        else:
            print(option[choice][10] % path)

    elif selected == 7:
        print(option[choice][11])
        path = input(option[choice][12])
        os.system("cat "+ path)

    elif selected == 8:
        print(option[choice][13])
        path = input(option[choice][12])
        os.system("sort " + path )

    elif selected == 9:
        sys.exit(option[choice][14])

print (option[choice][14])









