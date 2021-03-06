current_string = ''
curr_idx = 1
undo_buffer = []
buf_len = len(undo_buffer)

def BastShoe(command):

    if command == '':
        return current_string

    try:
        input_data = command.split(' ', 1)
        cmd = int(input_data[0])
    except ValueError:
        return current_string

    if len(input_data) > 1:
        string = input_data[1]
    else:
        string = ''

    if int(cmd) == 1:
        if string == '':
            return current_string
        else:
            add_text(string)

    elif int(cmd) == 2:
        if string == '' or current_string == '':
            return current_string
        else:
            cut_from_end(string)

    elif int(cmd) == 3:
        if string == '':
            return ''
        else:
            index = get_symbol_by_index(string)
            return index

    elif int(cmd) == 4 and string == '':
        if len(undo_buffer) == 0:
            return current_string
        else:
            undo_last_action()

    elif int(cmd) == 5 and string == '':
        if len(undo_buffer) == 0:
            return current_string
        else:
            redo_last_undo()
    else:
        return current_string

    return current_string


def add_text(S, string, ):
    global current_string
    global undo_buffer
    global curr_idx
    global buf_len

    if curr_idx != 1:
        undo_buffer = undo_buffer[buf_len - curr_idx:buf_len - curr_idx + 1]
        curr_idx = 1

    if len(undo_buffer) == 0:
        current_string = S
        undo_buffer.append(current_string)
    else:
        current_string = undo_buffer[-1] + S
        undo_buffer.append(current_string)

    return current_string


def cut_from_end(N):
    global current_string
    global undo_buffer
    global curr_idx
    global buf_len

    if curr_idx != 1:
        undo_buffer = undo_buffer[buf_len - curr_idx:buf_len - curr_idx + 1]
        curr_idx = 1

    str_len = len(current_string)
    try:
        if int(N) >= str_len:
            current_string = ''
        else:
            current_string = current_string[:str_len - int(N)]
        undo_buffer.append(current_string)

        return current_string
    except ValueError:
        return current_string


def get_symbol_by_index(i):
    global current_string

    try:

        if int(i) >= len(current_string) or int(i) < 0:
            return ''
        else:
            index = current_string[int(i)]
            return str(index)
    except ValueError:
        return ''


def undo_last_action():
    global current_string
    global undo_buffer
    global curr_idx

    if curr_idx == len(undo_buffer):
        curr_idx = len(undo_buffer)
    else:
        curr_idx += 1
    current_string = undo_buffer[len(undo_buffer) - curr_idx]

    return current_string


def redo_last_undo():
    global current_string
    global undo_buffer
    global curr_idx

    if curr_idx == 1:
        current_string = undo_buffer[len(undo_buffer) - curr_idx]
    else:
        curr_idx -= 1
        current_string = undo_buffer[len(undo_buffer) - curr_idx]

    return current_string

