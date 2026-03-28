from abc import ABC, abstractmethod


class SoundBehavior(ABC):

    @abstractmethod
    def make_sound(self, name: str) -> None:
      pass