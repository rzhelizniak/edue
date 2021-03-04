import json
import os


# Task 1
def change_string_by_index(file_example, n, word):
    f = open(file_example, "r+")
    lines = f.readlines()
    f.close()
    lines[n] = word + "\n"
    new_f = open(file_example, "w")
    new_f.writelines(lines)
    new_f.close()


def delete_raw(index, file_example):
    f = open(file_example, "r")
    lines = f.readlines()
    f.close()
    del lines[index]
    new_f = open(file_example, "w+")
    for line in lines:
        new_f.write(line)
    print(new_f.readlines())
    new_f.close()


delete_raw(1, "/Users/romanzhelizniak/PycharmProjects/pythonProject/venv/files/test.txt")
change_file("/Users/romanzhelizniak/PycharmProjects/pythonProject/venv/files/test.txt",1,"NEW")


# Task 2
def reverse_file(index, file_example):
    f = open(file_example, "r")
    lines = f.readlines()
    f.close()
    lines.reverse()
    new_f = open(file_example, "w")
    new_f.writelines(lines)
    new_f.close()


# Task 3
def from_2_to_1(file_example_1, file_example_2,file_example_3):
    f_1 = open(file_example_1, "r+")
    lines1 = f_1.readlines()
    f_1.close()
    f_2 = open(file_example_2,"r+")
    lines2 = f_2.readlines()
    new_lines = lines2 +lines1
    f_3 = open(file_example_3, "w")
    f_3.writelines(new_lines)
    f_3.close()


general_path = "/Users/romanzhelizniak/PycharmProjects/pythonProject/venv/files/"
path_1 = general_path + "test.txt"
path_2 = general_path + "test2.txt"
path_3 = general_path + "test3.txt"

from_2_to_1(path_1, path_2, path_3)