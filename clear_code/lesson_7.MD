########################################################
# 7.1
########################################################

Было: draw_result
Стало: is_draw
------------------------------------------------------------
Было: global_match_flag
Стало: is_global_match
------------------------------------------------------------
Было: match_flag
Стало: is_local_match
------------------------------------------------------------
### Было:

flag = True
while flag:
    flag = False
    for i in range(len(data) - 2):
        piece = data[i:i+3]

        if not piece[0] < piece[1] < piece[2]:
            refer = data[i:i+3]
            data[i:i+3] = swapper(piece)
            if data[i:i+3] == refer:
                flag = False
            else:
                flag = True

### Стало:

keep_searching = True
while keep_searching:
    keep_searching = False
    for i in range(len(data) - 2):
        slice_to_twist = data[i:i+3]

        if not slice_to_twist[0] < slice_to_twist[1] < slice_to_twist[2]:
            reference = data[i:i+3]
            data[i:i+3] = swapper(slice_to_twist)
            if data[i:i+3] == reference:
                keep_searching = False
            else:
                keep_searching = True


(ps. мне стыдно на это смотреть. Правильно будет переписать программу
с нуля и придумать алгоритм лучше)

------------------------------------------------------------

### Было:

check = True
    for i in range(len(values_list)):
        if values_list[i] == repeats:
            continue
        elif values_list[i] - 1 == repeats and check or (
            values_list[i] - 1 == 0 and check
        ):
            check = False
            continue
        else:
            break

### Стало:

for i in range(len(values_list)):
    if values_list[i] == repeats:
        continue
    elif values_list[i] - 1 == repeats or (
        values_list[i] - 1 == 0
    ):
        continue
    else:
        break
else:
    return True
return False


(кровавые слёзы. Кто это кодил?)
------------------------------
Было: not_caprured = True
Стало: is_caprured = False
------------------------------

########################################################
# 7.2
########################################################

### Было:

def TankRush(H1, W1, S1, H2, W2, S2):

    field = S1.split()
    to_find = S2.split()

    global_match_flag = False

    for window_y in range(len(field) - len(to_find) + 1):

        if global_match_flag:
            break

        for window_x in range(len(field[0]) - len(to_find[0]) + 1):
            match_flag = True
            for find_y in range(len(to_find)):
                for find_x in range(len(to_find[0])):
                    if field[window_y + find_y][window_x + find_x] != to_find[find_y][find_x]:
                        match_flag = False

            if match_flag:
                global_match_flag = True
                break

    return global_match_flag


### Стало:

def TankRush(H1, W1, S1, H2, W2, S2):

    field = S1.split()
    to_find = S2.split()

    global_found= False

    for window_y in range(len(field) - len(to_find) + 1):

        if global_found:
            break

        for window_x in range(len(field[0]) - len(to_find[0]) + 1):
            found = True
            for find_y in range(len(to_find)):
                for find_x in range(len(to_find[0])):
                    if field[window_y + find_y][window_x + find_x] != to_find[find_y][find_x]:
                        found = False

            if match_flag:
                global_found = True
                break

    return global_match_flag

### взглянул на свежий глаз, и мне кажется, что от flag вообще лучше избавиться
### как его не назови. Похоже что здесь вполне уместно применение "стандартных"
### имен булевых переменных.

--------------------------------------------------------

### Было.... flag...

### Стало:

found = True
while found:
    found = False
    for i in range(len(data) - 2):
        piece = data[i:i+3]

        if not piece[0] < piece[1] < piece[2]:
            refer = data[i:i+3]
            data[i:i+3] = swapper(piece)
            if data[i:i+3] == refer:
                found = False
            else:
                found = True

### Стало_2:

brute_force_success = True
  while brute_force_success:
      brute_force_success = False
      for i in range(len(data) - 2):
          piece = data[i:i+3]

          if not piece[0] < piece[1] < piece[2]:
              refer = data[i:i+3]
              data[i:i+3] = swapper(piece)
              if data[i:i+3] == refer:
                  brute_force_success = False
              else:
                  brute_force_success = True

