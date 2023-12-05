# https://adventofcode.com/2023/day/3 
import re
import math

engine_schematic_file = open('input', 'r')
engine_schematic = engine_schematic_file.readlines()


gears_symbol = [
    '*',
]
    
def find_gears():
    line_gears = {}
    line_id = 0
    for line in engine_schematic:
        line = line.strip()
        gear_positions = []
        for gear in gears_symbol:
            start_index = 0
            while start_index < len(line):
                text_number_index = line.find(gear, start_index)
                if text_number_index != -1:
                    gear_positions.append(int(text_number_index))
                    start_index = text_number_index + 1
                else:
                    break
        line_id += 1
        line_gears[line_id] = sorted(gear_positions)
    return(line_gears)

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

def find_gear_numbers():
    line_numbers = find_numbers()
    line_gears = find_gears()
    gears_list = []
    for line, gears in line_gears.items():
        
        for gear in gears:            
            for nline, numbers in line_numbers.items():
                if nline == line:
                    temp_gears = {gear: []}
                    for number in numbers:
                        if number['start_index'] == gear + 1 or number['end_index'] == gear:
                            temp_gears[gear].append(number['number'])
                    
                    
                    previous_line_id = nline - 1
                    if previous_line_id > 0:
                        previous_line_numbers = line_numbers[previous_line_id]
                        for number in previous_line_numbers:
                            gear_min_range = gear - 1
                            gear_max_range = gear + 2
                            if number['start_index'] >= gear_min_range and not number['start_index'] >= gear_max_range:
                                temp_gears[gear].append(number['number'])
                            elif number['end_index'] >= gear_min_range + 1 and not number['end_index'] >= gear_max_range:
                                temp_gears[gear].append(number['number'])
                    next_line_id = nline + 1
                    if next_line_id <= len(line_numbers):
                        next_line_id_numbers = line_numbers[next_line_id]
                        for number in next_line_id_numbers:
                            gear_min_range = gear - 1
                            gear_max_range = gear + 2
                            if number['start_index'] >= gear_min_range and not number['start_index'] >= gear_max_range:
                                temp_gears[gear].append(number['number'])
                            elif number['end_index'] >= gear_min_range + 1 and not number['end_index'] >= gear_max_range:
                                temp_gears[gear].append(number['number'])
                                
                    gears_list.append(temp_gears)
    return gears_list

def calculate_gear_ratio():
    gears = find_gear_numbers()
    
    gear_ratios = []
    for gear_set in gears:
        for gear_id, gear_numbers in gear_set.items():
            if len(gear_numbers) != 2:
                continue
            else:
                gear_ratio = math.prod(gear_numbers)
                gear_ratios.append(gear_ratio)

    print(sum(gear_ratios))
    
calculate_gear_ratio()