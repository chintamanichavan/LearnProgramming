
problem_dict = dict()
with open("Leetcode_Problem_List.csv", "r") as problem_list:
    for problem in problem_list:
        if problem not in problem_dict:
            problem_dict[problem] = 1
        else:
            problem_dict[problem] += 1

for problem in problem_dict:
    if problem_dict[problem] > 1:
        print("The {} has a duplicate item in the list".format(problem))