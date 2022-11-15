import csv
from random import shuffle

country_list = []  # hold countries and capitals
score_list = []  # saving score


def read_file(file_name):  # function to open country list
    with open(file_name + '.csv',
              'r') as csv_file:  # +,csv to enable you write the file name without adding the .csv extension
        reader = csv.reader(csv_file)  # reader object

        next(reader) #reads next line
        for line in reader:
            if file_name == 'countries':
                country_list.append([line[0], line[1]])  # update country list to contain two items
                shuffle(country_list)  # randomly run the list
            # else:
            # score_list.append([line[0],line[1]])


def write_file(name, score):  # function that writes to a file
    with open('scores.csv', 'a') as scores:
        writer = csv.writer(scores)
        writer.writerow([name, score])


"""def load_scores():
    score_list.clear()

    try:
        read_file('scores')
        score_list.sort(key=lambda score: score[1], reverse=True)
    except FileNotFoundError:
        write_file('name', 'score')"""


while True:
    read_file('countries')
    #load_scores()

    player_score = 0
    print("welcome")
    for i in range(5):
        guess = input(f"what is the capital of {country_list[i][0]}?\n>> ")
        if guess == 'quit':
            break
        if guess.title() == country_list[i][1]:
            player_score += 1
            print("Correct")
        else:
            print(f"The correct answer is {country_list[i][1]}")
        print("your score is: ", player_score)
    print("Game over\nScore: ", player_score)
    play_again = input("Type yes to play oncemore: ")
    if play_again.lower() != 'yes':
        break

print("See ya")




