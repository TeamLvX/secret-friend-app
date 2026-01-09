from src.shared import random_cycle_assigments


def test_matching_assigments():
    participants = ["PsharpX", "Jhogax", "Blaze", "Delta300", "666", "Karma", "Kirito"]

    result = random_cycle_assigments(participants)

    assert len(result) == 7
    name1 = result[0]

    result2 = random_cycle_assigments(participants)
    name2 = result2[0]

    assert name1 != name2
