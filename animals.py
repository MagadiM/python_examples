class Lion:
    def __init__(self, lower_classification, locale):
        self.lower_classification = lower_classification
        self.locale = locale
    

    def move(self):
        print("Prawling")

class Tortoise:
    def  __init__(self, lower_classification, locale):
        self.lower_classification = lower_classification
        self.locale = locale

    def move(self):
        print("Crawling")

class Snake:
    def __init__(self, lower_classification, locale):
        self.lower_classification = lower_classification
        self.locale = locale

    def move(self):
        print("Slithering")

Lion1 = Lion("Congo Lion", "Central Africa")
Tortoise1 = Tortoise("Russian tortoise", "Central Asia")
Snake1 = Snake("Reticulated python", "South Asia")
print(Lion1)
print(Tortoise1)
print(Snake1)