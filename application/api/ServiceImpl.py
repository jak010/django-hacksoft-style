from typing import Protocol

from application.common import DjangoModelType


class BaseService(Protocol):
    model: DjangoModelType

    def find_by(self, pk):
        ...

    def filter_by(self, pk):
        ...

    def delete_by(self, pk):
        ...
