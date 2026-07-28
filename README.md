# INQ Marks

Мод прогресу відміток на гарматі для World of Tanks. Показує поточний і прогнозований відсоток відмітки, зміну після бою, орієнтовний сумарний урон та найближчі планки.

Проєкт містить окремі інтерфейси для ангара й бою, написані на ActionScript 3, та Python-частину для отримання статистики, розрахунків і взаємодії з клієнтом гри.

## Можливості

- відображення прогресу відмітки в ангарі та під час бою;
- прогноз зміни відсотка з кольоровою дельтою;
- розрахунок поточного сумарного урону;
- планки 65%, 85%, 95% і 100%;
- окреме оформлення позитивної та негативної динаміки;
- згортання, розгортання та переміщення панелей;
- збереження вибраного стилю та позицій;
- локалізації українською, англійською та російською.

## Стилі

Стиль задається одним параметром і застосовується в бою та, якщо підтримується, в ангарі.

| Значення | Ангар | Бій | Опис |
|---|:---:|:---:|---|
| `classic` | ✓ | ✓ | Класичний блок із рамкою |
| `compact` | ✓ | ✓ | Компактний сегментований інтерфейс |
| `polaroid` | ✓ | ✓ | Напівпрозора панель у стилі оригінального Gun Marks |
| `neer` | — | ✓ | Альтернативний бойовий індикатор |
| `minimal` | — | ✓ | Мінімалістичний бойовий індикатор |

Для стилів без ангарної версії панель в ангарі не показується.

## Керування

- панель можна перетягувати мишею;
- короткий клік по ангарній панелі `compact` або `polaroid` перемикає згорнутий і розгорнутий стани;
- перетягування не спрацьовує як клік;
- `Alt` тимчасово показує розгорнуту бойову інформацію;
- `Ctrl` показує бойовий елемент згортання/розгортання;
- клік по бойовій панелі `polaroid` також перемикає її стан.


## Налаштування стилю

Приклад `marks.json`:

```json
{
    "battleBadgeStyle": "compact"
}
```

Допустимі значення:

```text
classic
compact
polaroid
neer
minimal
```

Некоректне або відсутнє значення автоматично замінюється на `classic`.

Старі параметри `badgeStyle` і `garageBadgeStyle` підтримуються лише для автоматичного перенесення налаштувань. Актуальний параметр — `battleBadgeStyle`.

## Структура проєкту

```text
MARKS-main/
├─ as3/
│  ├─ bin/                         # скомпільовані SWF
│  ├─ libs/                        # бібліотеки клієнта та playerglobal
│  └─ src_flash/
│     ├─ InqMarksPanelHangar.as3proj
│     ├─ InqMarksPanelBattle.as3proj
│     └─ src/com/inq/marks/        # вихідний код інтерфейсів
├─ python/gui/mods/                # Python-модулі клієнта
├─ resources/in/mods/inq.marks/    # локалізації
├─ build.py                        # пакування .wotmod
├─ build.example.json              # приклад конфігурації збірки
└─ .github/workflows/release.yml   # автоматична збірка та реліз
```

Основні файли інтерфейсу:

- `InqMarksPanelComponent.as` — ангарна панель;
- `InqMarksBattleRendererBase.as` — базова логіка бойових стилів;
- `InqMarksPanelHangar.as` — точка входу ангарного SWF;
- `InqMarksPanelBattle.as` — точка входу бойового SWF.

## Локальна збірка SWF

Потрібні:

- Apache Flex SDK 4.16.1;
- Java;
- `playerglobal.swc` для Flash Player 32;
- бібліотеки з `as3/libs`.

Найпростіший варіант — відкрити у FlashDevelop:

```text
as3/src_flash/InqMarksPanelHangar.as3proj
as3/src_flash/InqMarksPanelBattle.as3proj
```

Результати мають бути створені за такими шляхами:

```text
as3/bin/InqMarksPanelHangar.swf
as3/bin/InqMarksPanelBattle.swf
```

GitHub Actions компілює обидва SWF через `mxmlc` із такими основними параметрами:

```text
-target-player=32.0
-swf-version=39
-strict=true
-optimize=true
-warnings=true
-use-network=true
```

Усі `.swc` із `as3/libs`, крім `playerglobal.swc`, підключаються як зовнішні бібліотеки.

## Збірка WOTMOD

Для компіляції клієнтських `.pyc` потрібен Python 2.7. Сам пакувальник `build.py` запускається через Python 3.

1. Створи локальну конфігурацію:

   ```powershell
   Copy-Item build.example.json build.json
   ```

2. У `build.json` укажи шлях до Python 2.7 та версію мода:

   ```json
   {
       "software": {
           "python": "C:/Python27/python.exe"
       },
       "info": {
           "id": "com.inq.marks",
           "name": "INQ Marks",
           "description": "INQ Marks of Excellence progress mod",
           "version": "0.1.0"
       }
   }
   ```

3. Переконайся, що обидва SWF уже знаходяться в `as3/bin`.
4. Запусти пакування:

   ```powershell
   python build.py
   ```

Готовий файл:

```text
build/com.inq.marks_<version>.wotmod
```

Пакет створюється без ZIP-стиснення та містить:

- `meta.xml`;
- три скомпільовані Python-модулі;
- ангарний і бойовий SWF;
- три файли локалізації.

## Автоматична збірка

Workflow **Build and Release INQ Marks** запускається:

- вручну через `Actions → Build and Release INQ Marks → Run workflow`;
- автоматично для тегів формату `v*`.

Workflow:

1. встановлює Python 2.7, Python 3 і Java;
2. завантажує Apache Flex SDK;
3. компілює обидва SWF;
4. створює `.wotmod`;
5. завантажує артефакт;
6. створює або оновлює GitHub Release.

## Обмеження

Мод призначений для стандартних випадкових боїв. Панель не показується в реплеях, генеральній битві, «Натиску», «Лінії фронту», Mapbox та інших спеціальних режимах, для яких розрахунок не гарантується.

## Ідентифікатори

- ID пакета: `com.inq.marks`;
- назва: `INQ Marks`;
- ранній завантажувач конфігурації: `mod_00_inq_marks_config.pyc`;
- основний модуль: `mod_inq_marks.pyc`;
- правила конфігурації: `mod_inq_marks_rules.pyc`.
