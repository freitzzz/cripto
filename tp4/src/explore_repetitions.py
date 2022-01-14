import random


def explore_until_more_repetitions_than_unique(n):
    generated_count_dict = dict()
    repeated = 0
    non_repeated = 0
    dont_stop = True

    while dont_stop:
        gen = random.randint(0, n)

        if gen in generated_count_dict:
            repeated += 1
        else:
            non_repeated += 1
            generated_count_dict[gen] = -1

        generated_count_dict[gen] = generated_count_dict[gen] + 1

        dont_stop = non_repeated > repeated

    return non_repeated + repeated


n = 100


smallest_number_until_repetition = explore_until_more_repetitions_than_unique(
    n)

print(smallest_number_until_repetition)
