def parse_linux_syslog(message):
    match = re.match('(?P<timestamp>\w+\s+\d+\s+\d+:\d+:\d+)\s+(?P<hostname>\S+)\s+(?P<program>\S+)\[(?P<pid>\d+)\]:\s+(?P<message>.+)', message)
    if match:
        fields = match.groupdict()
        cef_event = cef_header + f"Linux|{fields['hostname']}|{fields['program']}|1.0|{fields['message']}"
        return cef_event
    else:
        return None
