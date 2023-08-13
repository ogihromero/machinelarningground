################### Scope ####################


# Global scope
player_health = 10


# Local Scope
def drink_potion():
    potion_strength = 2  # Local Scope
    print(potion_strength)
    print(player_health)


# drink_potion()
# print(potion_strength) # will give a error, the variable potion_strength is local
# print(player_health)


# There is no Block Scope
enemies = 1


game_level = 3


def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


# Modifying Global Scope

enemies = 1


# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")

# Instead of using 'global', it's better to return the value with the modification
def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants

PI = 3.14159
URL = "https://www.google.com"
GITHUB = "ogih_romero"
