def split(text, sep):
    text_list = []
    x = 0
    if sep in text:
#       text_list = [text[0:(i)] for i in range(0, len(text)) if sep == text[i], x = i]  
# не прошло валидацию т.к. не понял, 
# как в генераторе присвоить значение i к x (см. строка 11)
        for i in range(0, len(text)):
            if sep == text[i]:
                text_list.append(text[((x + 1) if text[x] == ' ' else x):(i)])
                x = i
            else:
                continue
        text_list.append(text[(x+1):len(text)])
    return text_list


print(split('Аркаша валит боком хорошо, но гоча лучше', ' '))
