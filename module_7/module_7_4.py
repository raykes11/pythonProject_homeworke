team1 = 'Мастера кода'
team1_num = 5
score_1 = 40
team1_time = 1552.512
team2 = 'Волшебники данных'
team2_num = 6
score_2 = 42
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

print('В команде %(team1)s участников: %(team1_num)s!' % {'team1': team1, 'team1_num': team1_num})
print('Итого сегодня в командах участников: %(team1_num)s  и %(team2_num)s!' % {'team1_num': team1_num,
                                                                                'team2_num': team2_num})
print('Команды решили {score_1} и {score_2} задач.'.format(score_1=score_1, score_2=score_2))
print('{team2} решили задачи за {team2_time}с !'.format(team2=team2, team2_time=team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 1)} секунды на задачу!')
