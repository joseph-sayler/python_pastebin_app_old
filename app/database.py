import peewee


class Database:
    """class to handle database selection based on user configuration"""

    def __init__(self, config=None):
        self._config = config
        if config is not None:
            self.init_db(config)

    def init_db(self, config):
        self._config = config
        if config.DATABASE_TYPE and config.DATABASE:
            if config.DATABASE_TYPE.lower() == "sqlite":
                self.database = peewee.SqliteDatabase(config.DATABASE)
            elif config.DATABASE_TYPE.lower() == "fauna":
                pass
            else:
                pass
        else:
            pass
