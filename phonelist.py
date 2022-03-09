
print("""
 _                   _ _   ___            _ 
| | _____  ___ _ __ / | |_( _ )  ___  ___| |
| |/ / _ \/ _ \ '_ \| | __/ _ \ / _ \/ _ \ |
|   <  __/  __/ |_) | | || (_) |  __/  __/ |
|_|\_\___|\___| .__/|_|\__\___/ \___|\___|_|
              |_|                           
""")
def start():
    file = input("filename: ")
    file = open(file, "w+")
    ext = input("extension: ")
    digits = input("digits: ")
    added = "1" + digits
    converted = int(added)
    for i in range(converted):
        i = f'{i:0{len(digits)}}\n'
        i = str (i)
        file.write (ext + i)
start()



