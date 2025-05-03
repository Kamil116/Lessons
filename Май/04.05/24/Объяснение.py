import re

text = "Контакты: john@mail.com, alice@work.org, invalid-email, bob@sub.domain"

pattern = r'([a-z]+)@([a-z]+\.[a-z]+)'

matches = re.findall(pattern, text)
print("Все найденные email-адреса:")
# print(matches)
for username, domain in matches:
    print(f"  Имя: {username}, Домен: {domain}")
