for i in range(64):
    data = [0] * 64
    data[i] = 1
    with open('file{:02d}.esp', 'wb') as fh:
        fh.write(bytes(data))
