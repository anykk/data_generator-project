import unittest
from main import *
from utility import *


class TestGeneratorMethods(unittest.TestCase):
    def setUp(self):
        self.test_data = {"test_data": {
            "address": {
                "city": "some_city",
                "street": "some_street"
            },
            "person": {
                "m": {
                    "first_name": "some_first_name_m",
                    "last_name": "some_last_name_m"},
                "f": {
                    "first_name": "some_first_name_f",
                    "last_name": "some_last_name_f"
                }
            },
            "job": "some_job"
        }
        }
        self.generator = Generator(("tests", self.test_data))

    def test_random_person(self):
        m_person = self.generator.random_person("m", "test_data").split()
        self.assertTrue(m_person[0] in self.generator.pds["test_data"]["person"]["m"]["first_name"] and
                        m_person[1] in self.generator.pds["test_data"]["person"]["m"]["last_name"])
        f_person = self.generator.random_person("f", "test_data").split()
        self.assertTrue(f_person[0] in self.generator.pds["test_data"]["person"]["f"]["first_name"] and
                        f_person[1] in self.generator.pds["test_data"]["person"]["f"]["last_name"])

    def test_random_address(self):
        address = self.generator.random_address("test_data").split()
        self.assertTrue(address[0] in self.generator.pds["test_data"]["address"]["city"] and
                        address[1] in self.generator.pds["test_data"]["address"]["street"])

    def test_random_job(self):
        job = self.generator.random_job("test_data")
        self.assertTrue(job in self.generator.pds["test_data"]["job"])

    def test_random_number(self):
        number = self.generator.phone_number()
        self.assertEqual(len(str(number)), 11)

    def test_password(self):
        password = self.generator.password(12)
        self.assertEqual(len(password), 12)


class DataMethodsTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_pds(self):
        pass


class ErrorTests(unittest.TestCase):
    def setUp(self):
        self.test_data = {"test_data": {
            "address": {
                "city": "some_city",
                "street": "some_street"
            },
            "person": {
                "m": {
                    "first_name": "some_first_name_m",
                    "last_name": "some_last_name_m"},
                "f": {
                    "first_name": "some_first_name_f",
                    "last_name": "some_last_name_f"
                }
            },
            "job": "some_job"
        }
        }

    def test_not_found_error(self):
        pass

    def test_generate_error(self):
        pass

    def test_not_full_error(self):
        pass


if __name__ == '__main__':
    unittest.main()
