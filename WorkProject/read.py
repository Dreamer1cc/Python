import write as w
def read_logs(filename):
    """function return file, that contains only errors from logs"""
    inputfile = filename.replace('"', ' ')
    inputfile = inputfile.strip()
    outputfile = 'log_analysis.txt'
    messages = []
    apendix = "\n=======================================================\n"
    try:
        with open(inputfile) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        msg = "Sorry, the file " + inputfile + " does not exist."
        print(msg)
    else:
        for index, line in enumerate(lines):
            begin_line = line.find("Executing script:")
            end_line = line.find("Error messages: ")
            if begin_line != -1:
                index_from = index
            if end_line != -1:
                index_to = index
                er_count = int(line[end_line+16:end_line+17])
                if er_count != 0:
                    w.write_log_to_buffer(
                        lines, index_from, index_to, messages, apendix
                        )
            begin_line = line.find("Running Db")
            end_line = line.find("ExitCode: ")
            if begin_line != -1:
                index_from = index
            if end_line != -1:
                index_to = index
                er_count = int(line[end_line+10:end_line+11])
                if er_count != 0:
                    w.write_log_to_buffer(
                        lines, index_from, index_to, messages, apendix
                        )

        with open(outputfile, 'w') as file_object:
            for message in messages:
                file_object.write(message) 
        print("Errors wrote into the file " + outputfile)

# read_logs("update_log.txt")

