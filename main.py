# Класс Стример
class Streamer:
    def __init__(self, nick, followers):
        self.nick = nick
        self.donates = []
        self.followers = followers

    def add_donate(self, amount):
        self.donates.append(amount)

    def total_donates(self):
        return sum(self.donates)

    def average_donate(self):
        if len(self.donates) == 0:
            return 0
        return sum(self.donates) / len(self.donates)

# Функция вне класса
def print_stats(streamer):
    print("=== СУПЕР Статистика стримера ===")
    print("Ник:", streamer.nick)
    print("Подписчики:", streamer.followers)
    print("Всего донатов:", streamer.total_donates())
    print("Средний донат:", streamer.average_donate())

# Главная часть
streamer = Streamer("GolubKin", 1200)
streamer.add_donate(500)
streamer.add_donate(150)
print_stats(streamer)
