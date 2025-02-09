from datetime import datetime


class Task:
    __num_id = 0

    @classmethod
    def make_next_id(cls):
        cls.__num_id += 1

    def __init__(self, *args):
        if len(args) == 1:
            self.make_next_id()
            self.id: int = self.__num_id
            self.description: str = args[0].replace('"', '')
            self.status: str = 'to-do'
            self.createdAt: str = str(datetime.now())
            self.updatedAt: str = str(datetime.now())
        elif len(args) == 5:
            self.id: int = args[0]
            self.status: str = args[1]
            self.description: str = args[2]
            self.createdAt: str = args[3]
            self.updatedAt: str = args[4]

    def update_task(self, *args, **kwargs):
        self.updatedAt = str(datetime.now())
        for key, value in kwargs.items():
            match (key, value):
                case('description', value):

                    self.description = value

                case('status', value):
                    self.status = value

                case('createdAt', value):
                    self.createdAt = value

                case('updatedAt', value):
                    self.updatedAt = value
                case ():
                    raise ValueError

    def transform_to_dict(self):
        return {
            'id': self.id,
            'status': self.status,
            'description': self.description,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt,
        }

    @classmethod
    def transform_from_dict(cls, data):
        return cls(
            data.get('id'),
            data.get('status'),
            data.get('description'),
            data.get('createdAt'),
            data.get('updatedAt'),
        )

    def __repr__(self):
        return f'{self.id} - {self.status} - {self.description}'
