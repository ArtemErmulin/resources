# python

## pyenv

*Установка*

Библиотеки для компиляции Python.  
Для Debian / Ubuntu / Linux Mint
```bash
$ sudo apt install curl git-core gcc make zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libssl-dev
```

Клонируем последнюю актуальную версию с github:
```bash
$ git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv
```

Добавим в файл `~/.bashrc` следующие строчки:
```bash
## pyenv configs
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi
```

Перезагрузим файл `~./bashrc`
```bash
$ source ~/.bashrc
```

*Использование*

Список всех доступных версий Python для установки
```bash
$ pyenv install -l
```

Установка определенной версии Python
```bash
$ pyenv install 3.7.4
```

Список всех версий Python, доступных для `pyenv`
```bash
$ pyenv versions
```

Просмотр глобальной версии Python
```bash
$ pyenv global
```

Установка глобальной версии Python
```bash
$ pyenv global 3.7.4
```

Установка локальной версии Python (в определенном репозитории)
```bash
$ pyenv local 3.7.4
```

Pyenv управляет виртуальными средами через плагин pyenv-virtualenv, который автоматизирует управление виртуальными и консольными средами для Python в Linux и других UNIX-подобных системах.
Установим данный плагин
```bash
$ git clone https://github.com/yyuu/pyenv-virtualenv.git   $HOME/.pyenv/plugins/pyenv-virtualenv
$ source ~/.bashrc
```

Теперь мы создадим тестовую виртуальную среду, называемую venv_project1, в проекте под названием project1:
```bash
$ cd python_projects
$ mkdir project1
$ cd project1
$ pyenv virtualenv 3.7.4 venv_project1
```

Теперь, когда вы выводите все версии Python, также должны быть указаны ваши виртуальные среды, а также их локальные версии python, как показано на скриншоте.
```bash
$ pyenv versions
```

При возникновении ошибки типа
```
UserWarning: Could not import the lzma module. Your installed Python is incomplete. Attempting to use lzma compression will result in a RuntimeError.
  warnings.warn(msg)
```
Небходимо установить модуль
```bash
$ sudo apt-get install liblzma-dev
```
и заново переустановить версию Python.

# python-packages
## Jupyter-notebook

Jupyther-notebook можно установить через `pip`.

```bash
$ sudo pipX.X install jupyter
```

Далее, настроим рабочую папку для jupyter. Для этого создадим файл конфигурации jupyter-notebook.

```bash
$ jupyter-notebook --generate-config
```

В результате выполнения появится путь, куда файл конфигурации помещен. Необходимо открыть созданный файл.

```bash
$ xdg-open jupyter_notebook_config.py
```

Далее необходимо заменить строку

```bash
#c.NotebookApp.notebook_dir = ''
```

на

```bash
 c.NotebookApp.notebook_dir = '/your/path/'
```

Далее сохраняем файл.


## Установим необходимые инструменты для Python

### Библиотеки

```bash
$ sudo pipX.X --upgrade install matplotlib pandas plotly scikit-learn scipy seaborn
$ sudo pipX.X --upgrade install statsmodels nose tqdm pydot pydotplus watermark
$ sudo pipX.X --upgrade install geopy joblib pillow
$ sudo apt-get -y install graphviz
```

Для работы с БД SQL.

```bash
$ sudo pipX.X install sqlalchemy
$ sudo apt-get install python3-dev
$ sudo apt-get install unixodbc-dev
$ sudo pipX.X install pyodbc
```


## Обновляем версию Python

Если необходимо обновить версию Python до последней версии, то необходимо:

1. Перед установкой Python из исходников, установим необходимые пакеты

```bash
$ sudo apt install build-essential checkinstall

$ sudo apt install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev
```

2. Скачаем исходники [с официального сайта](http://python.org). Далее, разархивируем скаченный архив:

```bash
$ tar xvf Python-X.X.X.tgz
```

3. Перейдем в папку, сконфигурируем и установим:
```bash
$ cd Python-X.X.X
$ ./configure
$ sudo make altinstall
```

Новая версия Python установится в директорию `/usr/local/bin/`. Туда же устанавливается и `pipX.X`.

## Обновим версию `pip`

```bash
$ sudo pipX.X install --upgrade pip
```

Здесь `X.X` версия `pip`, которая установилась вместе с новой версией Python.
