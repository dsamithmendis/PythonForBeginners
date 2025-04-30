with open("file1.txt", "r") as file1:
    lines = file1.readlines()[:2]  # Read the first two lines

with open("file2.txt", "w") as file2:
    file2.writelines(lines)

with open("file2.txt", "r") as file2:
    content = file2.read()
    print(content)
