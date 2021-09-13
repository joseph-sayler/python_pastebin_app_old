from faunadb import query as q
import faunadb.errors as faunadb_errors
from faunadb.objects import Ref
from faunadb.client import FaunaClient
from config import Fauna_config
from datetime import datetime
from flask import abort


class Fauna_DB:
    """class that acts like SQLAlchemy(), complete with a init_app method that does nothing

    used when constructing the initial application to mimmick SQLAlchemy so that a Class Factory 
    pattern can be utilized to determine which database to use based on config variables

    Session and Query sub(sub)classes are also set up to mimmick SQLAlchemy so that the calls in the
    routes can be identical regardless of which db driver is being used (sql or fauna)
    """
    session = None
    _client = None
    _collections = None
    _index = None

    def __init__(self, config=Fauna_config):
        self._client = FaunaClient(
            secret=config.FAUNA_SECRET_KEY,
            domain=config.FAUNA_DOMAIN,
            port=443,
            scheme="https"
        )
        self._collections = config.FAUNA_COLLECTION
        self._index = config.FAUNA_INDEX
        self.session = self.Session(
            client=self._client, collections=self._collections, index=self._index)

    def init_app(self, db):
        """this does nothing"""
        pass

    class Session:
        """Session class to mimmick SQLAlchemy"""

        def __init__(self, client, collections, index):
            self.__client = client
            self.__collections = collections
            self.__index = index

        def add(self, obj):
            self.__data = obj

        def commit(self):
            # convert to datetime string for storing in fauna
            self.__data.date = datetime.strftime(
                self.__data.date, "%Y-%m-%d %H:%M:%S.%f")
            # convert __data to dict for storing in fauna
            output = self.__data.__dict__
            self.__client.query(
                q.create(q.collection(self.__collections), {"data": output}))

        def query(self, cls):
            self.__class = cls
            return self

        def get(self, identifier):
            results = self.__client.query(
                q.get(q.match(q.index(self.__index), identifier)))
            # convert to datetime object for use in application
            results["data"]["date"] = datetime.strptime(
                results["data"]["date"], "%Y-%m-%d %H:%M:%S.%f")
            results_class = self.__class
            result_obj = results_class()
            result_obj._from_dict(results["data"])
            return result_obj

        def get_or_404(self, identifier):
            try:
                return self.get(identifier)
            except faunadb_errors.NotFound:
                return abort(404)
