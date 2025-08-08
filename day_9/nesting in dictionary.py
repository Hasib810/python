capitals = {
    "France": "Paris",
    "Bangladesh": "Dhaka",
    "Pakistan": "Islamabaad",
    "U.A": "Dubai",
    "Germany": "Berlin"
}
#nested list in dictionary
# travel_log = {
#     "France": ["Paris", "Lille","Dijon"],
#     "Bangladesh": ["Dhaka","Chottogram","Khulna"],
# }

# print(travel_log["France"][1]) #print lille

# nested_list = ["a","b",["c","d"]]
# print(nested_list[2])
# print(nested_list[2][0])

travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited":["Paris", "Lille","Dijon"],
    },

    "Bangladesh": ["Dhaka","Chottogram","Khulna"],
}
print(travel_log["France"]["cities_visited"][1])