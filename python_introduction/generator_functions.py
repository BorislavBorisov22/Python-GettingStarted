def read_file():
    try:
        f = open('list.txt', 'r')
        for line in f.readlines():
            yield line
    except Exception:
        print('Could not read file')


for text in read_file():
    print(text)