# https://adventofcode.com/2023/day/4
from queue import Queue

scratchcards_file = open('input', 'r')
scratchcards = scratchcards_file.readlines()


def unique_scratchcards():
    q = Queue()
    unique_scratchcards = {}
    total_cards = 0

    for card in scratchcards:
        card_numbers = card.split("|")
        
        card_id = int(card_numbers[0].split(":")[0].split()[1])
        winning_numbers = card_numbers[0].split(':')[1].split()
        elf_numbers = card_numbers[1].split()
        
        matching_numbers = set(winning_numbers) & set(elf_numbers)
        unique_scratchcards[card_id] = len(matching_numbers)
        
        q.put(card_id)
        
    while not q.empty():
        total_cards += 1
        card = q.get()
        
        for i in range(card + 1, card + unique_scratchcards[card] + 1):
            q.put(i)
        
    print(total_cards)    
                        

unique_scratchcards()