import write as w


def search_for_parse_exec(lines):
    """Search for key words in file and write into buffer"""
    global index_from
    appendix = "\n=======================================================\n"
    messages = []
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
                    lines, index_from, index_to, messages, appendix
                    )
    return messages
