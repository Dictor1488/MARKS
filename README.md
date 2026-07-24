# INQ Marks

Окремий мод прогресу відміток на стволі для World of Tanks.

## Ідентифікатор

- ID: `com.inq.marks`;
- назва: `INQ Marks`;
- основний Python-модуль: `mod_inq_marks.pyc`;
- правила режимів і конфігу: `mod_inq_marks_rules.pyc`;
- конфіг: `<World of Tanks>/mods/configs/inq/marks/marks.json`.

## Режими роботи

Мітка працює тільки у стандартних випадкових боях.

Вона не показується:

- у реплеях;
- у генеральній битві;
- у натиску;
- у лінії фронту;
- у Mapbox;
- у рангових, турнірних, кланових та інших спеціальних режимах.

## Інтерфейс

Мод має два SWF:

- `InqMarksPanelHangar.swf` — гаражна версія мітки;
- `InqMarksPanelBattle.swf` — мітка у випадковому бою.

Гараж і бій працюють у різних Scaleform-застосунках клієнта, тому це не дублікати.

## Стилі та конфіг

У конфігу вибирається одна мітка. Той самий стиль використовується у бою та, якщо для нього існує гаражна версія, у гаражі.

Доступні стилі:

- `classic` — бій і гараж;
- `compact` — бій і гараж;
- `polaroid` — бій і гараж;
- `neer` — тільки бій;
- `minimal` — тільки бій.

Приклад конфігу:

```json
{
  "badgeStyle": "classic"
}
```

Якщо вибраний стиль не має гаражної версії, гаражна мітка не показується.

Старий конфіг із `garageBadgeStyle` і `battleBadgeStyle` автоматично переноситься до одного параметра `badgeStyle`. Пріоритет має попередній бойовий стиль.

## Ручна збірка через GitHub Actions

1. Відкрий **Actions → Build and Release INQ Marks**.
2. Натисни **Run workflow**.
3. Вкажи версію мода.
4. Завантаж артефакт `com.inq.marks-<version>` або файл із створеного GitHub Release.

Артефакт містить тільки один файл:

```text
com.inq.marks_<version>.wotmod
```

Усередині `.wotmod` знаходяться рівно вісім файлів: `meta.xml`, два `.pyc`, два SWF і три локалізації. Пакет створюється без ZIP-стиснення.

Workflow має дозвіл `contents: write`, тому він може створювати та оновлювати GitHub Release.

## Локальна збірка

Створи `build.json` із шаблону та вкажи шлях до Python 2.7:

```bat
copy build.example.json build.json
python build.py
```

Перед запуском у `as3/bin` мають бути скомпільовані `InqMarksPanelHangar.swf` і `InqMarksPanelBattle.swf`.
