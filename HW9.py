from marvel import full_dict

# 1 Задание
films_id: list[str] = input(' Введите ID фильмов через пробел: ').split()
filtered_films_id: list[int] = list(map(lambda x: int(x) if x.isdigit() else None, films_id))
print(filtered_films_id)

# 2 Задание
filtered_films: dict[any, any] = dict(filter(lambda x: x[0] in filtered_films_id, full_dict.items()))
print(filtered_films)

# 3 Задание
set_directors: set[str] = {film.get('director') for film in filtered_films.values()}
print(set_directors)