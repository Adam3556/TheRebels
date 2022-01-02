print("  _______ _    _ ______   _____  ______ ____  ______ _       _____ ")
print(" |__   __| |  | |  ____| |  __ \|  ____|  _ \|  ____| |     / ____|")
print("    | |  | |__| | |__    | |__) | |__  | |_) | |__  | |    | (___  ")
print("    | |  |  __  |  __|   |  _  /|  __| |  _ <|  __| | |     \___ \ ")
print("    | |  | |  | | |____  | | \ \| |____| |_) | |____| |____ ____) |")
print("    |_|  |_|  |_|______| |_|  \_\______|____/|______|______|_____/ ")
#Welcome meessage
print("Only for Linux with Python installed!")
print("")
print("Welcome to THEREBELS hacking toolkit")
print("")
print("type HELP for help")
print("username-")
user_name =input()
if user_name == "TRl@mbda":
    print("Welcome λ")
if user_name == "guest":
    print("Welcome Guest")
if user_name == "HELP":
    print("-First type your username then press enter|If you want to enter as Guest in username type guest lowercase|If you want to quit code press CTRL-C")
#Username script
#End of username script
#Selection of tools
print("Wich tool do you wanna use?")
print("1-StormBreaker")
print("2-CamHackers-List of cameras")
print("3-I dont know")
print("4-still dont know")
print("")
user_name =input()
if user_name == "1":
    import StormBreaker
if user_name == "2":
    import camhackers
if user_name == "3":
    import gmail
if user_name == "4":
    print("Not Working")

