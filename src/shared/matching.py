import random


def random_cycle_assigments(data: list[str]) -> list[tuple[str,str]]:
    if(len(data) < 2):
        return ValueError("At least two members are required")
    
    shuffled = data[:]
    random.shuffle(shuffled)

    assigments = {
        shuffled[i]: shuffled[(i+1) % len(shuffled)] for i in range(len(shuffled))
    }

    return list(assigments.items())
