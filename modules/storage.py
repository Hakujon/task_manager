import json

from task_model import Task


class DatafileStorage:
    __file_path: str = 'tasks.json'
    __tasks: dict = {}

    def add_task(self, obj: Task):
        if obj:
            self.__tasks[obj.id] = obj

    def get_task_by_id(self, id: int):
        return self.__tasks[id]

    def show_all_task(self):
        return self.__tasks

    @classmethod
    def load_tasks_from_file(cls):
        try:
            with open(cls.__file_path, 'r') as dump_file:
                tasks = json.load(dump_file)
                for key, value in tasks.items():
                    cls.__tasks[int(key)] = Task.transform_from_dict(value)
        except FileNotFoundError('you have no dumps'):
            pass

    def save_tasks_to_file(self, fil):
        dict_of_tasks = {
            key: value.to_dict() for key, value in self.__tasks}
        with open(self.__file_path, 'w+') as file:
            json.dump(dict_of_tasks, file)

    def close(self):
        self.reload()
