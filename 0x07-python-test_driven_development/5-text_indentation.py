def text_indentation(text):
    i = 0
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        o = len(text)
        while i < o:
            print(text[i], end="")
            if text[i] == '.' or text[i] == '?' or text[i] == ':':
                while text[i+1]== ' ':
                    i = i + 1
                print()
                print()
            i = i + 1
