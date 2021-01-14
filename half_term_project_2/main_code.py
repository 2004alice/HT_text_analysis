book = str(input("book:"))


def boilerplate():
    ''':return: the book in a new file without the filler at the start and end'''
    with open("{}.txt".format(book), "r", encoding="UTF-8") as f:
        lines = f.readlines()
        index = 0  # a counter for the lines to be able to record when the file starts
        for line in lines:
            if "Chapter 1." in line:
                print(index)
                break
            elif "CHAPTER I" in line:
                print(index)
                break
            elif "CHAPTER I." in line:
                print(index)
                break
            elif "Chapter I." in line:
                print(index)
                break
            index += 1  # when the first chapter is found, the line is recorded
        index2 = 1  # second index to find the last line
        for line in lines:
            if "End of Project Gutenberg" in line:
                print(index2)
                break
            elif "***END OF THE PROJECT GUTENBERG EBOOK" in line:
                print(index2)
                break
            elif "End of the Project Gutenberg EBook" in line:
                print(index2)
                break
            index2 += 1
        f = open("clean_text.txt", "a", encoding="UTF-8")  # a new file is created
        for line_number in range(index, index2, 1):
            f.write(lines[
                        line_number])  # the indexed lines where the file starts and ends are written into the new text file


def chapter_cut():
    ''':return: the text cut into singular chapters as inputted by the user'''
    chapter = str(input("which chapter do you want to read? Please type 'Chapter' and then your number:"))
    with open("clean_text.txt", "r", encoding="UTF-8") as f:
        lines = f.readlines()
        index = 1
        start_index = 0
        index2 = 1
        begin = False
        for line in lines:
            if chapter in line:  # indexes the first line if it matches the name of that chapter inputted, as that is where it begins
                begin = True
                print(index)
                start_index = index
                continue
            elif "Chapter" in line and begin:  # continues reading the file to find the end of the chapter, but only if the first line is already indexed, as it will have the same key words in it
                print(index2)
                break
            elif "CHAPTER" in line and begin:
                print(index2)
                break
            elif "End of Project Gutenberg" in line and begin:
                print(index2)
                break
            elif "***END OF THE PROJECT GUTENBERG EBOOK" in line and begin:
                print(index2)
                break
            elif "End of the Project Gutenberg EBook" in line and begin:
                print(index2)
                break
            index += 1
            index2 += 1
    print(start_index, index2, index)
    with open("clean_chapter.txt", "a", encoding="UTF-8") as f:
        for line_number in range(start_index, index2,
                                 1):  # creates a new file for the clean chapter text and prints in it the lines indexed
            f.write(lines[line_number])


def chapter_word_count():
    ''':return: the amount of words in a chapter'''
    word_counter = 0
    with open("clean_chapter.txt", "r", encoding="UTF-8") as f:
        lines = f.readlines()
        for line in lines:
            if " " in line:  # reads the file and looks for spaces, as this will indicate how many words there are in the text
                word_counter += 1  # for each space, one is added to the counter which is returned at the end
        print("There are", word_counter, "words in this chapter.")


def chapter_sentence_count():
    ''':return: the amount of sentences in a chapter'''
    sentence_counter = 0
    with open("clean_chapter.txt", "r", encoding="UTF-8") as f:
        lines = f.readlines()
        for line in lines:
            if "." in line:  # reads the file and looks for full stops, as this will indicate how many sentences there are in the text
                sentence_counter += 1  # for each full stop, one is added to the counter which is returned at the end
        print("There are", sentence_counter, "sentences in this chapter.")


def chapter_ave_sent_len():
    ''':return: the average sentence length in a chapter'''
    word_counter = []
    with open("clean_chapter.txt", "r", encoding="UTF-8") as f:
        text = f.read()
        lines = text.split('.')  # splits the text into sentences by reading the full stops
        for sentence in lines:
            words = sentence.split(' ')  # splits the sentences into words by reading the spaces
            word_counter.append(len(words))
    average_wordcount = sum(word_counter) / len(
        word_counter)  # divides the sum of the words by the amount of words in a sentence
    print("There is an average of", average_wordcount, "words in each sentence of this chapter.")


