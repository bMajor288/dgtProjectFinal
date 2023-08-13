import requests
import json

searched_date = "2023-06-08"
object_number = 0
p1 = 0
params = [
    "id",
    "neo_reference_id",
    "name",
    "nasa_jpl_url",
    "absolute_magnitude_h",
    "is_potentially_hazardous_asteroid",
    "is_sentry_object",
    "estimated_diameter"
    # estimated_diameter = [
    #     kilometers = [
    #         "estimated_diameter_min",
    #         "estimated_diameter_max"
    #     ],
    #     meters = [
    #         "estimated_diameter_min",
    #         "estimated_diameter_max"
    #     ],
    #     miles = [
    #         "estimated_diameter_min",
    #         "estimated_diameter_max"
    #     ],
    #     feet = [
    #         "estimated_diameter_min",
    #         "estimated_diameter_max"
    #     ]
    # ],
    # close_approach_data = [
    #     "close_approach_date",
    #     "close_approach_date_full",
    #     "epoch_date_close_approach",
    #     relative_velocity = [
    #         "kilometers_per_second",
    #         "kilometers_per_hour",
    #         "miles_per_hour"
    #         ],
    #     miss_distance = [
    #         "astronomical",
    #         "lunar",
    #         "kilometers",
    #         "miles"
    #         ],
    #     "orbiting_body"
    #         ]
    ]

# new_link = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key=DEMO_KEY"

response = requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date=2023-06-07&end_date=2023-06-08&api_key=DEMO_KEY")
print(response.status_code)

data = response.text

parse_json = json.loads(data)

active_asteroids = parse_json["element_count"]
neow = parse_json["near_earth_objects"][searched_date][object_number][params[7]]
"""                [Value is constant][YYYY-MM-DD string][Int, will be changed when arrows pressed][Requested parameter]
EXAMPLE            ["near_earth_objects"]["2023-06-08"][0]["id"] 
"""
print(active_asteroids)
print(neow)

def update_plus_data():
    with open("plus_data.txt", "w") as pd:
        neow = parse_json["near_earth_objects"][searched_date][object_number]
        neow = str(neow).replace(",", ", ")
        pd.write(str(neow))
    

# with open("plus_data.txt", "w") as pd:
#     itr = 0
#     for param in params:
#         neow = parse_json["near_earth_objects"][searched_date][object_number][params[itr]]
#         pd.write(str(neow) + ", ")
#         itr += 1
#         print(f"Looped:{itr} times")



# with open('data2.json', 'w') as json_file:
#     json_file.write(response.text)

# with open('data2.json', 'r') as json_file:
#     sample_load_file = json.load(json_file)

# test = sample_load_file["name"]

# test1 = test[1].values()
# test2 = list(test1)[0]
# test3 = test2[1:-1].split(",")
# print(test3[1])

# original_data = list(response)

# print(f"The original data:\n{original_data}")

# sorted_data = json.dumps(original_data, sort_keys=True)

# print(f"The sorted data based on the keys:\n{sorted_data}")

# with open('data.json','w') as file:
#     response = .dumps()
#     file.write(response.text)

# with open('data.json','r') as file:
#     pass
