import json

def tokenise(input_text):
    tokens = []
    word = ""
    in_word = False
    word_start = 0
    output_text = ""

    for i in range(len(input_text)):
        ascii_val = ord(input_text[i])

        if not in_word \
        and ((ascii_val >= 97 and ascii_val <= 122) \
        or (ascii_val >= 65 and ascii_val <= 90)):
            word = ""
            in_word = True
            word_start = i

        if ascii_val < 65 or ascii_val > 122 or \
        (ascii_val > 90 and ascii_val < 97):
            if in_word:
                word = input_text[word_start:i]
                in_word = False
                tokens.append(word)
            tokens.append(input_text[i])

    if in_word:
        word = input_text[word_start:]
        tokens.append(word)

    return tokens

def replace_tokens(token_list, replace_set):
    for i in range(len(token_list)):
        token = token_list[i]
        if token in replace_set.keys():
            token_list[i] = replace_set[token]

if __name__ == "__main__":
    input_text = input("Input text: ")
    replacement_file = input("JSON file with replacement pairs: ")
    with open(replacement_file, "r") as f:
        replacement = json.load(f)
        tokens = tokenise(input_text)
        replace_tokens(tokens, replacement)
        print("")
        print("Output below")
        print(''.join(tokens))
