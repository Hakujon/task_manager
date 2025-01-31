import json

from .task_model import Task


class DatafileStorage:
    __file_path: str = 'tasks.json'
    __tasks: dict[int:Task] = {}

    def add_task(self, description: str):
        if description:
            obj = Task(description)
            self.__tasks[obj.id] = obj

    def get_task_by_id(self, id: int):
        return self.__tasks[id]

    def show_all_task(self):
        return self.__tasks

    @classmethod
    def load_tasks_from_file(cls):
        try:
            with open(cls.__file_path, 'r') as dump_file:
                tasks: dict = json.load(dump_file)
                if tasks:
                    for key, value in tasks.items():
                        cls.__tasks[int(key)] = Task.transform_from_dict(value)
                    for _ in range(int(sorted(tasks.keys())[-1])):
                        Task.make_next_id()
                else:
                    raise ModuleNotFoundError('you have no dumps')
        except FileNotFoundError('you have no dumps'):
            pass

    @classmethod
    def save_tasks_to_file(cls):
        dict_of_tasks = {
            key: value.transform_to_dict()
            for key, value in cls.__tasks.items()}
        with open(cls.__file_path, 'w+') as file:
            json.dump(dict_of_tasks, file)

    def update_task_by_id(self, id: int, new_descr: str):
        task: Task = self.get_task_by_id(id)
        task.update_task(description=new_descr)

    def close(self):
        self.reload()
