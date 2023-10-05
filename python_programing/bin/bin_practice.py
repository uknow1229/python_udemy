import os

with open('sample_binary.dat', 'wb') as file:
    file.write(b'AB123XYZ AB456DEF')

# 各フィールドのバイトサイズ
field_lengths = [2, 3, 4]

def extract_from_binary(file_path, field_lengths):
    with open(file_path, 'rb') as file:
        while True:
            row = file.read(sum(field_lengths))
            if not row:
                break
            start = 0
            fields = []
            for length in field_lengths:
                fields.append(row[start:start+length].decode('utf-8').strip())
                start += length
            yield fields

def save_to_file(data, output_path):
    with open(output_path, 'w') as file:
        for row in data:
            file.write('|'.join(row) + '\n')

def clear_existing_records(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

if __name__ == "__main__":
    input_path = 'sample_binary.dat'
    output_path = 'output.txt'
    
    extracted_data = list(extract_from_binary(input_path, field_lengths))
    clear_existing_records(output_path)
    save_to_file(extracted_data, output_path)
