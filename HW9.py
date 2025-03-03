from marvel import full_dict
from pprint import pprint

# 1 Задание
films_id: list[str] = input(" Введите ID фильмов через пробел: ").split()
filtered_films_id: list[int] = list(
    map(lambda x: int(x) if x.isdigit() else None, films_id)
)
print("Отфильтрованные ID фильмов:")
pprint(filtered_films_id)
print()

# 2 Задание
filtered_films: dict[any, any] = dict(
    filter(lambda x: x[0] in filtered_films_id, full_dict.items())
)
print()
print("Фильмы по ID:")
pprint(filtered_films)
print()

# 3 Задание
set_directors: set[str] = {film.get("director") for film in filtered_films.values()}
print()
print("Режиссёры:")
pprint(set_directors)
print()

# 4 Задание
full_dict_str_year: dict[any, any] = {
    key: {**value, "year": str(value["year"])} if "year" in value else value
    for key, value in full_dict.items()
}
print()
print("Фильмы с годом выпуска в виде строки:")
pprint(full_dict_str_year)
print()

# 5 Задание
filtered_dict_films: dict[any, any] = dict(
    filter(lambda x: str(x[1].get("title")).startswith("Ч"), full_dict.items())
)
print()
print('Фильмы с названием, начинающимся на "Ч":')
pprint(filtered_dict_films)
print()

# 6 Задание (сортируем по фазе)
sorted_by_stage: dict[any, any] = dict(sorted(full_dict.items(), key=lambda x: x[1].get("stage")))
print()
print("Фильмы, отсортированные по фазе:")
pprint(sorted_by_stage)
print()

# 7 Задание (сортиаруем по режиссёру и фазе)
sorted_by_director_title: dict[any, any] = dict(
    sorted(
        sorted(
            full_dict.items(), key=lambda x: (x[1].get("director"), x[1].get("stage"))
        )
    )
)
print()
print("Фильмы, отсортированные по режиссёру и фазе:")
pprint(sorted_by_director_title)
print()

# 8 Задание (фильтрация по 'Первой фазе' и сортировка по году)
sorted_filtered: dict[any, any] = dict(
    sorted(
        filter(lambda x: x[1].get("stage") == "Первая фаза", full_dict.items()),
        key=lambda x: x[1].get("year"),
    )
)
print()
print('Фильмы, отсортированные по году, отфильтрованные по фазе "Первая фаза":')
pprint(sorted_filtered)
