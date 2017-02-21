def read_logs(filename):
    inputfile = filename
    outputfile = 'log_analitics.txt'
    messages = []
    apendix = "\n=======================================================\n"
    with open(inputfile) as file_object:
        lines = file_object.readlines()
    for index, line in enumerate(lines):
        if ("ExitCode: 1") in line:
            log = lines[index - 10: index + 1]
            for line in log:
                messages.append(line)
            messages.append(apendix)
        elif "Error messages: 1" in line:
            log = lines[index - 10: index + 1]
            for line in log:
                messages.append(line)
            messages.append(apendix)
        elif "Error messages: 2" in line:
            log = lines[index - 10: index + 1]
            for line in log:
                messages.append(line)
            messages.append(apendix)
        elif "Error messages: 3" in line:
            log = lines[index - 10: index + 1]
            for line in log:
                messages.append(line)
            messages.append(apendix)
        elif "Error messages: 4" in line:
            log = lines[index - 10: index + 1]
            for line in log:
                messages.append(line)
            messages.append(apendix)
        elif "Error messages: 5" in line:
            log = lines[index - 10: index + 1]
            for line in log:
                messages.append(line)
            messages.append(apendix)
        elif "Error messages: 6" in line:
            log = lines[index - 10: index + 1]
            for line in log:
                messages.append(line)
            messages.append(apendix)
        elif "Error messages: 7" in line:
            log = lines[index - 10: index + 1]
            for line in log:
                messages.append(line)
            messages.append(apendix)
        elif "Error messages: 8" in line:
            log = lines[index - 10: index + 1]
            for line in log:
                messages.append(line)
            messages.append(apendix)
        elif "Error messages: 9" in line:
            log = lines[index - 10: index + 1]
            for line in log:
                messages.append(line)
            messages.append(apendix)

    with open(outputfile, 'w') as file_object: 
        for message in messages:
            file_object.write(message) 

read_logs("update_log.txt")

