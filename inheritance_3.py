# now we take more closer look in to inheritance

# class 1

class Sports():

    def cricket(self, player_name, matches_played, highest_score):

        player_name = player_name
        matches_played = matches_played
        highest_score = highest_score

        return player_name, matches_played, highest_score

        # we will return "Legend" if the player scored 200+ in one day matches.
        # also played more than 500 matches.
        # if that criteria met then he is a legend.
        # Anna i have poor signal I think we need to continue like this only :)
        # can you just try
    def analysis(self):
        name, matches, hig_score = self.cricket("rayadu", 298, 96) # this line is very important
        import pdb
        pdb.set_trace()
        if matches > 500 and hig_score > 200:
            print(f"Player {name} played {matches} with the highest score of {hig_score}.")
            print("He is a true legend")

        else:
            print("Something went wrong")


# ok
cric = Sports() # that's our class name
cric.analysis()             

# understood ? just one if and else only using and operator.

# create more functionalities with the above model. play with it.

# what is pdb anna and what is happening in the terminal ????

# haha :) pdb > python debugger. just search python pdb in google. very interesting topic
# you can understand any program easily
# basically it will show you whats happening in your code from top to bottom
# yes
# super  we can use this to create marksheets and it will be vry usefull :)
# yes very powerful package in python.

# create more functions and play with this pdb 
 

