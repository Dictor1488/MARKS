# INQ Marks

Окремий мод прогресу відміток на стволі для World of Tanks.

## Ідентифікатор

- ID: `com.inq.marks`;
- назва: `INQ Marks`;
- Python-модуль: `mod_inq_marks.pyc`;
- конфіг: `<World of Tanks>/mods/configs/inq/marks/marks.json`.

## Інтерфейс

Мод має два необхідні SWF:

- `InqMarksPanelHangar.swf` — інтерфейс у гаражі;
- `InqMarksPanelBattle.swf` — бойова мітка та реплеї.

Гараж і бій працюють у різних Scaleform-застосунках клієнта, тому це не дублікати.

## Стилі

Гаражні: `classic`, `compact`, `polaroid`.

Бойові: `classic`, `compact`, `polaroid`, `neer`, `minimal`.

## Ручна збірка через GitHub Actions

1. Відкрий **Actions → Build INQ Marks**.
2. Натисни **Run workflow**.
3. Вкажи версію мода.
4. Завантаж артефакт `com.inq.marks-<version>`.

Артефакт містить тільки один файл:

```text
com.inq.marks_<version>.wotmod
```

Усередині `.wotmod` дозволено рівно сім файлів: `meta.xml`, один `.pyc`, два SWF і три локалізації. Збірка завершується помилкою, якщо з'явиться будь-який зайвий файл.

Workflow має лише право читання репозиторію та не створює комітів.

## Локальна збірка

Створи `build.json` із шаблону та вкажи шлях до Python 2.7:

```bat
copy build.example.json build.json
python build.py
```

Перед запуском у `as3/bin` мають бути скомпільовані `InqMarksPanelHangar.swf` і `InqMarksPanelBattle.swf`.

## Перевірка репозиторію

```bash
python tools/debug_check.py
```
