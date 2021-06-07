def TheRabbitsFoot(s, encode):

    def encrypt(string_to_encrypt):
        string_to_encrypt = string_to_encrypt.replace(' ', '')

        STRING_LENGTH = len(string_to_encrypt)
        STRING_SQUARE_ROOT = round((STRING_LENGTH ** 0.5), 2)

        matrix_rows = int(STRING_SQUARE_ROOT // 1)
        matrix_cols = int(str(STRING_SQUARE_ROOT)[2:3])

        while matrix_rows * matrix_cols < STRING_LENGTH:
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

        result = ''.join(result_list).strip()
        return result

    def decrypt(encoded_string):

        encoded_string = encoded_string.split()
        result_list = []
        max_row_len = len(max(encoded_string, key=len))
        index = 0

        while index < max_row_len:
            for j in range(len(encoded_string)):
                if len(encoded_string[j]) - 1 < index:
                    break
                else:
                    result_list.append(encoded_string[j][index])
            index += 1
        result = ''.join(result_list)
        return result

    if encode:
        return encrypt(s)
    else:
        return decrypt(s)

