'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, initial_count = 0):
    # Set up a count tracker
    count = initial_count

    # Get the index of 'th'
    index_of_th = word.find('th')

    # If not found, return 0
    if index_of_th == -1:
        return 0
    else:
        # Otherwise, increment the count by 1
        count += 1

        try:
            # Check if there is a next letter
            next_letter = word[index_of_th+2]
        except IndexError:
            # If there's no next letter, return the count
            return count

        # Get the count of 'th's in the rest of the word
        # And add it to the total count
        count += count_th(word[index_of_th+2:])

        return count

