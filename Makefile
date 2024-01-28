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
	