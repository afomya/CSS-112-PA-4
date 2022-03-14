# if animal is v

animals = ["butterfly", "fly", "whale", "parrot"]
weights = [.0005, .000007, 300000, 3.52]
vertebrates = ["hamster", "crocodile", "parrot", "whale"]
pure_vertebrate = 0

def biggest_vertebrate(animals, weights, vertebrates):
    final_verdict = " "
    emp_variable = []
    c = 0
    max_animal = animals[c]
    # It's really annoying how I can't find max weight cause of the restrictions
    max_weight = weights[0]
    for weight in weights:
        if weight > max_weight:
          max_weight = weight

    # correspond the value with the animal
    for m in range(0, len(weights)):
        if weights[m] == max_weight:
            emp_variable.append(m)

    c = emp_variable[0]
    for vertebrate in vertebrates:
        max_animal = animals[c]
        if max_animal == vertebrate:
            final_verdict = max_animal
        else:
            final_verdict = "None"


    return final_verdict


print(biggest_vertebrate(["butterfly", "fly"], [0.0005, 0.000007], ["hamster","human", "mouse"]))









