input_filename = 'input.txt'
forbidden_word = 'die'

with open(input_filename, 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

replacements = 0
for i, line in enumerate(lines):
    words = line.split()
    for j, word in enumerate(words):
        if word.lower() == forbidden_word.lower():
            lines[i] = line.replace(word, '*' * len(word))
            replacements += 1

output_filename = 'output.txt'
with open(output_filename, 'w', encoding='utf-8') as outfile:
    outfile.writelines(lines)

print(f"Статистика: {replacements} заміни слова '{forbidden_word}'.")
