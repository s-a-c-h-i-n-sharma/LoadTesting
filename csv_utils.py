import os
import shutil

def ensure_n_csv_files(directory, n):
    files = os.listdir(directory)
    csv_files = [f for f in files if f.endswith('.csv')]
    num_csv_files = len(csv_files)
    if num_csv_files < n:
        files_to_create = n - num_csv_files
        for i in range(files_to_create):
            src_file = os.path.join(directory, csv_files[i % num_csv_files])
            new_file = os.path.join(directory, f"copy_{i + 1}_{csv_files[i % num_csv_files]}")
            shutil.copy(src_file, new_file)
            csv_files.append(new_file)
    csv_file_paths = [os.path.join(directory, f) for f in csv_files]
    return csv_file_paths
