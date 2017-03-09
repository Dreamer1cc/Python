import read as r

while True:
    print("To Exit the program input 'q'")
    file_path = input('Input file path: ')
    if file_path == 'q':
        break
    r.read_logs(file_path)
# r.read_logs("update_log.txt") sdf
