# Написать тест на проверку названия Issue в репозитории через Web-интерфейс.
#
#
# 2. Лямбда шаги через with allure.step
#
# 4. Разметку тестов всеми аннотациями
import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


def test_dynamic_steps():
    with allure.step('Открывем главную страницу'):
        browser.open('/')

    with allure.step('Ищем репозиторий'):
        browser.element('[data-target="qbsearch-input.inputButtonText"]').click()
        browser.element('[id="query-builder-test"]').send_keys('/eroshenkoam/allure-example').press_enter()

    with allure.step('Переходим по ссылке репозитория'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем таб  Issues'):
        browser.element('[id="issues-tab"]').click()

    with allure.step('Проверяем наличие issue с номером 76'):
        browser.element(by.partial_text('#76')).should(be.visible)


def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('#76')

@allure.step('Открывем главную страницу')
def open_main_page():
    browser.open('/')


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    browser.element('[data-target="qbsearch-input.inputButtonText"]').click()
    browser.element('[id="query-builder-test"]').send_keys(repo).press_enter()


@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Открываем таб  Issues')
def open_issue_tab():
    browser.element('[id="issues-tab"]').click()

@allure.step('Проверяем наличие issue с номером {number}')
def should_see_issue_with_number(number):
    browser.element(by.partial_text(number)).should(be.visible)