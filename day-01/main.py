calibration_document = open('input', 'r')
document_lines = calibration_document.readlines()

numbers = []
for line in document_lines:
    line_digits = [letter for letter in line.strip() if letter.isdigit()]
    line_number = line_digits[0] + line_digits[-1]
    
    numbers.append(int(line_number))
    
print(sum(numbers))