def save_file(text):
    try:
        f = open('file.txt', 'a')
        f.write(f'{text}\n')
        f.close()
    except Exception:
        print('Could not save file')


def read_file():
    try:
        f = open('file.txt', 'r')
        for line in f.readlines():
            print(line)
        f.close()
    except Exception:
        print('Could not read file')


save_file('some text')
save_file('some more text')
save_file('some more more text')

read_file()