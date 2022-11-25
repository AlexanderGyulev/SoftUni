country_names = input().split(", ")
country_capitals = input().split(", ")

country_dictionary = dict(zip(country_names, country_capitals))

for countries, capitals in country_dictionary.items():
    print(f"{countries} -> {capitals}")
