# Задание 2: "API-тесты" курс ЯндексПрактикум | Diplom_2

Предметом тестирования является сайт [Stella Burgers](https://stellarburgers.nomoreparties.site/) 
> Космический фастфуд: можно собрать и заказать бургер из необычных ингредиентов.

При написании проекта использованы библиотеки:
 * `pytest`
 * `allure`


### Структура проекта:

 * `data` - директория страниц
 * `tests` - директория тестов
 * `conftest.py` - фикстуры
 * `requirements` - внешние зависимости
 * `README.md` - описание проекта
 * `allure_results` - результаты тестирования

### Настройка и запуск:
1. Установить зависимости — `pip install -r requirements.txt`
2. Запустить тесты — `pytest tests`
3. Запустить тесты с записью отчета в allure_results: `pytest tests --alluredir=allure_results`
4. Сформировать html отчет тестирования: _`allure serve allure_results`_