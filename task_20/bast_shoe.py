current_string = ''
curr_idx = 1
undo_buffer = []
buf_len = len(undo_buffer)

def BastShoe(command ='empty'):

    if command == 'empty':
        return current_string
    try:
        cmd = int(command[:1])
        string = command[2:]
    except ValueError:
        return current_string

    if cmd == 1:
        append_str(string)
    elif cmd == 2 and type(string) == int:
        delete(string)
    elif cmd == 3 and type(string) == int:
        feedback_index(string)
    elif cmd == 4 and len(string) == 0 and buf_len != 0:
        undo()
    elif cmd == 5 and len(string) == 0 and buf_len != 0:
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
    if int(N) >= str_len:
        current_string = ''
    else:
        current_string = current_string[:str_len - int(N)]
    undo_buffer.append(current_string)

    return current_string


def feedback_index(x_str):
    global current_string
    if int(x_str) > len(current_string) or int(x_str) < 0:
        return ''
    else:
        index = current_string[int(x_str)]
        return index


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

