import cmd

from modules.storage import DatafileStorage as Storage


greetings = """
Good day, \n
My dear friend!"""
statuses = ['to-do', 'in process', 'done']


class TaskManagerShell(cmd.Cmd):
    intro = greetings
    prompt = 'task-cli- '
    file = 'tasks.json'

    def do_load(self, args=None):
        Storage().load_tasks_from_file()

    def do_save(self, args=None):
        Storage().save_tasks_to_file()

    def do_add(self, args):
        description = args.replace('"', '')
        print(description)
        Storage().add_task(args)

    def do_exit(self, args):
        Storage().save_tasks_to_file()
        return True

    def do_show(self, args):
        all_tasks: dict = Storage().show_all_task()
        for task in all_tasks.values():
            print(task)

    def do_update(self, args):
        try:
            id = int(args[0])
            description = args.split('"')[1]
            Storage().update_task_by_id(id, description=description)
        except ValueError:
            print('write the right statement')


if __name__ == "__main__":
    TaskManagerShell().cmdloop()