def chapter_word_frequency():
    ''':return: the frequency of chosen words in a chapter'''
    word = str(input("which word do you want to know the frequency of?"))
    word_frequency = 0
    unique_words = []
    with open("clean_chapter.txt", "r", encoding="UTF-8") as f:
        lines = f.readlines()
        for line in lines:
            if word in line:
                word_frequency += 1
        if word_frequency >= 1:  # reads through the text and adds one to the counter when it reads the chosen word inputted by the user
            print("The word", "'", word, "'", "appears", word_frequency, "times in this chapter.")
        elif word_frequency == 0:
            print("word not in text")  # if the word is not in the text it tells the user
        elif word_frequency == 1:
            unique_words.append(word)
            print(unique_words)


def text_chapter_count():
    ''':return: the number of chapters in a book'''
    chapter_counter = 0
    with open("clean_text.txt", "r", encoding="UTF-8") as f:
        lines = f.readlines()
        for line in lines:
            if "Chapter" in line:
                chapter_counter += 1
            elif "CHAPTER" in line:
                chapter_counter += 1  # each time the word chapter is in the text, which indicates a new chapter, one is added to the counter which is then printed
        print("There are", chapter_counter, "chapters in this book.")


def text_sentence_count():
    ''':return: the amount of sentences in a book'''
    sentence_counter = 0
    with open("clean_text.txt", "r", encoding="UTF-8") as f:
        lines = f.readlines()
        for line in lines:
            if "." in line:  # reads the file and looks for full stops, as this will indicate how many sentences there are in the text
                sentence_counter += 1  # for each full stop, one is added to the counter which is returned at the end
        print("There are", sentence_counter, "sentences in this book")


def text_ave_sent_len():
    ''':return: the average length of sentences in the book'''
    word_counter = []
    with open("clean_text.txt", "r", encoding="UTF-8") as f:
        text = f.read()
        lines = text.split('.')  # splits the text into sentences by reading the full stops
        for sentence in lines:
            words = sentence.split(' ')  # splits the text into words by reading the spaces
            word_counter.append(len(words))
    average_wordcount = sum(word_counter) / len(
        word_counter)  # divides the sum of the words by the amount of words in a sentence
    print("There is an average of", average_wordcount, "words in each sentence of this book.")


def text_frequency():
    ''':return: the frequency of chosen words in a chapter'''
    word = str(input("which word do you want to know the frequency of?"))
    word_frequency = 0
    unique_words = []
    with open("clean_text.txt", "r", encoding="UTF-8") as f:
        lines = f.readlines()
        for line in lines:
            if word in line:
                word_frequency += 1
        if word_frequency >= 1:  # reads through the text and adds one to the counter when it reads the chosen word inputted by the user
            print("The word", "'", word, "'", "appears", word_frequency, "times in this book.")
        elif word_frequency == 0:
            print("word not in text")
        elif word_frequency == 1:
            unique_words.append(word)
            print(unique_words)


