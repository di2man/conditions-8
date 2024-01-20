
input_filename = 'input.txt'
output_filename = 'output.txt'

with open(input_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', encoding='utf-8') as outfile:
    for line in infile:
        words = line.split()
        filtered_words = [word if len(word) >= 7 else '*' * len(word) for word in words]
        outfile.write(' '.join(filtered_words) + '\n')

print("Файл успішно створено.")
