def read_logs(filename):
    inputfile = filename
    outputfile = 'log_analitics.txt'
    messages = []
    apendix = "\n=======================================================\n"
    error_msg = [
    "Error messages: 1","Error messages: 2","Error messages: 3",
    "Error messages: 4","Error messages: 5","Error messages: 6",
    "Error messages: 7","Error messages: 8","Error messages: 9",
    ]
    with open(inputfile) as file_object:
        lines = file_object.readlines()

    for index, line in enumerate(lines):
        if ("ExitCode: 1") in line:
            log = lines[index - 23: index + 1]
            for line in log:
                messages.append(line)
            messages.append(apendix)

        for msg in error_msg:
            if msg in line:
                log = lines[index - 10: index + 1]
                for line in log:
                    messages.append(line)
                messages.append("\n" + apendix)

    with open(outputfile, 'w') as file_object:
        for message in messages:
            file_object.write(message) 

read_logs("update_log.txt")

