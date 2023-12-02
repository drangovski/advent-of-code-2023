games_list = open('input', 'r')
document_lines = games_list.readlines()

# Maximum Cubes
RED = 12
GREEN = 13
BLUE = 14

games = []
for line in document_lines:
    game_id = line.split(": ")[0].strip().split(" ")[1]
    game_subsets = line.split(": ")[1].strip().split("; ")
    red_cubes = []
    green_cubes = []
    blue_cubes = []
    for subset in game_subsets:
        subset_colors = subset.split(", ")
        for color in subset_colors:
            if 'red' in color:
                red_cubes_count = color.split(" ")[0]
                red_cubes.append(int(red_cubes_count))
            if 'green' in color:
                green_cubes_count = color.split(" ")[0]
                green_cubes.append(int(green_cubes_count))
            if 'blue' in color:
                blue_cubes_count = color.split(" ")[0]
                blue_cubes.append(int(blue_cubes_count))

    if max(red_cubes) > RED or max(green_cubes) > GREEN or max(blue_cubes) > BLUE:
        continue
    else:
        games.append(int(game_id))
    
# Total sum of the game ids
print(sum(games))