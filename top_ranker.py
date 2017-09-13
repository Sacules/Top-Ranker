import ranker_functions

# Main program #
if __name__ == '__main__':
    score_acum = dict() # Initialize the dictionary

    print("Welcome to the Top Tanker!")
    print("This simple script takes a text file with one item per line, ranked in descending order, and saves it.")
    print("Adding more files will accumulate the items and save you a top with the highest ranked items of all lists combined.")
    print("Please enter what type of top you're doing (Game, Album, Movie, etc) in singular:\n")

    type_top = input()

    print("\nNow enter how many items your top will have (make sure your text files have the same amount!):\n")

    num_top = int(input())
    print()

    print("How many lists will you load?\n")

    num_lists = int(input())
    print()

    i = 0

    while i < num_lists: # Juicy part
        ls = ranker_functions.load_list(num_top) # Loads the text file

        ranker_functions.add_list(ls,score_acum) # Adds items to dictionary

        ranker_functions.save_top(score_acum,num_top,type_top) # Ranks them and saves the top to a text file

        i += 1

    print("\nFinished! The resulting top has been save into a text file.")
