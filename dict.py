# question-1
# employee = {
#     "name":"Rahul",
#     "age": 28,
#     "department": "IT",
#     "salary": 45000
# }
# print(employee["name"])
# print(employee["department"])
# employee["salary"] = 50000
# employee["city"]="Bangalore"
# print(employee)

# question-2
# restaurant = {
#     "name": "Taj Café",
#     "location": "Mumbai",
#     "menu": ["Biryani", "Pasta", "Pizza", "Burger"],
#     "ratings": [4.5, 4.2, 4.8, 3.9]
# }

# print(restaurant["name"])
# print(restaurant["menu"][2])
# print(restaurant["ratings"][0])
# restaurant["menu"].append("sandwich")
# restaurant["ratings"].append(4.0)
# print(restaurant)

# question-3
# movie = {
#     "title":"Inception",
#     "director":"Christopher Nolan",
#     "actors":["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
#     "ratings":[8.8, 9.0, 8.5, 9.2],
#     "genre":["Sci-Fi", "Thriller"]
# }

# print(movie)
# print(movie["director"])
# print(movie["actors"][0])
# print(movie["ratings"][-1])
# movie["actors"].append("Tom Hardy")
# movie["ratings"].append(8.7)
# print(f" updated actors: {movie["actors"]}")
# print(f" updated ratings: {movie["ratings"]}")
# print(movie["genre"][0])

# question-4
# university = {
#     "name":"MIT",
#     "location":"USA",
#     "departments":{
#         "Computer Science":{
#             "head":"Dr, Smith",
#             "students": 500,
#             "courses":["Python", "AI", "Data Science"]
#         },
#         "Mathematics":{
#         "Head": "Dr, Johnson",
#         "students": 300,
#         "courses": ["Calculus", "Statistics"]
#         }
#     }
# }

# print(university)
# print(university["name"])
# print(university["departments"]["Computer Science"]["head"])
# print(university["departments"]["Mathematics"]["students"])
# print(university["departments"]["Computer Science"]["courses"][1])
# university["departments"]["Mathematics"]["head"]="Dr. Williams"
# print(university)
# university["departments"]["Computer Science"]["courses"].append("Machine Learning")
# print(university)
# print(f" updated department:{university["departments"]["Computer Science"]}")


# skip 5 as it has same concept as 4
# question-6

# library = {
#     "book1": "The Alchemist",
#     "book2": "1984",
#     "book3": "Harry Potter",
#     "book4": "The Hobbit"
# }

# print(library.keys())
# print(library.values())
# print(library.items())
# print(library.get("book3"))
# print(library.get("book5"))
# print(library.get("book5", "not found"))

# question-7
# inventory = {
#     "apples": 50,
#     "bananas": 30,
#     "oranges": 25,
#     "grapes": 15,
#     "mangoes": 20
# }

# print(inventory)
# mango_count=inventory.pop("oranges")
# print(mango_count)
# print(inventory)

# new_stock = {
#     "apples": 60, "watermelons": 10, "pineapples": 12
# }

# inventory.update(new_stock)
# print(inventory)








