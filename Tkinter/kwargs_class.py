# Author :- Biresashis Das

# NOTE :- **kwargs : Many Keyworded Argumnets.

class Sports():
    def __init__(self, **kwargs):
        self.sports = kwargs.get("sports_name")
        self.name = kwargs.get("cand_name")
        self.country = kwargs.get("country_name")

my_sports = Sports(sports_name="Javelin", cand_name="Neeraj Chopra")
print(my_sports.sports)
print(my_sports.country)    #This will print 'None'.




