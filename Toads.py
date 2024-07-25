import random
import asyncio
from abc import abstractmethod




class Toad:
    base_damage = 15
    base_health = 150
    base_armor = 5
    
    def __init__(self):
        self.damage = self.base_damage
        self.health = self.base_health
        self.armor = self.base_armor
        self.apply_modifiers()
    
    @abstractmethod
    def apply_modifiers(self):
        pass
    
    def attack(self):
        return round(random.uniform(self.damage/2, self.damage), 1)
    
    def defense(self):
        return round(random.uniform(0, self.armor), 1)
    
class Assasin(Toad):
    def __init__(self):
        super().__init__()

    def apply_modifiers(self):
        self.health = self.health * 1.25
    
    
class Adventurer(Toad):
    def __init__(self):
        super().__init__()

    def apply_modifiers(self):
        self.damage = self.damage * 1.5
    
class Craftstman(Toad):
    def __init__(self):
        super().__init__()

    def apply_modifiers(self):
        self.armor = self.armor * 2
        
def get_random_toad():
    toad_classes = [Assasin, Adventurer, Craftstman]
    toad = random.choice(toad_classes)()
    return toad

async def fight(toad1:Toad, toad2:Toad):
    while toad1.health > 0 and toad2.health > 0:
        attack1 = toad2.attack() - toad1.defense()
        attack2 = toad1.attack() - toad2.defense()
        
        if attack1 > 0:
            toad1.health -= attack1
            
        if attack2 > 0:
            toad2.health -= attack2
            

    if toad1.health > 0:
        return 1
    
    if toad2.health > 0:
        return 2
    
    return 0
        
async def battle_launcher():
    toad_statistic = {
        1: 0, 
        2: 0, 
        0: 0
        }
    
    for _ in range(100):
        toad1 = get_random_toad()
        toad2 = get_random_toad()
        winner = await fight(toad1, toad2)
        toad_statistic[winner] += 1
        
    return toad_statistic
        
async def main():
    first_battle_results = await battle_launcher()
    second_battle_results = await battle_launcher()
    
    print(f"Цикл 1 - Жабка 1: {first_battle_results[1]}, Жабка 2: {first_battle_results[2]}, Ничья: {first_battle_results[0]}")
    print(f"Цикл 2 - Жабка 1: {second_battle_results[1]}, Жабка 2: {second_battle_results[2]}, Ничья: {second_battle_results[0]}")

if __name__ == "__main__":
    asyncio.run(main())