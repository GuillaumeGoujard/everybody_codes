import os
import numpy as np

DAMAGES = np.array([0, 1, 3, 5])

def get_number_of_potions(string_of_letters):
    return (string_of_letters.count("B") + 3*string_of_letters.count("C"))

def evaluate_group(pair_of_letters):
    number_in_each_category = np.array([pair_of_letters.count("A"), pair_of_letters.count("B"), pair_of_letters.count("C"), pair_of_letters.count("D")])
    damages = sum(number_in_each_category*DAMAGES) + 2*(sum(number_in_each_category)==2) + 6*(sum(number_in_each_category)==3)
    return damages


def split_in_group(string_of_letters, n=2):
    return [string_of_letters[i:i+n] for i in range(0, len(string_of_letters), n)]


def get_number_of_potions_q2(string_of_letters):
    pairs_of_letters = split_in_pairs(string_of_letters)
    cumulated_potions = [evaluate_pair(p) for p in pairs_of_letters]
    return sum(cumulated_potions)

def get_number_of_potions_q3(string_of_letters):
    pairs_of_letters = split_in_group(string_of_letters, n=3)
    cumulated_potions = [evaluate_group(p) for p in pairs_of_letters]
    return sum(cumulated_potions)

if __name__ == "__main__":
    # file_path = "algorithmia_2024/quest1/everybody_codes_e2024_q01_p1.txt"
    # with open(file_path, 'r') as file:
    #     string_of_letters = file.read()
    # print("Input string:", string_of_letters)

    # answer = get_number_of_potions(string_of_letters)
    # print("Number of potions to use:", answer)

    #Q2
    # file_path = "algorithmia_2024/quest1/everybody_codes_e2024_q01_p2.txt"
    # with open(file_path, 'r') as file:
    #     string_of_letters = file.read()

    # # string_of_letters = "AxBCDDCAxD"
    # print("Input string:", string_of_letters)
    # print("By pair input string:", split_in_pairs(string_of_letters))
    # print("Potions by pair", [evaluate_pair(p) for p in split_in_pairs(string_of_letters)])
    

    # answer = get_number_of_potions_q2(string_of_letters)
    # print("Number of potions to use:", answer)

    #Q3

    string_of_letters = "xBxAAABCDxCC" 
    file_path = "algorithmia_2024/quest1/everybody_codes_e2024_q01_p3.txt"
    with open(file_path, 'r') as file:
        string_of_letters = file.read()

    print("By group input string:", split_in_group(string_of_letters, n=3))
    print("Potions by pair", [evaluate_group(p) for p in split_in_group(string_of_letters, n=3)])
    answer = get_number_of_potions_q3(string_of_letters)
    print("Number of potions to use:", answer)

