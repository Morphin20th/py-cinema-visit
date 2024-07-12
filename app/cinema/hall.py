from __future__ import annotations
from ..people.cinema_staff import Cleaner
from ..people.customer import Customer


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list[Customer],
            cleaning_staff: Cleaner
    ) -> None:
        print(f"\"{movie_name}\" started in hall number {self.number}.")

        for name in customers:
            name.watch_movie(movie_name)

        print(f"\"{movie_name}\" ended.")

        cleaning_staff.clean_hall(self.number)