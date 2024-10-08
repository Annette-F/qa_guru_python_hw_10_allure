import allure
from allure_commons.types import Severity


def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.label('owner', 'Annette-F')
    allure.dynamic.feature('Задачи в репозитории')
    allure.dynamic.story('Не авторизованный пользователь не может создать задачу в репозитории')
    allure.dynamic.link('https://github.com', name='Testing')


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Задачи в репозитории')
@allure.story('Авторизованный пользователь может создать задачу в репозитории')
@allure.link('https://github.com', name='Testing')
def test_decorator_labels():
    pass
