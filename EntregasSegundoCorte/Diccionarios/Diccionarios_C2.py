sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "bathroom":14, 15:12}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}
translations = {"mountain":	"orod", "bread":	"bass", "friend":	"mellon", "horse":	"roch" }
subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}
students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"], "Geografìa": "Carol", "Nùmero1":14}

print(sensors)
print(num_cameras)
print(translations)
print(subtotal_to_total)
print(students_in_classes)



powers = {}
print(powers)

powers["Fuerza"]=1
print(powers)

animales={"vacas":3, "pollos":12, "caballos":32}
print(animales)

animales["unicornios"]=0
print(animales)

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)

user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print(oscar_winners)

oscar_winners.update({"Supporting Actress": "Viola Davis"})
oscar_winners["Best Picture"] = "Moonlight"
print(oscar_winners)

drinks = ["espresso", "chai", "chocolate", "tea", "decaf"]
caffeine = [70, 14, 0, 1, 53]
zipped_drinks = zip (drinks, caffeine)
print(zipped_drinks)

drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)

