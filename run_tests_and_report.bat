rmdir /s /q allure-results
rmdir /s /q allure-report
pytest --alluredir=allure-results
allure generate allure-results --clean -o allure-report
start allure-report\index.html
