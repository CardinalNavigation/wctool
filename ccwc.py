def main():
    book_path="test.txt"
    file_text=file_open(book_path)
    print(file_text)
    
def file_open(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

main()
