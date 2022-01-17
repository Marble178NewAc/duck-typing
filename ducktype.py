class Marble178:
    def talk():
        print("Im talking")
    def scream():
        print("Im screaming")

class Marble178alt:
    def talk():
        print("Im talking")
    def scream():
        print("Im screaming")

class Person:
    def take(self, Marble):
        Marble178.talk()
        Marble178.scream()
        print("Congrats you take me")

marble = Marble178()
marble178 = Marble178alt()
you = Person()

you.take(marble)
