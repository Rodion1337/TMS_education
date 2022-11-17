def split(text, sep):
    text_list = []
    x = 0
    if sep in text:
        for i in range(0, len(text)):
            if sep == text[i]:
                text_list.append(text[((x + 1) if text[x] == sep else x):(i)])
                x = i
            else:
                continue
        text_list.append(text[(x+1):len(text)])
    return text_list


print(split('Аркаша валит боком хорошо, но гоча лучше', ' '))
