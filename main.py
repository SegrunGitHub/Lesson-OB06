# Класс Hero:
# Атрибуты:
# Методы:
# attack(other): атакует другого героя (other), отнимая здоровье в размере своей силы удара
# is_alive(): возвращает True, если здоровье героя больше 0, иначе False
# Класс Game:
# Атрибуты:
# Игрок (player), экземпляр класса Hero
# Компьютер (computer), экземпляр класса Hero
# Методы:
# start(): начинает игру, чередует ходы игрока и компьютера,
# пока один из героев не умрет. Выводит информацию о каждом ходе
# (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f'{self.name} атакует {other.name} и отнимает {self.attack_power} здоровья')


    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        current_player = self.player
        while self.player.is_alive() and self.computer.is_alive():
            if current_player == self.player:
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)

            print(f'Осталось здоровья у {self.player.name}: {self.player.health}')
            print(f'Осталось здоровья у {self.computer.name}: {self.computer.health}\n')

            current_player = self.player if current_player == self.computer else self.computer

        if self.player.is_alive():
            print(f'{self.player.name} победил!')
        else:
            print(f'{self.computer.name} победил!')


# Пример использования
player = Hero('Игрок')
computer = Hero('Компьютер', attack_power=25)
game = Game(player, computer)
game.start()