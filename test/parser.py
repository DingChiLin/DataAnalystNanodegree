# coding=utf-8
import codecs
source = codecs.open('./text.txt', 'rb', encoding='utf-8')

text = ''

for line in source:
    my_new_list = list(line);
    for idx, word in enumerate(my_new_list):
        if word == '（'.decode('utf-8') and \
            (my_new_list[idx+1] == '一'.decode('utf-8') or \
             my_new_list[idx+1] == '二'.decode('utf-8') or \
             my_new_list[idx+1] == '三'.decode('utf-8') or \
             my_new_list[idx+1] == '四'.decode('utf-8') or \
             my_new_list[idx+1] == '五'.decode('utf-8') or \
             my_new_list[idx+1] == '六'.decode('utf-8') or \
             my_new_list[idx+1] == '七'.decode('utf-8') ):
            text += '\n\n'
        elif word in ['1','2','3','4','5','6','7','8','9'] and my_new_list[idx+1] == '.':
            text += '\n\n'
            text += '  '

        text += word

target = codecs.open('./beautiful_text.txt', 'wb', encoding='utf-8')

target.write(text)
print(text)
