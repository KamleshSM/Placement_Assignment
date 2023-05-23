"""Question 3: -
Write a program, which would download the data from the provided link, and then read the data and convert 
that into properly structured data and return it in Excel format."""

import requests
import pandas as pd

# Download the data from the URL
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
response = requests.get(url)
data = response.json()

# Extract the required information from the data
pokemons = data["pokemon"]
pokemon_list = []

for pokemon in pokemons:
    pokemon_data = {
        "Name": pokemon["name"],
        "Image": pokemon["img"],
        "Type": ", ".join(pokemon["type"]),
        "Height": pokemon.get("height", ""),
        "Weight": pokemon.get("weight", ""),
        "Candy": pokemon.get("candy", ""),
        "candy_count": pokemon.get("candy_count", ""),
        "egg": pokemon.get("egg", ""),
        "spawn_chance": pokemon.get("spawn_chance", ""),
        "avg_spawns": pokemon.get("avg_spawns", ""),
        "spawn_time": pokemon.get("spawn_time", ""),
        "multipliers": pokemon.get("multipliers", ""),
        "weaknesses": ", ".join(pokemon.get("weaknesses", [])),
        "Next_evolution": ", ".join(evol["name"] for evol in pokemon.get("next_evolution", [])),
        "Prev_evolution": ", ".join(evol["name"] for evol in pokemon.get("prev_evolution", []))
    
    }
    pokemon_list.append(pokemon_data)

# Create a DataFrame from the extracted data
df = pd.DataFrame(pokemon_list)

# Save the DataFrame to an Excel file
output_file = "pokedex.xlsx"
df.to_excel(output_file, index=False)

print("Data has been converted and saved to", output_file)

