filename = "input.txt"


def find_first_marker(cipher: str, length: int) -> int:
    index = 0
    markerloc = length
    while markerloc < len(cipher):

        items = cipher[index:markerloc]
        test = set(items)
        if len(test) == length:
            break
        else:
            index = index + 1
            markerloc = markerloc + 1
    return markerloc


def main():
    with open(filename) as cipherfile:
        cipher = cipherfile.read()
        print(find_first_marker(cipher, 4))
        print(find_first_marker(cipher, 14))


if __name__ == "__main__":
    main()
