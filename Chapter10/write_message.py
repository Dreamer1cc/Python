def read_logs(filename):
    inputfile = filename
    outputfile = 'log_analitics.txt'
    messages = []
    with open(inputfile) as file_object:
        lines = file_object.readlines()
    for line in lines:
        if ("ExitCode: 1") in line:
            message = "ExitCode: 1. Error in Object files"
            messages.append(message)
        else:
            if "Error messages: 1" in line:
                messages.append("Error messages: 1")
            elif "Error messages: 2" in line:
                messages.append("Error messages: 2")
            elif "Error messages: 3" in line:
                messages.append("Error messages: 3")
            elif "Error messages: 4" in line:
                messages.append("Error messages: 4")
            elif "Error messages: 5" in line:
                messages.append("Error messages: 5")
            elif "Error messages: 6" in line:
                messages.append("Error messages: 6")
            elif "Error messages: 7" in line:
                messages.append("Error messages: 7")
            elif "Error messages: 8" in line:
                messages.append("Error messages: 8")
            elif "Error messages: 9" in line:
                messages.append("Error messages: 9")

    with open(outputfile, 'w') as file_object: 
        for message in messages:
            file_object.write("\n" + message + "; ") 

#read_logs("update_log.txt")