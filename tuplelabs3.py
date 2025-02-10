def count_animals(animal_types, seen_animals):
    animal_count = {animal: 0 for animal in animal_types}
    
    for animal in seen_animals:
        if animal in animal_count:
            animal_count[animal] += 1
    
    print("Animal Count")
    for animal, count in animal_count.items():
        print(f"{animal} = {count}")

animal_types = ("Elephants", "Lions", "Gnu", "Zebras", "Buffalo")
short_animal_tuple = ("Elephants", "Lions", "Elephants", "Gnu", "Lions", "Gnu", "Gnu", "Elephants", "Gnu", "Gnu", "Gnu")

count_animals(animal_types, short_animal_tuple)