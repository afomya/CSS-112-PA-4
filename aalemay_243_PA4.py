#-------------------------------------------------------------------------------
# Name: Afomya Sisay Alemayehu
# Assignment 4
# Due Date: 03/14/2022
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: (W3Schools)
#-------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------

def biggest_vertebrate(animals, weights, vertebrates):
    # assign starter values as string and number
    biggest_weight = -1
    biggest_animal = ""
    #If we have no animals or vertebrates, we say zero
    if len(vertebrates) == 0 or len(animals) == 0:
        return None
    # for each variable and animal that exist in both lists,
    # i created and if statement to find the maximum weight
    for ani in range(len(animals)):
        for vert in range(len(vertebrates)):
            vertebrate = vertebrates[vert]
            animal = animals[ani]
            weight = weights[ani]
            if vertebrate == animal:
                if weight >= biggest_weight:
                    biggest_weight = weight
                    biggest_animal = animal
                break
    if biggest_weight == -1:
        return None
    else:
        return biggest_animal



    final_verdict = 0
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
            return final_verdict
        else:
            return None



def within_weight(animals, weights, weightLimit):
    # Assign weight range for animals within the range
    weight_range = []
# For each element in animals,
# if each corresponding weight is less than or equals to
# the weight limit, append to weight range
    for i in range(len(animals)):
        if(weights[i] <= weightLimit):
            animals_list = animals[i]
            weight_range.append(animals_list)

    return weight_range





def any_adjacent_vertebrates(animals, vertebrates):
    # We start off with a false premise
    vertebrate_maybe = False
    for i in range(len(animals)-1):
        for j in range(len(vertebrates)):
# If animal is vertebrate, then we set vertebrate_maybe as True
            statement1 = animals[i]
            statement2 = vertebrates[j]
            if statement1 == statement2:
                vertebrate_maybe = True
                break
        if (vertebrate_maybe == True):
            vertebrate_maybe = False
            for j in range(len(vertebrates)):
# If the animlas are nnext to eat other.
                if (animals[i + 1] == vertebrates[j]):
                    return True
    return False



def count_weights(weight_list):
    # hold answer
    answer = 0
# for all of the values in weight list
    for i in range(len(weight_list)):
        for j in range( i+ 1, len(weight_list)):
# add consecutive unique values
            sum = weight_list[i] + weight_list[j]
            for k in range(len(weight_list)):
                if(weight_list[k] == sum):
                    answer += 1
                    break
    return answer



























