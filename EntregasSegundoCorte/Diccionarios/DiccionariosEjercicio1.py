sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "bathroom": 29}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 3}

print(sensors)
print(num_cameras)

translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch", "beach":"relax" }
print(translations)

children = {"Von Trapp": ["Johan", "Rosmarie", "Eleonore", "Michael"] , "Corleone": ["Sonny", "Fredo", "Michael", "Sara"] }
print(children)

my_empty_dictionary = {}
print(my_empty_dictionary)

menu = {"oatmeal": 15, "avocado toast": 8, "orange juice": 5, "chocolate muffin": 9, "sandwich":5}
print("Before: ", menu)

menu["Birthday cake"] = 2
print("After", menu)

animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"elephant": 14}
animals_in_zoo = {"horses": 21}
print(animals_in_zoo)

sensors = {"living room": 11, "kitchen": 27, "bedroom": 10}
print("Before", sensors)

sensors.update({"pantry": 22, "guest room": 29, "patio": 32})
print("After", sensors)

user_ids = {"teraCoder": 901159293, "proProgrammer": 17919238}
print(user_ids)

user_ids.update({"theLooper": 13118475, "stringQueen": 8572239})
print(user_ids)

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)

menu["banana"] = 8
print("After", menu)

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print("Before", oscar_winners)

print()
oscar_winners.update({"Supporting Actress": "Viola Davis"})
print("After1", oscar_winners)

print()
oscar_winners["Best Picture"] = "Moonlight"
print("After2", oscar_winners)

###Dict Comprehensions
names = ['Jenny', 'Alex', 'Samuel', 'Gerardo']
heights = [68, 70, 67, 88]
zipStudents = zip(names, heights)
print("zipStudents: ", zipStudents)
students = {key:value for key, value in zip(names, heights)}
print(students)

drinks = ["espresso", "chai", "decaf", "drip", "chocolate"]
caffeine = [64, 40, 0, 120, 3]
zipped_drinks = zip(drinks, caffeine)
print(zipped_drinks)

drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [112, 29, 344, 821, 89, 15]
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)
plays.update({"Purple Haze": 1})
plays.update({"Respect": 94})
print("After: ", plays)
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)