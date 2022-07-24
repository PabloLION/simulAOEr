from simulaoer.objects.task import Task


class Player:
    ...


class Thing:
    """
    All units, buildings, neutral resources
    """

    def __init__(self, name, player, x, y, type):
        self.name = name
        self.player = player
        self.x = x
        self.y = y
        self.type = type
        self.tasks = []
        self.abilities = []
        self.bonuses = []

    def add_task(self, task: Task):
        if task not in self.abilities:
            raise Exception("Task not in abilities")  # mb not print
            return
        self.tasks.append(task)

    def run_task(self):
        next_task = self.tasks
