## More Tech 4.0 Backend

### Шаг 1. Требования

- Linux (Ubuntu)
- Python 3.5+
- PostgreSQL

### Шаг 2) Установка
Введите в psql:

```
CREATE DATABASE more_tech4;
```

Введите в терминале:

```
sudo apt update && sudo apt -y dist-upgrade
sudo apt install -y git python3-venv libpq-dev gcc postgresql
git clone https://github.com/vahellame/more_tech4_backend.git
cd more_tech4_backend
python3 -m venv venv
./venv/bin/pip install -U pip wheel
./venv/bin/pip install -r requirements.txt
PYTHONPATH=$PWD ./venv/bin/python common/init.py
```


### Шаг 3) Настройка

Просмотрите и отредактируйте `src/config.py`

Просмотрите и отредактируйте `common/mt-backend.service`

```
sudo cat common/mt-backend.service > /usr/lib/systemd/system/mt-backend.service
sudo systemctl daemon-reload
sudo systemctl enable mt-backend.service
sudo systemctl start mt-backend.service
```

Также на нашем сервере настроен Nginx и SSL, но делать это необязательно
