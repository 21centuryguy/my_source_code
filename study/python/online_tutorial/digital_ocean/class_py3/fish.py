"""
https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3
"""


#########################################
######################
######################      Parent Class       
######################
#########################################

class Fish:
    print("\n")
    print("====== parent class Fish =======")
    def __init__(self, first_name, last_name="Fish", skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
    
    def swim(self):
        print("The fish is swimming.")
    
    def swim_backwards(self):
        print("The fish can swim backwards.")


#########################################
######################
######################      Child Class       
######################
#########################################

class Trout(Fish):
    print("\n")
    print("====== child class 1 Trout =======")
    pass

terry = Trout("Terry") 
print(terry.first_name + " " + terry.last_name) 
print(terry.skeleton) 
print(terry.eyelids) 
terry.swim() 
terry.swim_backwards()


class Clownfish(Fish):
    print("\n")    
    print("====== child class 2 Clownfish =======")
    def live_with_anemone(self):
        print("The clownfish is coexisting with sea anemone.")

casey = Clownfish("Casey")
print(casey.first_name + " " + casey.last_name)
casey.swim()
casey.live_with_anemone()



#########################################################
######################
######################      Obverriding by Child Class       
######################
#########################################################

class Shark(Fish):
    print("\n")
    print("====== child class 3 Shark ( Obverride Parent Methods ) =======")
    def __init__(self, first_name, last_name="Shark", skeleton="cartilage", eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")

sammy = Shark("Sammy")
print(sammy.first_name + " " + sammy.last_name)
sammy.swim()
sammy.swim_backwards()
print(sammy.eyelids)
print(sammy.skeleton)



#########################################################
######################
######################      super() function        
######################
#########################################################

class Trout(Fish):
    print("\n")
    print("====== child class 1 Trout ( super() ) =======")    
    def __init__(self, water = "freshwater"):
        self.water = water
        super().__init__(self)


terry = Trout()

# Initialize first name
terry.first_name = "Berry"

# from parent class
print(terry.first_name + " " + terry.last_name) 
print(terry.skeleton) 
print(terry.eyelids) 
terry.swim() 
terry.swim_backwards()

# Use child __init__() override
print(terry.water)



#########################################################
######################
######################      Multiple Inheritance        
######################
#########################################################

class Trout_Shark(Trout, Shark):
    print("\n")
    print("====== child class 4 Trout_Shark ( Multiple Inheritance from Trout and Shark ) =======")

multiple_fish = Trout_Shark()
multiple_fish.swim()
multiple_fish.swim_backwards()

