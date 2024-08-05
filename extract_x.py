import re
url = input("URL: ").strip()

#username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
#print(f"Username: {username}")

if matches := re.search(r"^https?://?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(F"Username:", matches.group(1))