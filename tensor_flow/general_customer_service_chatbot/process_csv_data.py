
# Get the twitter data file from https://www.kaggle.com/thoughtvector/customer-support-on-twitter


from pathlib import Path
import pandas as pd
import math

import pprint
pp = pprint.PrettyPrinter(indent=2)


DATA_PATH = (Path(__file__).parent / "twcs/twcs.csv").absolute()
        
def print_tweets_from_parent_tweet(pandas_dataset, tweet_id_responses: list, tweet_list:dict):

    #print("--- Response list: ", tweet_id_responses)

    data_list = list()
    
    for tweet_id in tweet_id_responses:
        source_row = pandas_dataset.loc[ pandas_dataset["tweet_id"] == int(tweet_id) ]

        #create a message list
        data_list.append({
            "tweet_id": source_row["tweet_id"].values[0], 
            "author_id": source_row["author_id"].values[0],
            "text": source_row["text"].values[0]
            })

        
        #print( 
        #    padding, " Tweet no:", source_row["tweet_id"].values,
        #    "User: ", source_row["author_id"].values, "Says: ", source_row["text"].values
        #) 

        # generate the list of response tweets if possible
        pandas_response_field = source_row["response_tweet_id"].values[0]
        #print("--- Item: ", pandas_response_field)

        if isinstance(pandas_response_field, str):

            # format to list and process each id
            response_list = pandas_response_field.split(",")
            print_tweets_from_parent_tweet(pandas_dataset, response_list, tweet_list)

        # if the field if not empty (we go to the thread that )
        elif not math.isnan(pandas_response_field):

            # got o the response tweet
            response_list = [pandas_response_field] # pandas always returns a list
            print_tweets_from_parent_tweet(pandas_dataset, response_list, tweet_list)

        # no response found... exit small while:
        else:

            # no response list stop the recurrency
            pass

    #due to recursion the list is created starting from the last item
    #data_list.reverse()
    tweet_list.insert(0, data_list)



if __name__ == "__main__":
    dataset_pandas = pd.read_csv(DATA_PATH)

    print("Dataset format: \n", dataset_pandas.head())
    print(">>>>>>> Specific field ", dataset_pandas["response_tweet_id"][0]) # get the row from the 
    print(">>>>>>> Complete row: ", dataset_pandas.loc[5]) # get the entire row
    print(">>>>>>> Filtered set: ", dataset_pandas.loc[ dataset_pandas["in_response_to_tweet_id"] == 119237] )
    print(">>>>>>> Filtered set: ", dataset_pandas.loc[ dataset_pandas["in_response_to_tweet_id"].isnull()] )
    print(">>>>>>> Dataframe size: ", dataset_pandas.shape )

    # Get the list of the tweets that started a conversation
    conversation_starters_dataset = dataset_pandas.loc[ dataset_pandas["in_response_to_tweet_id"].isnull()]

    # The first name and text
    conversation_pointer = 5
    next_tweet_id = conversation_starters_dataset["tweet_id"].values[conversation_pointer]
    
    
    # Go throug each thread (any tweet related to a first one)
    while True:    

        # use the recursive function to print all the thread:
        print("--------  Conversation number "+conversation_pointer +": --------- ")
        tweet_list = list()
        print_tweets_from_parent_tweet(dataset_pandas, [next_tweet_id], tweet_list)
        for response_list in tweet_list:
            print(">> parent tweet:")
            pp.pprint(response_list)

        # if keyboard pressed go for the next conversation
        input()
        conversation_pointer += 1
        next_tweet_id = int(conversation_starters_dataset["tweet_id"].values[conversation_pointer])

    
    # noise words:
    # filtter all the i am
    # -aa -ResolutionSup SR http* -fr ^jk -jb � 😩 ^hsb ^ACM ^JAY ^NHP ^kmg ^bcw
