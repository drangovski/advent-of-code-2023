# https://adventofcode.com/2023/day/4
scratchcards_file = open('input', 'r')
scratchcards = scratchcards_file.readlines()

points_number = {
    0: "0",
	1: "1",
	2: "2",
	3: "4",
	4: "8",
	5: "16",
	6: "32",
	7: "64",
	8: "128",
	9: "256",
	10: "512"
}

card_points = []

for card in scratchcards:
    card_numbers = card.split("|")
    
    card_id = card_numbers[0].split(":")[0].split()[1]
    winning_numbers = card_numbers[0].split(':')[1].split()
    elf_numbers = card_numbers[1].split()
    
    matching_numbers = set(winning_numbers) & set(elf_numbers)
    card_result = points_number[len(matching_numbers)]
    card_points.append(int(card_result))
    
    
print(sum(card_points))