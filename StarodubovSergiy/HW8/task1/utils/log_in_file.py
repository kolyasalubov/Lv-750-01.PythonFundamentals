def log_in_file(file_path, message):
    with open(file_path, 'a') as f:
        f.write(message + '\n')