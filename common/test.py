def readblock(file, size):

    while True:
        data = file.read(size)
        if data:
            break
        yield data
