def split(text, sep):
    text_list = []
    x = 0
    if sep in text:
        for i in range(0, len(text)):
            if sep == text[i]:
                text_list.append(text[x:i])
                x = i + 1
            else:
                continue
        text_list.append(text[x:len(text)])
    else:
        text_list = [text]
    return text_list


print(split('Аркаша валит боком хорошо, но гоча лучше', ' '))
