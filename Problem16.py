# 16. Imagine you are creating a Super Mario game. You need to define  a class to represent Mario.
# What would it look like? If you aren't familiar with SuperMario, use your own favorite video or board game
# to model a player.


class Mario:

    def __init__(self, gender, height, shirt_color, pant_color, eye_color, hair_color, complexion, jumping_limit):
        self.gender = gender
        self.height = height
        self.shirt_color = shirt_color
        self.pant_color = pant_color
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.complexion = complexion
        self.jumping_limit = jumping_limit

        self.has_moustache = True
        self.has_cap = True


