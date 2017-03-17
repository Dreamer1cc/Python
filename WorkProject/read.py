import search_exec as se
import search_db as db


def read_logs(filename):
    """function return file, that contains only errors from logs"""
    inputfile = filename.replace('"', ' ')
    inputfile = inputfile.strip()
    outputfile = 'log_analysis.txt'

    try:
        with open(inputfile) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        msg = "Sorry, the file " + inputfile + " does not exist."
        print(msg)
    else:
        messages = db.search_for_parse_db(lines)
        messages += se.search_for_parse_exec(lines)

        with open(outputfile, 'w') as file_object:
            for message in messages:
                file_object.write(message)
        print("Errors wrote into the file " + outputfile)
