x = 0
y = 0

with open('levels/hello.xsb') as f:
    for line in f:
        for zeichen in line:
            if zeichen != "\n":
                print(zeichen, x, y)
                x += 1
        y += 1
        x = 0