**Приложение**

Платформа для онлайн-обучения, на которой каждый желающий сможет размещать свои полезные материалы или курсы.

## Инструкция по установке:

1. Клонировать с GitHab (*git clone https://github.com/AlexOst97/Homework_Django_REST*)
2. Установить зависимости (*pip install -r requirements.txt*)


## Инструкция по запуску проекта:

1. Установите Docker, Docker Compose;
2. Запустите проект (docker-compose up -d)
3. Проверьте работоспособность (http://localhost:8000)
4. - Для просмотра запущенных контейнеров: *docker-compose ps*
   - Для просмотра логов всех контейнеров: *docker-compose logs*
   - Для остановки сервисов и удаления контейнеров: *docker-compose down*


## Настройка сервера:
1. Войдите в систему виртуальной машины для настройки сервиса: *ssh test@130.193.57.90*
2. В терминале выполните команду для обновления списка пакетов: *sudo apt update*
3. Выполните команду для обновления всех установленных пакетов до их последних версий: *sudo apt upgrade*
4. Установите Docker, по инструкции с официального сайта:: *https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository*
5. Активируйте файрвол: *sudo ufw enable*
6. Откройте необходимые порты: Порт 80 для HTTP (*sudo ufw allow 80/tcp*), Порт 443 для HTTPS (*sudo ufw allow 443/tcp*), Порт 22 для SSH (*sudo ufw allow 22/tcp*)


## Команда проекта:

- Останин Александр (*aostanin97@gmail.com*) - **backend developer** 

## Источники

Программа создана при поддержке онлайн-школы
![Программа создана при поддержке онлайн-школы](https://digital-academy.ru/foto/school/skypro-2.png)