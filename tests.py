import io
import unittest
from unittest import mock
import utility
from main import *


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

    def test_get_jsons(self):
        with mock.patch('utility.listdir', return_value=['ko.json', 'en.json.json', 'ru', 'ar.csv']):
            self.assertEqual(utility.get_jsons(), ['ko.json', 'en.json.json'])

    def test_parse(self):
        with mock.patch('utility.open', return_value=io.StringIO('''{
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
        }''')):
            self.assertEqual(utility.parse("file"), {
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
            })
        with mock.patch('utility.open', return_value=io.StringIO('')):
            self.assertEqual(utility.parse("file"), dict())


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
        del self.test_data["test_data"]
        self.generator = Generator(("tests", self.test_data))
        with self.assertRaises(LocalizationNotFoundError):
            if "test_data" not in self.generator.pds:
                raise LocalizationNotFoundError("test_data", "test")
            self.generator.random_person("m", "test_data")

    def test_generate_error(self):
        self.test_data["test_data"]["job"] = ()
        self.generator = Generator(("tests", self.test_data))
        with self.assertRaises(NothingGeneratedError):
            self.generator.random_job("test_data")

    def test_not_full_error(self):
        del self.test_data["test_data"]["address"]
        self.generator = Generator(("tests", self.test_data))
        with self.assertRaises(NotFullLocalizationError):
            self.generator.random_address("test_data")

    def test_invalid_argument(self):
        self.generator = Generator(("tests", self.test_data))
        with self.assertRaises(utility.InvalidArgumentError):
            self.generator.random_person("male", "test_data")
        with self.assertRaises(utility.InvalidArgumentError):
            self.generator.random_person("female", "test_data")
        with self.assertRaises(utility.InvalidArgumentError):
            self.generator.random_person("men", "test_data")
        with self.assertRaises(utility.InvalidArgumentError):
            self.generator.random_person("fem", "test_data")


if __name__ == '__main__':
    unittest.main()
