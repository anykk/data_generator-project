import unittest
import data.en as en
import data.ru as ru
from generator import Generator


class TestGeneratorMethods(unittest.TestCase):
    def setUp(self):
        self.generator = Generator()
        self.ru = ru
        self.en = en

    def test_random_person(self):
        person_ru_m = self.generator.random_person('m', 'ru').split()
        person_ru_f = self.generator.random_person('f', 'ru').split()
        person_en_m = self.generator.random_person('m', 'en').split()
        person_en_f = self.generator.random_person('f', 'en').split()
        self.assertTrue(
            person_ru_m[0] in self.ru.person.first_names_male and person_ru_m[1] in self.ru.person.last_names_male)
        self.assertTrue(
            person_ru_f[0] in self.ru.person.first_names_female and person_ru_f[1] in self.ru.person.last_names_female)
        self.assertTrue(
            person_en_f[0] in self.en.person.first_names_female and person_en_f[1] in self.en.person.last_names_female)
        self.assertTrue(
            person_en_m[0] in self.en.person.first_names_male and person_en_m[1] in self.en.person.last_names_male)

    def test_random_address(self):
        ru_address = self.generator.random_address('ru').split()
        en_address = self.generator.random_address('en').split()
        self.assertTrue(ru_address[0] in self.ru.address.city_names and ru_address[1] in self.ru.address.street_titles)
        self.assertTrue(en_address[0] in self.en.address.city_names and en_address[1] in self.en.address.street_titles)

    def test_random_job(self):
        ru_job = self.generator.random_job('ru')
        en_job = self.generator.random_job('en')
        self.assertTrue(ru_job in self.ru.job.jobs and en_job in self.en.job.jobs)

    def test_random_number(self):
        number = self.generator.phone_number()
        self.assertEquals(len(str(number)), 11)

    def test_password(self):
        password = self.generator.password(12)
        self.assertEquals(len(password), 12)


if __name__ == '__main__':
    unittest.main()