def author_frequency():
    ''':return: the frequency of words used by authors'''
    author = str(input("which author do you want to analyse?"))
    word = str(input("which word do you want to know the frequency of?"))
    unique_words = []
    word_frequency = 0
    if author == "Arthur Conan Doyle":
        with open("ACDthe_hound_of_baskerville.txt", "r", encoding="UTF-8") as f:
            lines = f.readlines()
            for line in lines:
                if word in line:
                    word_frequency += 1  # reads through the text and adds one to the counter when it reads the chosen word inputted by the user
        with open("ACDa_study_in_scarlet.txt", "r", encoding="UTF-8") as f:
            lines = f.readlines()
            for line in lines:
                if word in line:
                    word_frequency += 1
            if word_frequency >= 1:  # reads through the text and adds one to the counter when it reads the chosen word inputted by the user
                print("The word", "'", word, "'", "appears approximately", word_frequency, "times in this authors "
                                                                                           "books.")
            elif word_frequency == 0:
                print("word not in text")
            elif word_frequency == 1:
                unique_words.append(word)
                print(unique_words)
    elif author == "George Elliot":
        with open("GEthe_lifted_veil.txt", "r", encoding="UTF-8") as f:
            lines = f.readlines()
            for line in lines:
                if word in line:
                    word_frequency += 1
        with open("GEtom_and_maggie_tulliver.txt", "r", encoding="UTF-8") as f:
            lines = f.readlines()
            for line in lines:
                if word in line:
                    word_frequency += 1
            if word_frequency >= 1:
                print("The word", "'", word, "'", "appears approximately", word_frequency, "times in this authors "
                                                                                           "books.")
            elif word_frequency == 0:
                print("word not in text")
            elif word_frequency == 1:
                unique_words.append(word)
                print(unique_words)
    elif author == "H.G.Wells":
        with open("HGWthe_invisible_man.txt", "r", encoding="UTF-8") as f:
            lines = f.readlines()
            for line in lines:
                if word in line:
                    word_frequency += 1
        with open("HGWthis_misery_of_boots.txt", "r", encoding="UTF-8") as f:
            lines = f.readlines()
            for line in lines:
                if word in line:
                    word_frequency += 1
            if word_frequency >= 1:
                print("The word", "'", word, "'", "appears approximately", word_frequency, "times in this authors "
                                                                                           "books.")
            elif word_frequency == 0:
                print("word not in text")
            elif word_frequency == 1:
                unique_words.append(word)
                print(unique_words)
    elif author == "Mark Twain":
        with open("MTa_connecticut_yankee.txt", "r", encoding="UTF-8") as f:
            lines = f.readlines()
            for line in lines:
                if word in line:
                    word_frequency += 1
        with open("MTa_dogs_tale.txt", "r", encoding="UTF-8") as f:
            lines = f.readlines()
            for line in lines:
                if word in line:
                    word_frequency += 1
            if word_frequency >= 1:
                print("The word", "'", word, "'", "appears approximately", word_frequency, "times in this authors "
                                                                                           "books.")
            elif word_frequency == 0:
                print("word not in text")
            elif word_frequency == 1:
                unique_words.append(word)
                print(unique_words)


def top_50_words():
    ''':return: the 50 most common important words used in the text'''
    with open("clean_text.txt", "r", encoding="UTF-8") as f:
        text = f.read()
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;()[]') for word in words]  # strips the text of punctuation to be able to read the words singuarly
        words = [word.replace("'s", '') for word in words]  # strips the text of plural words
    important_words = []  # creates an empty list to record the common words
    for word in words:
        if len(word) > 3:
            if word != "could" or "from" or "have" or "that" or "their" or "they" or "were" or "when" or "which" or "while" or "with" or "would":  # removes words that aren't important and are too common to be included
                important_words.append(word)
    top_50 = important_words[0:49]  # places only the first 50 words in the empty list to print it
    print(top_50)


def common_10000():
    ''':return: how many words are not in the 10,000 most common in the English language'''
    with open("common_words.txt", "r", encoding="UTF-8") as f:  # opens and read the text file containing the 10000 most common words
        lines = f.read()
    with open("clean_text.txt", "r", encoding="UTF-8") as x:
        chapter_lines = x.readlines()
        uncommon_words = []
        for word in chapter_lines:
            if word in lines:
                uncommon_words.append(word)
    print(len(uncommon_words))



boilerplate()
chapter_cut()
text_chapter_count()
text_sentence_count()
text_ave_sent_len()
text_frequency()
chapter_word_count()
chapter_sentence_count()
chapter_ave_sent_len()
chapter_word_frequency()
author_frequency()
top_50_words()
common_10000()