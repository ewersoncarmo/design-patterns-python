from dataclasses import dataclass

from strategy.behavior.sound_behavior import SoundBehavior


@dataclass
class Pet:
    name: str
    _sound_behavior: SoundBehavior

    def eat(self) -> None:
        print(f'{self.name} is eating')

    def perform_sound(self) -> None:
        self._sound_behavior.make_sound(self.name)