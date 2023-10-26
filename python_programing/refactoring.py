def read_and_process_file(file_name):
    with open(file_name, "r") as f:
        data = f.read()
    process_data(data)
    return data

if file_name_pattern1.match(file_name):
    data = read_and_process_file(file_name)
    save_to_database(data)

elif file_name_pattern2.match(file_name):
    data = read_and_process_file(file_name)
    extra_process_for_pattern2(data)
    save_to_database(data)