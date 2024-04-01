# Importing the ABC (Abstract Base Class) module from the abc package
from abc import ABC, abstractmethod
# from typing import Optional
# from sqlmodel import Field, Session, SQLModel, create_engine, select


# Defining an abstract class called AbstractRepository that inherits from ABC
class AbstractRepository(ABC):

    # Defining an abstract method called add that takes one argument, 'chocolate_box'
    @abstractmethod
    def adicionar(self, repository: object) -> None:
        # This method will be implemented by the concrete repositories
        pass #raise NotImplemented

    # Defining an abstract method called get that takes one argument, 'id'
    @abstractmethod
    def listar(self) -> list[object]:
        # This method will be implemented by the concrete repositories
        pass #raise NotImplemented

    @abstractmethod
    def buscar_por_id( self, id: int) -> object:
        pass #raise NotImplemented

    # Defining an abstract method called remove that takes one argument, 'chocolate_box'
    @abstractmethod
    def remover(self, id: int) -> bool:
        # This method will be implemented by the concrete repositories
        pass #raise NotImplemented
