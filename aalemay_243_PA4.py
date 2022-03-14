# Part 1
# are all the elements of animals in vertebrates?
# if not, remove them.
# find the max value
# correspond the value with the animal
# if animal is v

animals = ["butterfly", "fly", "whale", "parrot"]
weights = [.0005, .000007, 300000, 3.52]
vertebrates = ["hamster", "crocodile", "parrot", "whale"]
pure_vertebrate = 0


for animal in animals:
    for vertebrate in vertebrates:
        if animal == vertebrate:
            pure_vertebrate.append(animal)
            for pure in pure_vertebrate:
                print(pure_vertebrate)
                for i in range(10,000):
                    if animal[i] == pure:
                        final_verdict.append(weights[i])
print(final_verdict)
def biggest_vertebrate(animals, weights, vertebrates):
    final_verdict = 0
    max_weight = weights[0]
    for weight in weights:
        if weight > max_weight:
          max_weight = weight
          for animal in animals:
            index1 = weights.index(max_weight)
            index2 = animals.index(animal)
            if index1 == index2:
                final_verdict = animal
                for vertebrate in vertebrates:
                    if animal == vertebrate:
                        final_verdict = animal
                    else:
                        final_verdict = "None"
    return final_verdict





