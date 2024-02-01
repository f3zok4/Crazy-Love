class Amor_da_minha_vida:
    def __init__(self, name, surname, age, pets, job, incollege, college_course, colour, fav_colour) -> object:
        self.name = name
        self.surname = surname 
        self.age = age
        self.pets = pets
        self.job = job
        self.incollege = incollege
        self.college_course = college_course
        self.colour = colour
        self.fav_colour = fav_colour

    def chata(self) -> str:
        print(Amor_da_minha_vida.name, " esta sendo chata! Você perde 10 de sanidade")

    def depressiva(self) -> str: 
        print(Amor_da_minha_vida.name, " esta sendo depressiva!", Amor_da_minha_vida.name, " perde 5 de sanidade")

