class UrTube:

    def __init__(self):

        self.users = []

        self.videos = {}

        self.current_user = None

    def current(self, **kwargs):

        User.__init__(self, **kwargs)

        self.current_user = self.nickname

        return self

    def log_in(self, nickname, password):

        id_user = 0

        flag = False

        for user in self.users:

            if user['nickname'] == nickname and self.__hash__(id_user) == hash(password):

                flag = True

                break

            else:

                id_user += 1

        if flag:

            return UrTube.current(self, **self.users[id_user])

        else:

            print(f'Нет такого пользователя или не подходит пороль')

            exit()

    def register(self, nickname, password, age):

        persona = {'nickname': nickname, 'password': password, 'age': age}

        flag = False

        for user in self.users:

            if user['nickname'] == nickname:
                flag = True

                break

        if flag:

            return print(f'Пользователь с ником {nickname} уже существует')

        else:

            self.users.append(persona)

            id_user = len(self.users) - 1

            return UrTube.current(self, **self.users[id_user])

    def log_out(self):

        del self.nickname

        del self.password

        del self.age

        self.current_user = None

        return

    def __del__(self):

        return f'exit'

    def __hash__(self, id_user):

        return hash(self.users[id_user]['password'])

    def add(self, *Video):

        for info in Video:
            title = str(info.title)

            duration = info.duration

            time_now = info.time_now

            adult_mode = info.adult_mode

            self.videos[title] = duration, time_now, adult_mode

            print(f'{title} добавлено')

        return

    def get_videos(self, str):

        list_ = []

        for key in self.videos:

            if key.upper().lower().count(str.upper().lower()):
                list_.append(key)

        return list_

    def watch_video(self, str):

        if self.current_user == None:

            print("Войдите в аккаунт, чтобы смотреть видео")

        else:
            import time

            verification_age = self.age >= 18

            for key in self.videos:

                if key == str:

                    if self.videos[key][2] <= verification_age:

                        print(f'Просмотр {str}')

                        start = self.videos[key][1]

                        end = self.videos[key][0]

                        for time_ in range(start, end):
                            time.sleep(1)

                            print(time_ + 1)

                        print('Конец видео')

                    else:

                        print(f'Вам нет 18 лет, пожалуйста покиньте страницу')

        return


#

#

class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title

        self.duration = duration

        self.time_now = time_now

        self.adult_mode = adult_mode


class User:

    def __init__(self, **kwargs):
        self.nickname = kwargs['nickname']

        self.password = kwargs['password']

        self.age = kwargs['age']


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)

v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# ur.register('vasya_pupkin', 'lolkekcheburek', 13)

#

# ur.register('vasya_2upkin', 'lolkekcheburek', 15)

#

# ur.register('vasya_23pkin', 'lolkekcheburek', 40)


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

ur.log_in('vasya_pupkin', 'lolkekcheburek')

print(ur.current_user)

ur.log_in('vasya_pupkin', 'lolkecheburek')

print(ur.current_user)
#dg