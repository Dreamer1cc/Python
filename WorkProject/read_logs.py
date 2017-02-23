import read as r

while True:
    print("To Exit the programm input 'q'")
    filepath = input("Input file path: ")
    if filepath == 'q':
        break
    r.read_logs(filepath)
# r.read_logs("update_log.txt")

