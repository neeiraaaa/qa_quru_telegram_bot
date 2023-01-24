from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    mobile: str
    address: str
    gender: str
    birth_year: str
    birth_month: str
    birth_day: int
    subject: str
    hobby: str
    picture: str
    state: str
    city: str


irina_rogova = User(first_name='Irina',
                    last_name='Rogova',
                    email='neeiraaaa@gmail.com',
                    mobile='7925399999',
                    address='India',
                    gender='Female',
                    birth_year='1997',
                    birth_month='November',
                    birth_day=25,
                    subject='English',
                    hobby='Music',
                    picture='img1.png',
                    state='Uttar Pradesh',
                    city='Agra')