# Здесь не какое то конкретное значение, поэтому found называть
# всё таки не корректно. Пусть лучше будет такое длинное название
# , тем не менее - оно не слишком длинное (19 с подчеркиваниями)
# но говорящее (наверное...)

--------------------------------------------------------

### Было:

sorted_input = sorted(input_lst)
list_length = len(input_lst)

for i in range(list_length):
    for j in range(i + 1, list_length):
        input_lst[i], input_lst[j] = input_lst[j], input_lst[i]
        if sorted_input == input_lst:
            return True
        else:
            input_lst[i], input_lst[j] = input_lst[j], input_lst[i]
return False

### Стало:

sorted_input = sorted(input_lst)
list_length = len(input_lst)

rearrange_success = False
for i in range(list_length):
    for j in range(i + 1, list_length):
        input_lst[i], input_lst[j] = input_lst[j], input_lst[i]
        if sorted_input == input_lst:
            rearrange_success = True
        else:
            input_lst[i], input_lst[j] = input_lst[j], input_lst[i]
return rearrange_success

# нехорошо, когда return больше чем 1 в функции. Я избавился от лишнего и
# воспользовался хорошей переменной с хорошим именем, но чуть более говорящим
# чекм просто success


########################################################
# 7.3
########################################################

### Так и было:

check_line = Line.replace(' ', '')
total_cost = 0

for symbol in check_line:
    if symbol in toner_per_char:
        total_cost += toner_per_char.get(symbol)
    else:
        total_cost += 23

--------------------------------------------------------

### Так и было:

global_found= False

for window_y in range(len(field) - len(to_find) + 1):

    if global_found:
        break

    for window_x in range(len(field[0]) - len(to_find[0]) + 1):
        found = True
        for find_y in range(len(to_find)):
            for find_x in range(len(to_find[0])):
                if field[window_y + find_y][window_x + find_x] != to_find[find_y][find_x]:
                    found = False

        if match_flag:
            global_found = True
            break

# Конечно вызывает сомнение вообще это решение с кучей вложенных циклов,
# вероятно, можно как то лучше закодить. Но тем не менее в данном случае, когда
# я решал задачу, мне в голову не пришло называть итераторы однобуквенными именами.

--------------------------------------------------------

### Так и было:

def transform(numbers_to_transform):

    back_keys = []
    coef = 0
    for outer_index in range(0, len(numbers_to_transform)):
        for inner_index in range(0, len(numbers_to_transform) - outer_index):
            coef = outer_index + inner_index
            major_number = 0
            for find_max in range(inner_index, coef + 1):
                if major_number <= numbers_to_transform[find_max]:
                    major_number = numbers_to_transform[find_max]
            back_keys.append(major_number)
    return back_keys


def TransformTransform(A, N):

    key = transform(transform(A))
    return sum(key) % 2 == 0

# Смотрю сейчас на этот код и с одной стороны понимаю, что вызывают некоторые
# сомнения имена переменных, но с другой стороны - это явно лучше чем i, j, k.
# в данный момент лучше придмать не могу


########################################################
# 7.4
########################################################

### Так и было:

def MadMax(N, Tele):

    Tele.sort()
    slice_idx = int((len(Tele) - 1) / 2)
    first_slice = Tele[:slice_idx]
    second_slice = Tele[slice_idx:]
    second_slice.reverse()
    result_arr = first_slice + second_slice

    return result_arr

# Возможно это не совсем подходязий случай, но так как в контексте кусков всего два,
# (рубим пополам), то они вполне себе антонимы

------------------------------------------------------------

### Было:
### Переменные:
larger
lesser

### Стало:
larger_number
lesse_number


# это имена антонимы, но они были не очень, потому что непонятно что большее
# а что меньшее, а так сразу очевидно что речь идет о числах

------------------------------------------------------------

### Так и было (минутка юмора):

