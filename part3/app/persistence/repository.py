from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass


class InMemoryRepository(Repository):
    def __init__(self):
        self._objects = {}

    def add(self, obj):
        self._objects[obj.id] = obj

    def get(self, obj_id):
        return self._objects.get(obj_id)

    def get_all(self):
        return list(self._objects.values())

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)

    def delete(self, obj_id):
        if obj_id in self._objects:
            del self._objects[obj_id]

    def get_by_attribute(self, attr_name, attr_value):
        for obj in self._objects.values():
            if getattr(obj, attr_name, None) == attr_value:
                return obj
        return None
