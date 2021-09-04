def lengthoflastword(s):
    x = s.split()
    return len(x[-1])


def main():
    x = []
    x.append(lengthoflastword("Hello World"))
    x.append(lengthoflastword("   fly me   to   the moon  "))
    x.append(lengthoflastword("luffy is still joyboy"))
    print(x)


if __name__ == "__main__":
    main()
