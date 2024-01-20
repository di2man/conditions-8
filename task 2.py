input_filename = 'input.txt'

with open(input_filename, 'r', encoding='utf-8') as infile:
    word_count = sum(len(line.split()) for line in infile)

print(f"Загальна кількість слів у файлі: {word_count}")
