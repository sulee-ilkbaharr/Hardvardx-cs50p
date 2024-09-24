import re
url = input("URL: ").strip()

# username = re.sub("https://twitter.com/", "", url)
# print(f"username: ",username)
if mathes := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url , re.IGNORECASE):
    print(f"username:", mathes.group(1))
    
    
# ?:  means dont caches this for to groping