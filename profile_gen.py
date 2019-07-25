'''
    Profile Predictor 
'''
from random import randint
from random import choice
# profile class
class Profile:
    #class variables
    states = ['Abia', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno', 'Cross River', 'Delta', 'Ebonyi', 'Enugu', 'Edo', 'Ekiti', 'Gombe', 'Imo', 'Jigawa', 'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger', 'Ogun', 'Ondo', 'Osun', 'Oyo', 'Plateau', 'Rivers', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara']
    genders = ['Male', 'Female']
    regions = {'North': ['Benue', 'Kogi', 'Kwara', 'Nasarawa', 'Niger', 'Plateau', 'Federal Capital Territory'], 
                    'South': ['Akwa Ibom', 'Bayelsa', 'Cross River', 'Rivers', 'Delta', 'Edo'],
                    'East': ['Abia', 'Anambra', 'Ebonyi', 'Enugu', 'Imo'],
                    'West': ['Ekiti', 'Lagos', 'Ogun', 'Ondo', 'Osun', 'Oyo']}
    #initialize with input name/nickname
    def __init__(self, inputName):
        self.name = inputName
        self.state, self.tribe, self.gender = self.genprofile()

    # formats Profile object display
    def __str__(self):
        return f'Name/Nickname: {self.name}\nState of Origin: {self.state}\nTribe: {self.tribe}\nGender: {self.gender}'
    
    # function genprofile 
    # generates unique/random profile from give input parameters
    def genprofile(self) -> (str, str, str):
        ulength = len(self.name) # obtain length of name/nickname 
        rsIndex = len(self.states) # use ulength to obtain offset for states to randomly select
        stateIndex = randint(0, rsIndex) % rsIndex # randomly obtain state index for profile 
        tribeRegion = None
        # scan regions from obtained state 
        for region in self.regions.keys():
            if self.states[stateIndex] in self.regions.get(region):
                tribeRegion = region
        tribe = self.choosetribe(tribeRegion)
        gender = choice(self.genders)

        return (self.states[stateIndex], tribe, gender)

    # function choosetribe (params -> regions) -> tribe   
    # choose from selected group of tribes
    def choosetribe(self, region) -> str:
        
        if region == 'North':
            return 'Hausa'
        elif region == 'West':
            return 'Yoruba'
        elif region == 'South':
            return choice(['Benin', 'Edo'])
        else:
            return 'Igbo'

          

#Test run 
def main():
    myprofile = Profile(input('Enter your Name or NickName: '))
    print(myprofile)

if __name__ == '__main__':
    main()