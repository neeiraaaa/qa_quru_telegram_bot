from selene import command, have
from selene.support.shared import browser

from demoqa_tests.data.user_data import User
from demoqa_tests.model.controls.checkbox import Checkbox
from demoqa_tests.model.controls.dropdown import Dropdown
from demoqa_tests.model.controls.option_select import Select
from demoqa_tests.model.controls.radiobutton import Radio
from demoqa_tests.utils import add_path


class Form:

    def __int__(self, user: User):
        self.user = user

    def validation(self, *args):
        browser.element('.table').all('td').even.should(have.texts(args))

    def given_opened(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def add_name_and_surname(self, user):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)

    def add_contacts(self, user):
        browser.element('#userEmail').type(user.email)
        browser.element('#userNumber').type(user.mobile)
        browser.element('#currentAddress').type(user.address)

    def add_subject(self, user):
        browser.element('#subjectsInput').type(user.subject).press_enter()

    def choose_hobby(self, user):
        browser.element('[for="hobbies-checkbox-3"]').perform(command.js.scroll_into_view)
        Checkbox.click_checkbox('[for^=hobbies-checkbox]', user.hobby)

    def add_state(self, user):
        Dropdown.choose('#state', user.state)

    def add_city(self, user):
        Dropdown.choose('#city', user.city)

    def submit(self):
        browser.element('#submit').with_(click_by_js=True).press_enter()

    def choose_gender(self, user):
        Radio.radio_button('[name=gender]', user.gender)

    def select_month(self, user):
        browser.element('.react-datepicker__month-select').click()
        Select.select_by_text('.react-datepicker__month-select', user.birth_month)

    def select_year(self, user):
        browser.element('.react-datepicker__year-select').click()
        Select.select_by_text('.react-datepicker__year-select', user.birth_year)

    def select_day(self, user):
        browser.element(f'.react-datepicker__day--0{user.birth_day}').click()

    def send_file(self):
        path = add_path.get_path('resources/img1.png')
        browser.element('#uploadPicture').set_value(path)

    def click(self, locator):
        browser.element(locator).click()

    def add_birthday(self, user):
        self.click('#dateOfBirthInput')
        self.select_month(user)
        self.select_year(user)
        self.select_day(user)

    def submit_form(self, user):
        self.given_opened()
        self.add_name_and_surname(user)
        self.add_contacts(user)
        self.choose_gender(user)
        self.add_birthday(user)
        self.add_subject(user)
        self.choose_hobby(user)
        self.send_file()
        self.add_state(user)
        self.add_city(user)
        self.submit()

    def validate_form(self, user):
        user_birth = f'{user.birth_day} {user.birth_month},{user.birth_year}'
        user_full_name = user.first_name + ' ' + user.last_name
        user_place = user.state + ' ' + user.city

        self.validation(
            user_full_name,
            user.email,
            user.gender,
            user.mobile,
            user_birth,
            user.subject,
            user.hobby,
            user.picture,
            user.address,
            user_place
        )