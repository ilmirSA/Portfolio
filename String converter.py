convert = {'A': 'ALT N6 N5', 'B': 'ALT N6 N6', 'C': 'ALT N6 N7', 'D': 'ALT N6 N8', 'E': 'ALT N6 N9', 'F': 'ALT N7 N0',
           'G': 'ALT N7 N1', 'H': 'ALT N7 N2', 'I': 'ALT N7 N3', 'J': 'ALT N7 N4', 'K': 'ALT N7 N5', 'L': 'ALT N7 N6',
           'M': 'ALT N7 N7', 'N': 'ALT N7 N8', 'O': 'ALT N7 N9', 'P': 'ALT N8 N0', 'Q': 'ALT N8 N1', 'R': 'ALT N8 N2',
           'S': 'ALT N8 N3', 'T': 'ALT N8 N4', 'U': 'ALT N8 N5', 'V': 'ALT N8 N6', 'W': 'ALT N8 N7', 'X': 'ALT N8 N8',
           'Y': 'ALT N8 N9', 'Z': 'ALT N9 N0', 'a': 'ALT N9 N7', 'b': 'ALT N9 N8', 'c': 'ALT N9 N9',
           'd': 'ALT N1 N0 N0', 'e': 'ALT N1 N0 N1', 'f': 'ALT N1 N0 N2', 'g': 'ALT N1 N0 N3', 'h': 'ALT N1 N0 N4',
           'i': 'ALT N1 N0 N5', 'j': 'ALT N1 N0 N6', 'k': 'ALT N1 N0 N7', 'l': 'ALT N1 N0 N8', 'm': 'ALT N1 N0 N9',
           'n': 'ALT N1 N1 N0', 'o': 'ALT N1 N1 N1', 'p': 'ALT N1 N1 N2', 'q': 'ALT N1 N1 N3', 'r': 'ALT N1 N1 N4',
           's': 'ALT N1 N1 N5', 't': 'ALT N1 N1 N6', 'u': 'ALT N1 N1 N7', 'v': 'ALT N1 N1 N8', 'w': 'ALT N1 N1 N9',
           'x': 'ALT N1 N2 N0', 'y': 'ALT N1 N2 N1', 'z': 'ALT N1 N2 N2', ',': 'ALT N4 N4', '.': 'ALT N4 N6',
           '/': 'ALT N4 N7', '<': 'ALT N6 N0', '>': 'ALT N6 N2', '?': 'ALT N6 N3', ';': 'ALT N5 N9', ':': 'ALT N5 N8',
           '"': 'ALT N3 N4', '[': 'ALT N9 N1', ']': 'ALT N9 N3', '{': 'ALT N1 N2 N3', '}': 'ALT N1 N2 N5', }

stEng = input("Введите текст для конвертирования на английском: ")

for k in stEng:
    print(f"{convert.get(k, '*')} = {k}")










