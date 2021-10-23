from abc import ABC, abstractmethod


class BaseController(ABC):
    def __init__(self, storage):
        self._storage = storage

    @abstractmethod
    def processRequest(self, request):
        pass