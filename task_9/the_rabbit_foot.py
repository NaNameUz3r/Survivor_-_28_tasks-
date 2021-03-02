def TheRabbitFoot(s, encode):

    def encrypt(string_to_encrypt):
        string_to_encrypt = string_to_encrypt.replace(' ', '')

        s_length = len(string_to_encrypt)
        s_sqrt = round((s_length ** 0.5), 2)

        matrix_rows = int(s_sqrt // 1)
        matrix_cols = int(str(s_sqrt)[2:3])

        while matrix_rows * matrix_cols < s_length:
            matrix_rows += 1

        encrypt_list = []

        while len(string_to_encrypt) > matrix_cols:
            encrypt_list.append(list(string_to_encrypt[:matrix_cols]))
            string_to_encrypt = string_to_encrypt[matrix_cols:]
        else:
            encrypt_list.append(list(string_to_encrypt))

        result_list = []

        for i in range(matrix_cols):
            for j in range(matrix_rows):
                if i < len(encrypt_list[j]):
                    result_list.append(encrypt_list[j][i])
            result_list.append(' ')

        result_list = ''.join(result_list).strip()

        return result_list

    def decrypt(encoded_string):

        encoded_string = encoded_string.split()
        result = []
        max_row_len = len(max(encoded_string, key=len))
        index = 0
        
        while index < max_row_len:
            for j in range(len(encoded_string)):
                if len(encoded_string[j]) - 1 < index:
                    break
                else:
                    result.append(encoded_string[j][index])
            index += 1
        result = ''.join(result)
        print(result)
        return result

    if encode:
        encrypt(s)
    else:
        decrypt(s)

