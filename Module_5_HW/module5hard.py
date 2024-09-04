from time import sleep
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'user: {self.nickname}'

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for i in self.users:
            if i.nickname == nickname and i.password == hash(password):
                self.current_user = i

    def log_out(self):
        self.current_user = None

    def get_videos(self, word):
        list = []
        for i in self.videos:
            if word.lower() in i.title.lower():
                list.append(i.title)
        return list

    def register(self, nickname, password, age):
        flag = False
        user = User(nickname, password, age)
        for i in self.users:
            if user.nickname == i.nickname:
                flag = True
                break
        if flag:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(user)
            self.current_user = user
    def add(self, *videos):
        for i in videos:
            if i not in self.videos:
                self.videos.append(i)
            else:
                continue

    def watch_video(self, title_movie):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for i in self.videos:
                if i.title == title_movie:
                    if i.adult_mode and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        for k in range(i.time_now+1, i.duration+1):
                            print(k, end=' ')
                            sleep(0.5)
                        print('Конец видео')
                        break




ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
