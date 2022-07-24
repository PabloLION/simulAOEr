from simulaoer.objects.__main__ import Thing
from simulaoer.objects.task import Task, TrainProto, VillagerProto


class TownCenter(Thing):
    def __init__(self) -> None:
        self.abilities = [TrainProto(VillagerProto), "research loom"]
        self.hotkeys: dict[str, Task]

    def _check(self) -> None:
        for hk in self.hotkeys:
            if hk in self.abilities:
                continue
            else:
                raise Exception("Hotkey not in abilities")


tc = TownCenter()
tc.add_task(TrainProto(VillagerProto))