def MaximumDiscount(N, price):

    goods = sorted(price, reverse=True)

    fool_discount = sum(goods[::-1][:N // 3])
    smart_discount = sum(goods[2::3])

    return max([fool_discount, smart_discount])

# а чем не антонимы??? ;D

------------------------------------------------------------

# К сожалению я не нашел других примеров, где можно было бы применить имена
# антонимы, но мне кажется что эту идею я понимаю и применяю, возможно не всегда
# когда стоило бы.

########################################################
# 7.5
########################################################

###  Было:

def SumOfThe(N, data):

    for i in range(N):
        temp_data = data.copy()
        scope = temp_data.pop(i)
        if sum(temp_data) == scope:
            return scope

### Стало:

def SumOfThe(N, data):

    for i in range(N):
        data_copy_to_process = data.copy()
        sum_candidate = data_copy_to_process.pop(i)
        if sum(data_copy_to_process) == sum_candidate:
            return sum_candidate

# в длинну уложились, обращаться небрежно с временной переменной теперь не хочется :D

------------------------------------------------------------

### Было:


def UFO(N, data, octal):

    converted = []

    if octal:
        for i in range(N):
            result = 0
            power = len(str(data[i])) - 1
            for j in str(data[i]):
                tmp = int(j) * (8 ** power)
                result += tmp
                power -= 1
            converted.append(result)
    else:
        for i in range(N):
            result = 0
            power = len(str(data[i])) - 1
            for j in str(data[i]):
                tmp = int(j) * (16 ** power)
                result += tmp
                power -= 1
            converted.append(result)

    return converted


### Стало:


def UFO(N, data, octal):

    converted_numbers = []

    if octal:
        for i in range(N):
            converting_number = 0
            current_power = len(str(data[i])) - 1
            for j in str(data[i]):
                converting_number += int(j) * (8 ** current_power)
                current_power -= 1
            converted.append(converting_number)
    else:
        for i in range(N):
            converting_number = 0
            current_power = len(str(data[i])) - 1
            for j in str(data[i]):
                converting_number += int(j) * (16 ** current_power)
                current_power -= 1
            converted.append(converting_number)

    return converted_numbers


# Я избавился от лишней переменной tmp, и изменил имена переменных на более
# подходящие (мне так кажется)

------------------------------------------------------------

### Было:


def MisterRobot(N, data):

    def swapper(lst):
        i = 0
        to_swap = lst
        while not lst[0] < lst[1] < lst[2]:
            to_swap.append(to_swap.pop(0))
            i += 1
            if i == 3:
                break
        return to_swap

    sorted_data = sorted(data)

    brute_force_success = True
    while brute_force_success:
        brute_force_success = False
        for i in range(len(data) - 2):
            piece = data[i:i+3]

            if not piece[0] < piece[1] < piece[2]:
                refer = data[i:i+3]
                data[i:i+3] = swapper(piece)
                if data[i:i+3] == refer:
                    brute_force_success = False
                else:
                    brute_force_success = True

    if data == sorted_data:
        return True
    else:
        return False


### Стало: 

def MisterRobot(N, data):

    def swapper(list_to_swap):
        swap_count = 0
        while not list_to_swap[0] < list_to_swap[1] < list_to_swap[2] and (
                swap_count != 3):
            list_to_swap.append(list_to_swap.pop(0))
            swap_count += 1
        return list_to_swap

    sorted_data = sorted(data)

    brute_force_success = True
    while brute_force_success:
        brute_force_success = False
        for i in range(len(data) - 2):
            piece_to_swap = data[i:i+3]

            if not piece_to_swap[0] < piece_to_swap[1] < piece_to_swap[2]:
                piece_snapshot = data[i:i+3]
                data[i:i+3] = swapper(piece_to_swap)
                if data[i:i+3] == piece_snapshot:
                    brute_force_success = False
                else:
                    brute_force_success = True

    if data == sorted_data:
        return True
    else:
        return False


# Избавился от избыточных переменных, попутно исправил код в целом. Убрал ненужный
# break. Я, кажется, начинаю что-то понимать

------------------------------------------------------------


