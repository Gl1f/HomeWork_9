from marvel import full_dict
from pprint import pprint

# 1 Задание
films_id: list[str] = input(' Введите ID фильмов через пробел: ').split()
filtered_films_id: list[int] = list(map(lambda x: int(x) if x.isdigit() else None, films_id))
print('Отфильтрованные ID фильмов:')
pprint(filtered_films_id)

# 2 Задание
filtered_films: dict[any, any] = dict(filter(lambda x: x[0] in filtered_films_id, full_dict.items()))
print('Фильмы по ID:')
pprint(filtered_films)

# 3 Задание
set_directors: set[str] = {film.get('director') for film in filtered_films.values()}
print('Режиссёры:')
pprint(set_directors)

# 4 Задание
full_dict_str_year = {
    key: {**value, 'year': str(value['year'])} if 'year' in value else value
    for key, value in full_dict.items()}
print('Фильмы с годом выпуска в виде строки:')
pprint(full_dict_str_year)

# 5 Задание
filtered_dict_films = dict(filter(lambda x: str(x[1].get('title')).startswith('Ч'), full_dict.items()))
print('Фильмы с названием, начинающимся на "Ч":')
pprint(filtered_dict_films)

# 6 Задание
