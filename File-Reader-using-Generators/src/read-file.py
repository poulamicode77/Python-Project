import sys

file_path = r"data\my-file.txt"
def read_file_line(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()

if __name__ == "__main__":
    count = 0
    for line in read_file_line(file_path):
        if "Python" in line:
            print(line.strip())
        count += 1
    print(f"Line count: {count}")