"""
gbasaad
6/11/2023
This file performs sentiment analysis on tweets using functions from sentiment_analysis module.
"""

from sentiment_analysis import *


# Prompts the user for input filenames, ensures proper file extensions, generates a sentiment analysis report,
# and writes the report to an output file in text format by using functions from the sentiment_analysis module.
def main():
    keyword_file_name = input("Input keyword filename (.tsv file): ")
    if not keyword_file_name.endswith('.tsv'):
        raise Exception("Must have tsv file extension!")
    keywords_dict = read_keywords(keyword_file_name)
    # To check if read_keywords returns an empty dict.
    if keywords_dict == {}:
        raise Exception("Tweet list or keyword dictionary is empty!")
    tweet_file_name = input("Input tweet filename (.csv file): ")
    if not tweet_file_name.endswith('.csv'):
        raise Exception("Must have csv file extension!")
    tweets_list = read_tweets(tweet_file_name)
    # To check if read_tweets returns an empty list.
    if tweets_list == []:
        raise Exception("Tweet list or keyword dictionary is empty!")
    output_file = input("Input filename to output report in (.txt file): ")
    if not output_file.endswith('.txt'):
        raise Exception("Must have txt file extension!")
    # Generate report and write it to the specified output file
    write_report(make_report(tweets_list, keywords_dict), output_file)


main()

