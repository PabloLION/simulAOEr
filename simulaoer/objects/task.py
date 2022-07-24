""" ALL TIME UNITS ARE IN SECONDS IF NOT SPECIFIED ELSEWHERE """


class Task:
    ...
    time: float


class UnitPrototype:
    training_time: float

    def __init__(self, training_time) -> None:
        self.training_time = training_time


VillagerProto = UnitPrototype(25)


class TrainProto(Task):
    ...
    unit: UnitPrototype
    count: int
    time: float

    def __init__(self, unit):
        self.unit = unit
