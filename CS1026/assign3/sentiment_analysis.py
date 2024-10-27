"""
gbasaad
6/11/2023
This file processes tweet data, calculates sentiment scores based on a provided keyword dictionary,
generates statistics on tweet sentiments and countries, and produces a report, which is then written to an output file.
"""

# Reads keywords and their sentiment scores from a file, and returns a keyword dictionary.
def read_keywords(keyword_file_name):
    keyword_dict = {}
    try:
        keyword_file = open(keyword_file_name, "r")
        for line in keyword_file:
            # Split each line into keyword and sentiment score
            key, value = line.strip().split("\t")
            keyword_dict[key] = int(value)
    except IOError as exception:
        print("Could not open file", [keyword_file_name], "!")
    finally:
        return keyword_dict


# Takes a text and returns it clean by removing non-alphabetic characters and converting to lowercase.
def clean_tweet_text(tweet_text):
    clean_tweet_text = ""
    for char in tweet_text:
        if char.isalpha():
            # Keep only alphabetic characters and convert to lowercase
            clean_tweet_text += char.lower()
        elif char.isspace():
            # Preserve spaces in the text
            clean_tweet_text += char
    return clean_tweet_text


# Calculates the sentiment score of a tweet based on keywords and returns the score.
def calc_sentiment(tweet_text, keyword_dict):
    tweet_words = tweet_text.split()
    score = 0
    for word in tweet_words:
        if word in keyword_dict:
            # Accumulate sentiment score for each keyword in the tweet
            score += keyword_dict[word]
    return score


# Classifies the sentiment score as positive, negative, or neutral and returns a string.
def classify(score):
    if score > 0:
        return "positive"
    if score < 0:
        return "negative"
    if score == 0:
        return "neutral"


# Reads tweet data from a file, cleans the text, and organizes it into a list of dictionaries and returns the list.
def read_tweets(tweet_file_name):
    tweet_list = []
    try:
        with open(tweet_file_name, 'r') as text_file:
            for line in text_file:
                # Split each line into tweet attributes and create a dictionary
                lines = line.strip().split(",")
                line_dict = dict()
                # Assign each attribute to the corresponding key in the dictionary
                line_dict["date"] = str(lines[0])
                line_dict["text"] = clean_tweet_text(lines[1])
                line_dict["user"] = str(lines[2])
                line_dict["retweet"] = int(lines[3])
                line_dict["favorite"] = int(lines[4])
                line_dict["lang"] = str(lines[5])
                line_dict["country"] = str(lines[6])
                line_dict["state"] = str(lines[7])
                line_dict["city"] = str(lines[8])
                # Check for "NULL" values and convert latitude and longitude to float if not "NULL"
                if lines[9] == "NULL":
                    line_dict["lat"] = str(lines[9])
                else:
                    line_dict["lat"] = float(lines[9])
                if lines[10] == "NULL":
                    line_dict["lon"] = str(lines[10])
                else:
                    line_dict["lon"] = float(lines[10])
                # Sort the dictionary by keys
                sorted_list = sorted(line_dict.items())
                sorted_dict = dict(sorted_list)
                tweet_list.append(sorted_dict)

    except IOError as exception:
        print("Could not open file", [tweet_file_name])
    finally:
        return tweet_list


# Generates a report with various statistics on tweet sentiments and countries, and return the report.
def make_report(tweet_list, keyword_dict):
    num_favorite = 0
    num_negative = 0
    num_neutral = 0
    num_positive = 0
    num_retweet = 0
    num_tweets = 0
    total_favorite_sent = 0
    total_tweets_sent = 0
    total_retweet_sent = 0
    country_sentiments = dict()
    for tweet in tweet_list:
        if tweet["favorite"] != 0:
            num_favorite += 1
            total_favorite_sent += calc_sentiment(tweet["text"], keyword_dict)
        if tweet["retweet"] != 0:
            num_retweet += 1
            total_retweet_sent += calc_sentiment(tweet["text"], keyword_dict)
        num_tweets += 1
        total_tweets_sent += calc_sentiment(tweet["text"], keyword_dict)
        if classify(calc_sentiment(tweet["text"], keyword_dict)) == "positive":
            num_positive += 1
        elif classify(calc_sentiment(tweet["text"], keyword_dict)) == "negative":
            num_negative += 1
        else:
            num_neutral += 1
        country = tweet["country"]
        # To exclude the unknown countries from the top five list.
        if country != "NULL":
            sentiment = calc_sentiment(tweet["text"], keyword_dict)
            if country in country_sentiments:
                country_sentiments[country].append(sentiment)
            else:
                country_sentiments[country] = [sentiment]
    # Calculate average sentiments for each country
    average_sentiments = {country: sum(sentiments) / len(sentiments) for country, sentiments in country_sentiments.items()}
    # Sort countries by average sentiment in descending order
    sorted_countries = sorted(average_sentiments, key=average_sentiments.get, reverse=True)
    # Select the top five countries
    top_5_countries = sorted_countries[:5]
    top_five = ", ".join(top_5_countries)  # This var stores the top five countries as a single string
    # Calculate averages and handle division by zero cases
    if num_favorite == 0:
        avg_favorite = "NAN"
    else:
        avg_favorite = round(total_favorite_sent / num_favorite, 2)
    if num_retweet == 0:
        avg_retweet = "NAN"
    else:
        avg_retweet = round(total_retweet_sent / num_retweet, 2)
    if num_tweets == 0:
        avg_sentiment = "NAN"
    else:
        avg_sentiment = round(total_tweets_sent / num_tweets, 2)
    # Create a dictionary containing the report information
    report = dict()
    report['avg_sentiment'] = avg_sentiment
    report['num_tweets'] = num_tweets
    report['num_positive'] = num_positive
    report['num_negative'] = num_negative
    report['num_neutral'] = num_neutral
    report['num_favorite'] = num_favorite
    report['avg_favorite'] = avg_favorite
    report['num_retweet'] = num_retweet
    report['avg_retweet'] = avg_retweet
    report['top_five'] = top_five
    return report


# Writes the generated report(made by the previous function) to an output file.
def write_report(report, output_file):
    try:
        with open(output_file, "w") as file:
            for key, value in report.items():
                if key == "avg_sentiment":
                    file.write(f"Average sentiment of all tweets: {value}\n")
                elif key == "num_tweets":
                    file.write(f"Total number of tweets: {value}\n")
                elif key == "num_positive":
                    file.write(f"Number of positive tweets: {value}\n")
                elif key == "num_negative":
                    file.write(f"Number of negative tweets: {value}\n")
                elif key == "num_neutral":
                    file.write(f"Number of neutral tweets: {value}\n")
                elif key == "num_favorite":
                    file.write(f"Number of favorited tweets: {value}\n")
                elif key == "avg_favorite":
                    file.write(f"Average sentiment of favorited tweets: {value}\n")
                elif key == "num_retweet":
                    file.write(f"Number of retweeted tweets: {value}\n")
                elif key == "avg_retweet":
                    file.write(f"Average sentiment of retweeted tweets: {value}\n")
                elif key == "top_five":
                    file.write(f"Top five countries by average sentiment: {value}\n")
            print("Wrote report to {}".format(output_file))
    except IOError as exception:
        print("Could not open file", str(exception))
