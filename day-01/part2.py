# https://adventofcode.com/2023/day/1
calibration_document = open('input', 'r')
document_lines = calibration_document.readlines()

numbers = []
for line in document_lines:
	line = line.strip()
	text_numbers = {
		"one": "1",
		"two": "2",
		"three": "3",
		"four": "4",
		"five": "5",
		"six": "6",
		"seven": "7",
		"eight": "8",
		"nine": "9"
	}

	ordered_words = {}

	for key, val in text_numbers.items():
		start_index = 0
		while start_index < len(line):
			text_number_index = line.find(key, start_index)
			if text_number_index != -1:
				ordered_words[text_number_index] = key
				start_index = text_number_index + 1
			else:
				break

	sorted_words = sorted(ordered_words.items())
	if len(sorted_words) != 0:
		first_and_last = [sorted_words[0][1], sorted_words[-1][1]]
		for word in first_and_last:
			line = line.replace(word, text_numbers[word])

	line_digits = [letter for letter in line.strip() if letter.isdigit()]
	line_number = line_digits[0] + line_digits[-1]

	numbers.append(int(line_number))
print(sum(numbers))

