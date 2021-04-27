"""
File: class_reviews.py
Name: Allen Lee
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your program should be case-insensitive.
If the user input -1 for class name, your program would output
the maximum, minimum, and average among all the inputs.
"""


def main():
    """
    TODO:
    """
    max_001 = 0
    min_001 = 10
    max_101 = 0
    min_101 = 10
    num_score_001 = 0
    num_score_101 = 0
    total_001 = 0
    total_101 = 0
    while True:
        class_name = input('Which class? ')
        class_name = class_name.upper()
        if class_name == '-1':
            break
        score = int(input('Score: '))
        if class_name == 'SC001':
            num_score_001 += 1
            total_001 += score
            if score < min_001:
                min_001 = score
            if score > max_001:
                max_001 = score
            avg_001 = total_001 / num_score_001
        elif class_name == 'SC101':
            num_score_101 += 1
            total_101 += score
            if score < min_101:
                min_101 = score
            if score > max_101:
                max_101 = score
            avg_101 = total_101 / num_score_101
    if num_score_001 == 0 and num_score_101 == 0:
        print('No class scores were entered')
    else:
        print('=============SC001=============')
        if num_score_001 == 0:
            print('No score for SC001')
        else:
            print('Max (001): '+str(max_001))
            print('Min (001): '+str(min_001))
            print('Avg (001): '+str(avg_001))
        print('=============SC101=============')
        if num_score_101 == 0:
            print('No score for SC101')
        else:
            print('Max (101): '+str(max_101))
            print('Min (101): ' + str(min_101))
            print('Avg (101): '+str(avg_101))


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
