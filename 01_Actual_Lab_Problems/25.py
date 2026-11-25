"""Add two times using private attributes and operator overloading."""


class Time:
    def __init__(self, hour, minute, second):
        if hour < 0 or not 0 <= minute < 60 or not 0 <= second < 60:
            raise ValueError("Hours must be non-negative; minutes and seconds must be 0-59.")
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        if not isinstance(other, Time):
            return NotImplemented

        total_seconds = (
            self.__hour * 3600
            + self.__minute * 60
            + self.__second
            + other.__hour * 3600
            + other.__minute * 60
            + other.__second
        )
        hour, remainder = divmod(total_seconds, 3600)
        minute, second = divmod(remainder, 60)
        return Time(hour, minute, second)

    def __str__(self):
        return f"{self.__hour:02}:{self.__minute:02}:{self.__second:02}"


first_hours, first_minutes, first_seconds = map(
    int, input("Enter the first time (hours minutes seconds): ").split()
)
second_hours, second_minutes, second_seconds = map(
    int, input("Enter the second time (hours minutes seconds): ").split()
)

first_time = Time(first_hours, first_minutes, first_seconds)
second_time = Time(second_hours, second_minutes, second_seconds)

print("Sum of times:", first_time + second_time)
