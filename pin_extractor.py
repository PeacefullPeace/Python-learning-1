def pin_extractor(poems):
    secret_codes = []

    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')

        for i, line in enumerate(lines):
            words = line.split()

            if i < len(words):
                secret_code += str(len(words[i]))
            else:
                secret_code += '0'

        secret_codes.append(secret_code)

    return secret_codes


poem1 = input('What is the poem?')
poem2 = input('What is the poem?')
poem3 = input('What is the poem?')

print(pin_extractor([poem1, poem2, poem3]))