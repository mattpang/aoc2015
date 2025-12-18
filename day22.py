from copy import deepcopy


class Spell:
    def __init__(self, mana, dmg, hp, armour, mana_gain, turns, spell_id):
        self.mana = mana
        self.dmg = dmg
        self.hp = hp
        self.armour = armour
        self.mana_gain = mana_gain
        self.turns = turns
        self.id = spell_id

    def tick(self):
        """Return a new spell with one fewer turn remaining."""
        return Spell(
            self.mana,
            self.dmg,
            self.hp,
            self.armour,
            self.mana_gain,
            self.turns - 1,
            self.id,
        )


class GameState:
    def __init__(self, boss_hp, my_hp, my_mana, active_spells, mana_used):
        self.boss_hp = boss_hp
        self.my_hp = my_hp
        self.my_mana = my_mana
        self.active_spells = active_spells
        self.mana_used = mana_used
        self.my_armour = 0


class Game:
    def __init__(self, part_two=True):
        self.part_two = part_two
        self.boss_dmg = 8
        self.least_mana_used = 1000000

        self.spells = [
            Spell(53, 4, 0, 0, 0, 0, 0),     # Magic Missile
            Spell(73, 2, 2, 0, 0, 0, 1),     # Drain
            Spell(113, 0, 0, 7, 0, 6, 2),    # Shield
            Spell(173, 3, 0, 0, 0, 6, 3),    # Poison
            Spell(229, 0, 0, 0, 101, 5, 4),  # Recharge
        ]

    def apply_spells(self, state):
        new_active = []
        state.my_armour = 0

        for spell in state.active_spells:
            if spell.turns >= 0:
                state.boss_hp -= spell.dmg
                state.my_hp += spell.hp
                state.my_armour += spell.armour
                state.my_mana += spell.mana_gain

            updated = spell.tick()
            if updated.turns > 0:
                new_active.append(updated)

        state.active_spells = new_active

    def sim(self, state, player_turn):
        if self.part_two and player_turn:
            state.my_hp -= 1
            if state.my_hp <= 0:
                return

        self.apply_spells(state)

        if state.boss_hp <= 0:
            self.least_mana_used = min(self.least_mana_used, state.mana_used)
            return

        if state.mana_used >= self.least_mana_used:
            return

        if player_turn:
            active_ids = {s.id for s in state.active_spells}

            for spell in self.spells:
                if spell.id in active_ids:
                    continue
                if spell.mana > state.my_mana:
                    continue

                next_state = deepcopy(state)
                next_state.my_mana -= spell.mana
                next_state.mana_used += spell.mana
                next_state.active_spells.append(spell)

                self.sim(next_state, False)
        else:
            damage = max(1, self.boss_dmg - state.my_armour)
            state.my_hp -= damage
            if state.my_hp > 0:
                self.sim(state, True)

    def run(self):
        start = GameState(
            boss_hp=55,
            my_hp=50,
            my_mana=500,
            active_spells=[],
            mana_used=0,
        )
        self.sim(start, True)
        print(self.least_mana_used)


if __name__ == "__main__":
    Game(part_two=False).run()
    Game(part_two=True).run()
