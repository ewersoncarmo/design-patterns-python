from strategy.behavior.sound_behavior import SoundBehavior


class MeowSound(SoundBehavior):

    def make_sound(self, name: str) -> None:
        print(f'{name} is neowing')