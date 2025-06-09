class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        # Kiểm tra key hợp lệ
        if not key or not isinstance(key, str):
            raise ValueError("Khóa phải là một chuỗi không rỗng")

        # Thay "J" bằng "I" và chuyển thành chữ in
        key = key.replace("J", "I").upper()
        key_set = set(key)
        key = ''.join(dict.fromkeys(key))  # Giữ thứ tự và loại bỏ trùng lặp

        # Định nghĩa bảng chữ cái (loại bỏ "J")
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining_letters = [letter for letter in alphabet if letter not in key_set]
        matrix = list(key)
        
        for letter in remaining_letters:
            matrix.append(letter)
            if len(matrix) == 25:  # Ma trận 5x5
                break

        playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        # Tìm tọa độ (hàng, cột) của ký tự trong ma trận
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        raise ValueError(f"Ký tự '{letter}' không được tìm thấy trong ma trận")

    def playfair_encrypt(self, plain_text, matrix):
        # Kiểm tra đầu vào
        if not plain_text or not isinstance(plain_text, str):
            raise ValueError("Văn bản gốc phải là một chuỗi không rỗng")
        
        # Thay "J" bằng "I" và chuyển thành chữ in
        plain_text = plain_text.replace("J", "I").upper()
        plain_text = ''.join(c for c in plain_text if c in "ABCDEFGHIKLMNOPQRSTUVWXYZ")
        
        encrypted_text = ""
        i = 0
        while i < len(plain_text):
            if i + 1 < len(plain_text):
                pair = plain_text[i:i+2]
            else:
                pair = plain_text[i] + "X"  # Thêm "X" nếu lẻ
            i += 2

            if len(pair) == 2 and pair[0] == pair[1]:
                pair = pair[0] + "X"
                i -= 1

            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        if not cipher_text or not isinstance(cipher_text, str):
            raise ValueError("Văn bản mã hóa phải là một chuỗi không rỗng")

        cipher_text = cipher_text.upper()
        cipher_text = ''.join(c for c in cipher_text if c in "ABCDEFGHIKLMNOPQRSTUVWXYZ")

        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return decrypted_text

    def banro(self, decrypted_text):
        if not decrypted_text or not isinstance(decrypted_text, str):
            raise ValueError("Văn bản giải mã phải là một chuỗi không rỗng")

        cleaned_text = ""
        i = 0
        while i < len(decrypted_text):
            if i + 1 < len(decrypted_text):
                pair = decrypted_text[i:i+2]
                i += 2
            else:
                pair = decrypted_text[i]
                i += 1

            if len(pair) == 2 and pair[1] == "X":
                cleaned_text += pair[0]
            else:
                cleaned_text += pair

            if i < len(decrypted_text):
                cleaned_text += " "

        return cleaned_text.strip()