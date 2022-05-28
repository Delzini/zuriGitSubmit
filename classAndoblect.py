from typing import List


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name='', age='', tracks='', score=''):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        print(self.name, self.age, self.tracks, self.score)
    def change_name(self, newName):
        self.name = newName
        print(newName, self.age, self.tracks, self.score)

    def change_age(self, newAge):
        self.age = newAge
        print(self.name, newAge, self.tracks, self.score)

    def add_track(self, newtrack):
        self.tracks = newtrack
        print(self.name, self.age, newtrack, self.score)
    def get_score(score):
        return score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

Bob.change_name("peter")
Bob.change_age("34")
Bob.add_track(["UI/UX"])
Bob.get_score()







