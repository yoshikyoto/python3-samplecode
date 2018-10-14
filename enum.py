from enum import Enum

class Word(Enum):
    all = 1
    part = 1

    @classmethod
    def value_from_name(cls, name):
        return cls[name]

    @classmethod
    def value_from_name_magic_method(cls, name):
        return cls.__members__.get(name)

print(Word.value_from_name('all'))
# ↓ここで例外になる
# print(Word.value_from_name('invalid'))

# こっちだと例外にならない
print(Word.value_from_name_magic_method('all'))
print(Word.value_from_name_magic_method('invalid'))
