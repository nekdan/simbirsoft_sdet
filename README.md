Тестовое задание **SimbirSoft SDET**.  
Запустить тест с формированием отчёта можно из корня проекта с помощью комманды:  
`pytest -s -v test_registration_page.py --alluredir e2e_report` - где e2e_report папка в которой будет создан отчёт.  
Просмотреть отчёт можно с помощью команды:  
`allure serve e2e_report` 
