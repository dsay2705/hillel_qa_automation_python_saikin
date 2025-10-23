#!/bin/bash
# Запуск тестів у Docker, збереження історії Allure та відкриття репорту

docker-compose up --abort-on-container-exit --build

if [ -d allure-report/history ]; then
  cp -r allure-report/history allure-results/
fi

allure generate allure-results -o allure-report --clean
allure open allure-report
