import random
import time

names = list("Bach Corey Adam Steve Rick Thomas".split())
majors = list("Math Engineering CompSci Arts Business".split())

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
        }
        result.append(person)
    return result

people = people_list(5)
print(people)