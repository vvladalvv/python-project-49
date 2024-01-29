Install: # установка зависимостей
	poetry install

brain-games: # запуск программы
	poetry run brain-games

build: # сборка пакета
	poetry build

publish: # публикация пакета на pypi
	poetry publish --dry-run

package-install: # установка пакета из dist 
	python3 -m pip install --user dist/*.whl

lint: # проверка кода на ошибки
	poetry run flake8 brain_games

brain-even:
	poetry run brain-even
