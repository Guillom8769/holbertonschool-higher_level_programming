#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    for i in sorted(dir(hidden_4)):
        if i[:2] != "__":
            print(i)
