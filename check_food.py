def check_food(animal,food):
    first = animal[0]
    last = animal[-1]
    if first == food[0] and last == food[-1]:
        print("Accepted")
    else:
        print("Not Accepted")
        
        
check_food("great blue heron","garlic naan")