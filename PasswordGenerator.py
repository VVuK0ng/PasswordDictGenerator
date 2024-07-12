#密码字典生成器
import exrex
import os

class PasswordGenerator:
    def __init__(self, url):
        self.url = url
        self.generate_password()

    def generate_password(self):
        passwords = []
        urls = self.url.replace("http://", "").replace("https://", "").replace("www.", "").replace(".com", "").replace(".cn", "").replace(".net", "").split(".")
        if not os.path.exists("./dict.txt"):
            with open("password_dict_generator/dict.txt", "w", encoding="utf-8") as f:
                f.writelines(["password\n", "admin\n", "root\n", "user\n"])

        with open("./dict.txt", "r", encoding="utf-8") as f:
            for line in f:
                for url in urls:
                    passwords+=list(exrex.generate(rf'{url}[!@#$]{{0,1}}{line.strip()}[\d]{{1,3}}'))

        with open("./password_dict.txt", "w", encoding="utf-8") as f:
            for password in passwords:
                f.write(password + "\n")
        
        print(f"Passwords generated and saved to password_dict.txt")
