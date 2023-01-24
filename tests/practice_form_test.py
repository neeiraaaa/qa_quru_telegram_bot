import allure
from allure_commons.types import Severity

from demoqa_tests.model.pages.practice_form import Form
from demoqa_tests.data.user_data import irina_rogova


@allure.title("Successful fill form")
def test_submitting_form():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.label('owner', 'rogova_irina')
    allure.dynamic.feature('Successful fill form')

    form = Form()

    with allure.step('submit_form'):
        form.submit_form(irina_rogova)

    with allure.step('validate_form'):
        form.validate_form(irina_rogova)