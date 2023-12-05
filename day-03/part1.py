import json
import re

engine_schematic_file = open('input', 'r')
engine_schematic = engine_schematic_file.readlines()


symbols_list = [
    '!', '"', '#', '$', '%', '&', "'", '(',
    ')', '*', '+', ',', '-', '/', ':',
    ';', '<', '=', '>', '?', '@', '[', '\\',
    ']', '^', '_', '`', '{', '|', '}', '~'
]
    
# find symbols and sybmols index position.
# Append positon and symbol to a dict
def find_symbols():
    line_symbols = {}
    line_id = 0
    for line in engine_schematic:
        line = line.strip()
        symbol_positions = []
        for symbol in symbols_list:
            start_index = 0
            while start_index < len(line):
                text_number_index = line.find(symbol, start_index)
                if text_number_index != -1:
                    symbol_positions.append(int(text_number_index))
                    start_index = text_number_index + 1
                else:
                    break
        line_id += 1
        line_symbols[line_id] = sorted(symbol_positions)
    return line_symbols
        

# find numbers in line and numbers start and end index position. 
# Store current line number. Append start/end index position
# and the number to a dict.
def find_numbers():
    line_numbers = {}
    line_id = 0
    for line in engine_schematic:
        line = line.strip()
        line_id += 1
        matches = re.finditer(r'\d+', line)
        temp_numbers = []
        for match in matches:
            start_index = match.start()
            end_index = match.end()
            number = match.group()
            temp_numbers.append({"number": int(number), "start_index": start_index, "end_index": end_index})
        line_numbers[line_id] = temp_numbers
    return line_numbers

# find_numbers()
# check if there is a symbol before and after the number
# -1/+1 from the start/end index range
def check_adjacent_symbol():
    line_numbers = find_numbers()
    line_symbols = find_symbols()
    engine_numbers = []
    
    for line, numbers in line_numbers.items():
        for number in numbers:
            index_left_offset = number['start_index'] - 2
            index_right_offset = number['end_index'] +1
            horizontal_left_offset = number['start_index'] - 1
            horizontal_right_offset = number['end_index']
            for sline, symbol in line_symbols.items():
                if sline == line:
                    if horizontal_left_offset in symbol or horizontal_right_offset in symbol:
                        engine_numbers.append(number['number'])
                    previous_line_id = sline - 1
                    if previous_line_id > 0:
                        previous_line_symbols = line_symbols[previous_line_id]
                        for sym in previous_line_symbols:
                            if sym > index_left_offset and sym < index_right_offset:
                                engine_numbers.append(number['number'])
                                
                    next_line_id = sline + 1
                    if next_line_id <= len(line_numbers):
                        next_line_id_symbols = line_symbols[next_line_id]
                        for sym in next_line_id_symbols:
                            if sym > index_left_offset and sym < index_right_offset:
                                engine_numbers.append(number['number'])

    print(engine_numbers)
    print(sum(engine_numbers))


check_adjacent_symbol()
