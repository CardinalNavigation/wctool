import sys
import functools
import os

def main():
    arguments=sys.argv[1:]
    text_path="test.txt"
    text_stats=os.stat(text_path)
    print(text_stats.st_size)
    # file_text=file_open(text_path)
    # count=byte_count(file_text)
    # print(count)

# def byte_count(file_text):
#     return functools.reduce(lambda accum, file_text: ord(accum) + ord(file_text), file_text)

# def file_open(text_pah):
#     with open(text_path) as f:
#         file_contents = f.read()
#         return file_contents

main()
