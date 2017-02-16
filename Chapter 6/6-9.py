# 6-9 . Любимые места: создайте словарь с именем favorite_places . Придумайте 
# названия трех мест, которые станут ключами словаря, и сохраните для каждого 
# человека от одного до трех любимых мест . Чтобы задача стала более 
# интересной, опросите нескольких друзей и соберите реальные данные для своей 
# программы . Переберите данные в словаре, выведите имя каждого человека и 
# его любимые места . 



favorite_places = {
    "Kyrylo" : ["Kyiv", "Lviv", "Karpaty"],
    "Elena" : ["USA", "Washington", "Karpaty"]
    }
# for human_n, human_inf in people.items():
#     print("Username: " + human_n.title() + " " + human_inf["last_name"].title() 
#         + " is " + str(human_inf["age"]) + " years old. Live in " 
#         + human_inf["city"].title())
for name, places in favorite_places.items():
    print(name + " favorite places is:")
    for place in places:
        print("\t" + place)
