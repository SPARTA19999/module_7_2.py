def custom_write(file_name, strings):
    #file = open(file_name, "a", encoding='utf-8')
    with open(file_name, 'a', encoding='utf-8') as f:
        strings_positions = {}
        for index, list in enumerate(strings, start=1):
            bt = f.tell()
            f.write(f"{list} \n")
            strings_positions[(index, bt)] = list
    #f.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)