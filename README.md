# dr.web_test

Интерактивное консольное приложение, напоминающее интерфейс базы
данных. Данные запрашиваются у пользователя в диалоговом режиме (ввод
с клавиатуры). Вся "база" находится в оперативной памяти и не
сохраняется между сеансами. Одна команда — один запрос. Аргументы
команд пробелов не содержат. Также в вводе должен рапознаваться EOF,
который означает конец ввода и завершение приложения.


Команды:
SET - сохраняет аргумент в базе данных.
GET - возвращает, ранее сохраненную переменную. Если такой переменной
не было сохранено, возвращает NULL
UNSET - удаляет, ранее установленную переменную. Если значение не было
установлено, не делает ничего.
COUNTS - показывает сколько раз данные значение встречается в базе данных.
FIND - выводит найденные установленные переменные для данного значения.
END - закрывает приложение.

Пример:
```
> GET A
NULL
> SET A 10
> GET A
10
> COUNTS 10
1
> SET B 20
> SET C 10
> COUNTS 10
2
> UNSET B
> GET B
NULL
> END
```


Также "база" должна поддерживать транзакции. Транзакции могут быть
вложенными.

BEGIN - начало транзакции.
ROLLBACK - откат текущей (самой внутренней) транзакции
COMMIT - фиксация изменений текущей (самой внутренней) транзакции

Пример:
```
> BEGIN
> SET A 10
> BEGIN
> SET A 20
> BEGIN
> SET A 30
> GET A
30
> ROLLBACK
> GET A
20
> COMMIT
> GET A
20
```
