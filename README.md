# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Установите зависимости командой:
  ```
  pip install -r requirements.txt
   ```
- Запустите сайт командой:
  ```
  python main.py
  ```
  В этом случае скрипт запустится с аргументом `--path`(или `-p`), по умолчанию:
  ```
  python main.py -p=table_wine.xlsx или (python main.py --path=table_wine.xlsx)
  ```
- Скрипт принимает позиционный аргумент `--path` (или `--p`), указывающий путь к файлу `table_wine.xlsx` с таблицей напитков следующего вида:  
  Категория | Название | Сорт | Цена | Картинка | Акция
  --- | --- | --- | --- | --- | --- |  
  Белые вина | Белая леди | Дамский пальчик | 399 | belaya_ledi.png | Выгодное предложение |  
  
  Поле "Картинка" указывается название файла в формате `png` или `jpg(jpeg)`,например `belaya_ledi.png`, сами файлы картинок необходимо расположить в папке
  `\images`
  

- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

