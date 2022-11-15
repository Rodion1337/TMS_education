def split(text, sep):
    text_list = []
    while sep in text:
        [text_list.append(text[0:(i - 1)]) for i in range(0, len(text)) if sep == text[i]]
#            text_list.append(text(0:(i - 1)))
#            text = text((i+1):len(text))
    return text_list


print(split('Аркаша валит боком хорошо, но гоча лучше', ','))