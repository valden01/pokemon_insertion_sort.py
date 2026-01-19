TYPE_RANK = {
    "normal": 1,
    "fire": 2,
    "water": 3,
    "electric": 4,
    "grass": 5,
    "ice": 6,
    "fighting": 7,
    "poison": 8,
    "ground": 9,
    "flying": 10,
    "psychic": 11,
    "bug": 12,
    "rock": 13,
    "ghost": 14,
    "dragon": 15,
    "dark": 16,
    "steel": 17,
    "fairy": 18
}


class Pokemon:
    def _init__(self, name, stage, generation, hp, type):
        self.name = name
        self.stage = stage
        self.generation = generation
        self.hp = hp
        self.type = type_.lower()


def compare(a, b, priorities):
    for p in priorities:
        if p == 1:  # Evolution
            if a.stage != b.stage:
                return a.stage - b.stage
        elif p == 2:  # Generation
            if a.generation != b.generation:
                return a.generation - b.generation
        elif p == 3:  # HP
            if a.hp != b.hp:
                return a.hp - b.hp
        elif p == 4:  # Type hierarchy
            if TYPE_RANK[a.type] != TYPE_RANK[b.type]:
                return TYPE_RANK[a.type] - TYPE_RANK[b.type]
        elif p == 5:  # Name
            if a.name != b.name:
                return -1 if a.name < b.name else 1
    return 0


# Insertion sort with swap & comparison counters
def insertion_sort(data, priorities):
    swaps = 0
    comparisons = 0
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0:
            comparisons += 1  # Count each compare call
            if compare(data[j], key, priorities) > 0:
                data[j + 1] = data[j]
                swaps += 1
                j -= 1
            else:
                break
        data[j + 1] = key
    return swaps, comparisons


def print_single(data, choice):
    print("\nPokemon       Value")
    print("-" * 28)
    for p in data:
        if choice == 1:
            value = p.stage
        elif choice == 2:
            value = p.generation
        elif choice == 3:
            value = p.hp
        elif choice == 4:
            value = p.type  # Print type name
        print(f"{p.name:12} {value}")


def print_mirror(original, sorted_data):
    print("\nORIGINAL (UNSORTED)        SORTED (ALPHABETICAL)")
    print("-" * 45)
    for o, s in zip(original, sorted_data):
        print(f"{o.name:22} {s.name}")


def print_final(data):
    print("\nFINAL SORTED ORDER")
    print(f"{'Pokemon':12} {'Stage':6} {'Gen':6} {'HP':6} {'Type':10}")
    print("-" * 46)
    for p in data:
        print(f"{p.name:12} {p.stage:<6} {p.generation:<6} {p.hp:<6} {p.type:10}")


def main():
    pokemon_data = [
        Pokemon("Greninja", 2, 6, 72, "water"),
        Pokemon("Bulbasaur", 0, 1, 45, "grass"),
        Pokemon("Lucario", 1, 4, 70, "fighting"),
        Pokemon("Pikachu", 0, 1, 35, "electric"),
        Pokemon("Gardevoir", 2, 3, 68, "psychic"),
        Pokemon("Charmander", 0, 1, 39, "fire"),
        Pokemon("Froakie", 0, 6, 41, "water"),
        Pokemon("Ivysaur", 1, 1, 60, "grass"),
        Pokemon("Zoroark", 1, 5, 60, "dark"),
        Pokemon("Charizard", 2, 1, 78, "fire"),
        Pokemon("Riolu", 0, 4, 40, "fighting"),
        Pokemon("Empoleon", 2, 4, 84, "water"),
        Pokemon("Frogadier", 1, 6, 54, "water"),
        Pokemon("Blaziken", 2, 3, 80, "fire"),
        Pokemon("Eevee", 0, 1, 55, "normal"),
        Pokemon("Sylveon", 1, 6, 95, "fairy"),
        Pokemon("Tyranitar", 2, 2, 100, "dark"),
        Pokemon("Abra", 0, 1, 25, "psychic"),
    ]

    while True:
        print("\nSORTING MENU")
        print("1 - Evolution")
        print("2 - Generation")
        print("3 - HP")
        print("4 - Type")
        print("5 - Alphabetical")
        print("6 - FINAL SORTED ORDER")
        print("7 - Exit")

        choice = int(input("\nEnter choice: "))

        if choice == 7:
            print("\nProgram ended.")
            break

        # Choices 1–4
        if choice in [1, 2, 3, 4]:
            data = pokemon_data.copy()
            swaps, comparisons = insertion_sort(data, [choice])
            print_single(data, choice)
            print(f"\nNumber of swaps: {swaps}")
            print(f"Number of comparisons: {comparisons}")

        # Choice 5
        elif choice == 5:
            original = pokemon_data.copy()
            sorted_data = pokemon_data.copy()
            swaps, comparisons = insertion_sort(sorted_data, [5])
            print_mirror(original, sorted_data)
            print(f"\nNumber of swaps: {swaps}")
            print(f"Number of comparisons: {comparisons}")

        # Choice 6
        elif choice == 6:
            data = pokemon_data.copy()
            swaps, comparisons = insertion_sort(data, [1, 2, 3, 4, 5])
            print_final(data)
            print(f"\nNumber of swaps: {swaps}")
            print(f"Number of comparisons: {comparisons}")

        else:
            print("Invalid choice.")


if _name_ == "_main_":
    main()

