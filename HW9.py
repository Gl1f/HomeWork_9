from marvel import full_dict

films_id: list[str] = input(' Введите ID фильмов через пробел: ').split()
filtered_films_id: list[int] = list(map(lambda x: int(x) if x.isdigit() else None, films_id))
