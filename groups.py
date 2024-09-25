import re
location={"+1":"United Sattes and Canada","+62":"Indonesia","+505":"Nicaragua"}

def main():
    pattern= r"(?P<country_group>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Number:")
    
    match = re.search(pattern,number)
    if match:
        country_code = match.group("country_group")
        print(location[country_code])
    else:
        print("Invalid")
        
main()