import re

def camel_to_snake(camel):
    return re.sub(r"([A-Z])", r"_\1", camel).lower().lstrip("_")

print(camel_to_snake("HelloWorldExample"))  # hello_world_example
([A-Z]) – ищет заглавные буквы.
r"_\1" – вставляет перед ними _.
.lower() – делает всё строчными.
.lstrip("_") – убирает _ в начале, если оно появилось.
3. Общие вопросы на защиту
1. Чем match() отличается от search()?

match() проверяет только начало строки.
search() ищет совпадение в любом месте строки.
2. Чем findall() отличается от search()?

search() возвращает только первое совпадение.
findall() возвращает все совпадения списком.

pattern = r"(?=[A-Z])"
re.split(pattern, text)
pattern = r"(?=[A-Z])"
re.split(pattern, text)
(?=[A-Z]) – разделяет перед заглавной буквой.

Пример работы:
Вход: "HelloWorldExample"
Выход: ['Hello', 'World', 'Example']

pattern = r"[ ,.]"
re.sub(pattern, ":", text)

pattern = r"^a.*b$"
^a – строка начинается с 'a'.
.* – любое количество любых символов.
b$ – строка заканчивается на 'b'.

"w" – запись (стирает старое содержимое)
"a" – добавление в конец файла
"r" – только для чтения
"r+" – чтение и запись

def count_lines(filename):
    with open(filename, "r") as f:
        return sum(1 for _ in f)

def write_list_to_file(filename, my_list):
    with open(filename, "w") as f:
        f.write("\n".join(map(str, my_list)))

write_list_to_file("file.txt", [10, 20, 30, "hello"])
