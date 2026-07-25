def pattern_code_generator(texts):
    secret_codes = []

    for text in texts:
        secret_code = ""
        lines = text.split("\n")

        for line_index, line in enumerate(lines):
            words = line.split()


            if line_index < len(words):
                secret_code += str(len(words[line_index]))
            else:
                secret_code += "0"

        secret_codes.append(secret_code)

    return secret_codes


text1 = """i am ajit
i live in patna
i am a boy"""

text2 = """i am ajit
i live in patna"""

text3 = """i am ravi
i live in delhi
i am doctor"""

print(pattern_code_generator([text1, text2, text3]))