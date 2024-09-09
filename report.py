def main():
    spacecraft={"name":"Sule's web spacecraft"}
    spacecraft.update({"distance":0.01, "orbit":"sun"})
    print(create_report(spacecraft))
    
def create_report(spacecraft):
    return f"""
    =================REPORT=====================
    Name: {spacecraft.get("name","Unknown")}
    Distance :{spacecraft.get("distance","Unknown")}AU
    Orbit:{spacecraft.get("orbit","Uknown")}
    ===========================================
    """

main()