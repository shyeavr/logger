import logging


class MyLogger(logging.Logger):
    root_logger = None
    root_handlers = None
    log_level = None

    def __init__(self):
        self.log = logging.getLogger('fsdfsfsf')

    @classmethod
    def update_root_config(cls, handlers=None, log_level=logging.DEBUG):
        cls.root_handlers = handlers

    @classmethod
    def show_root_config(cls):
        return cls.root_handlers

    def create_object_var(self, my_var):
        self.my_var = my_var

    def get_my_var(self):
        return self.my_var

ml1 = MyLogger()
ml2 = MyLogger()

ml1.update_root_config(handlers='test from ml1')
ml2.update_root_config(handlers='test from ml2')

s = ml1.show_root_config
print(ml1.root_handlers)

ml1.create_object_var('shay')
ml2.create_object_var('ronen')

print(ml1.get_my_var())
print(ml2.get_my_var())
ml1.debug()





