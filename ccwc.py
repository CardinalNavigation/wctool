import sys
import os

def main():
    arguments=sys.argv[1:]
    text_path="test.txt"
    full_text=file_open(text_path)
    if arguments[0] == "-c":
        text_stats=os.stat(text_path)
        print(text_stats.st_size)
    elif arguments[0] == "-l":
        lines=0
        for text in full_text:
            if text=="\n":
                lines= lines + 1
        print(lines)

def file_open(text_path):
    with open(text_path) as f:
        file_contents = f.read()
        return file_contents

main()
