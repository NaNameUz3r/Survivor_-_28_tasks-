current_string = ''
curr_idx = 1
undo_buffer = []
buf_len = len(undo_buffer)

def BastShoe(command):

    global current_string
    global undo_buffer
    global curr_idx
    global buf_len

    if command == '':
        return current_string

    input_data = command.split(' ', 1)
    cmd = int(input_data[0])
    if len(input_data) > 1:
        string = input_data[1]
    else:
        string = ''

    if int(cmd) == 1:
        if string == '':
            return current_string
        append_str(string)
    elif int(cmd) == 2:
        if string == '' or current_string == '':
            return current_string
        else:
            delete(string)
    elif int(cmd) == 3:
        if string == '':
            return ''
        else:
            feedback_index(string)
    elif int(cmd) == 4 and string == '':
        if len(undo_buffer) == 0:
            return current_string
        undo()
    elif int(cmd) == 5  and string == '':
        if len(undo_buffer) == 0:
            return current_string
        redo()
    else:
        return current_string


def append_str(x_str):
    global current_string
    global undo_buffer
    global curr_idx
    global buf_len

    if curr_idx != 1:
        undo_buffer = undo_buffer[buf_len - curr_idx:buf_len - curr_idx + 1]
        curr_idx = 1

    if len(undo_buffer) == 0:
        current_string = x_str
        undo_buffer.append(current_string)
    else:
        current_string = undo_buffer[-1] + x_str
        undo_buffer.append(current_string)

    return current_string


def delete(N):
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

def feedback_index(x_str):
    global current_string

    try:
        if int(x_str) >= len(current_string) or int(x_str) < 0:
            return ''

        else:
            index = current_string[int(x_str)]
            print(index)
            return str(index)
    except ValueError:
        return ''

def undo():
    global current_string
    global undo_buffer
    global curr_idx

    if curr_idx == len(undo_buffer):
        curr_idx = len(undo_buffer)
    else:
        curr_idx += 1
    current_string = undo_buffer[len(undo_buffer) - curr_idx]

    return current_string


def redo():
    global current_string
    global undo_buffer
    global curr_idx

    if curr_idx == 1:
        current_string = undo_buffer[len(undo_buffer) - curr_idx]
    else:
        curr_idx -= 1
        current_string = undo_buffer[len(undo_buffer) - curr_idx]

    return current_string

