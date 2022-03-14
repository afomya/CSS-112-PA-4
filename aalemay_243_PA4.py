
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

def within_weights(animals, weights, weightLimit):
    weight_range = []
    for i in range(len(animals)):
        if(weights[i] <= weightLimit):
            animals_list = animals[i]
            weight_range.append(animals_list)

    return weight_range


def any_adjacent_vertebrates(animals, vertebrates):
    isVertebrate = False
    for i in range(len(animals)-1):
        for j in range(len(vertebrates)):
            if(animals[i == vertebrates[j]]):
                isVertebrate = True
                break
        if (isVertebrate == True):
            isVertebrate = False
            for j in range(len(vertebrates)):
                if (animals[i + 1] == vertebrates[j]):
                    return True
    return False


def count_weights(weight_list):
    ways = 0
    for i in range(len(weight_list)-1):
        for j in range(i+1, len(weight_list)):
            sum = weight_list[i] + weight_list[j]
            for k in range(len(weight_list)):
                if(weight_list[k] == sum):
                    ways += 1
                    break
    return ways















