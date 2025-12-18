from itertools import permutations

weapons = [
    {"name": "Dagger", "cost": 8, "damage": 4, "armor": 0},
    {"name": "Shortsword", "cost": 10, "damage": 5, "armor": 0},
    {"name": "Warhammer", "cost": 25, "damage": 6, "armor": 0},
    {"name": "Longsword", "cost": 40, "damage": 7, "armor": 0},
    {"name": "Greataxe", "cost": 74, "damage": 8, "armor": 0},
]

armors = [
    {"name": "None", "cost": 0, "damage": 0, "armor": 0},
    {"name": "Leather", "cost": 13, "damage": 0, "armor": 1},
    {"name": "Chainmail", "cost": 31, "damage": 0, "armor": 2},
    {"name": "Splintmail", "cost": 53, "damage": 0, "armor": 3},
    {"name": "Bandedmail", "cost": 75, "damage": 0, "armor": 4},
    {"name": "Platemail", "cost": 102, "damage": 0, "armor": 5},
]

rings = [
    {"name": "Damage +1", "cost": 25, "damage": 1, "armor": 0},
    {"name": "Damage +2", "cost": 50, "damage": 2, "armor": 0},
    {"name": "Damage +3", "cost": 100, "damage": 3, "armor": 0},
    {"name": "Defense +1", "cost": 20, "damage": 0, "armor": 1},
    {"name": "Defense +2", "cost": 40, "damage": 0, "armor": 2},
    {"name": "Defense +3", "cost": 80, "damage": 0, "armor": 3},
]

w = weapons
a = armors
r = (
    list(permutations(rings, 0))
    + list(permutations(rings, 1))
    + list(permutations(rings, 2))
)


def fight(armour: int, dmg: int, hp=8, boss_hp=103, boss_armour=2, boss_dmg=9):
    while True:
        boss_hp -= dmg - boss_armour
        # print(boss_hp,hp)
        if boss_hp <= 0:
            return True
        hp -= boss_dmg - armour
        # print(boss_hp,hp)

        if hp <= 0:
            return False


lowest_cost = 1000000
highest_cost = 0
for weapon in w:
    for armour in a:
        for rings in r:
            total_cost = 0
            total_dmg = 0
            total_armour = 0
            if len(rings) == 0:
                total_cost += 0
            else:
                for ring in rings:
                    total_cost += ring.get("cost", 0)
                    total_dmg += ring.get("damage")
                    total_armour += ring.get("armor")

            total_cost += armour.get("cost")
            total_dmg += armour.get("damage")
            total_armour += armour.get("armor")

            total_cost += weapon.get("cost")
            total_dmg += weapon.get("damage")
            total_armour += weapon.get("armor")

            if fight(hp=100, dmg=total_dmg, armour=total_armour):
                if total_cost < lowest_cost:
                    lowest_cost = total_cost

            if not fight(hp=100, dmg=total_dmg, armour=total_armour):
                if total_cost > highest_cost:
                    highest_cost = total_cost

print(lowest_cost)
print(highest_cost)
