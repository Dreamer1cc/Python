def write_log_to_buffer(lines, index_from, index_to, messages, appendix):
    """write finded errors into the buffer string"""
    log = lines[index_from-1:index_to+1]
    for line in log:
        messages.append(line)
    messages.append("\n" + appendix)
    return messages
