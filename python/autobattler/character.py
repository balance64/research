from weapon import fists


class Character:
    # Class level variables
    race = "Human"

    def __init__(self, name: str, health: int) -> None:
        # Object level (instance) variables
        self.name = name
        self.health = health
        self.health_max = health

        self.weapon = fists

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        print(f"{self.name} dealt {self.weapon.damage} to {
              target.name} with {self.weapon.name}")


class Hero(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 ) -> None:
        super().__init__(name=name, health=health)


class Enemy(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 ) -> None:
        super().__init__(name=name, health=health)
