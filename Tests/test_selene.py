# Написать тест на проверку названия Issue в репозитории через Web-интерфейс.
#
# 1. Чистый Selene (без шагов)
#
# 4. Разметку тестов всеми аннотациями
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


def test_selene_to_search_issue():
    browser.open('/')
    browser.element('[data-target="qbsearch-input.inputButtonText"]').click()
    browser.element('[id="query-builder-test"]').send_keys('/eroshenkoam/allure-example').press_enter()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('[id="issues-tab"]').click()
    browser.element(by.partial_text('#76')).should(be.visible)
