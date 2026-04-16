import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

class InputTesting(unittest.TestCase):
    BLOG_URL = "https://web.usos.pwr.edu.pl/kontroler.php?_action=logowaniecas/index&callback=g7YyNrVS0s%2F0zyspys9JLdIsryCiwj09MLsnMz7PNSy0v1k9JTUsszS1RsgYAa3d6d19f42e41bfa7f4bcd2d8d3b56d4b3a9d247"
    INPUT_NAME = "username"

    def setUp(self):
        options = Options()
        options.binary_location = '/snap/firefox/current/usr/lib/firefox/firefox'
        self.driver = webdriver.Firefox(options=options)

    def tearDown(self):
        self.driver.close()

    def test_input_value_and_clear_button(self):
        self.driver.get(self.BLOG_URL)
        try:
            login_box = self.driver.find_element(By.NAME, self.INPUT_NAME)
        except Exception:
            self.fail("Login input not found!")

        login_box.send_keys("test_login")
        inputValue = login_box.get_attribute("value")
        self.assertEqual("test_login", inputValue)

        try:
            clear_button = self.driver.find_element(By.XPATH, "//*[@type='reset' or @name='clear' or contains(text(), 'Clear')]")
            clear_button.click()
        except Exception:
            self.fail("There is no \"clear\" button on page")

        clearedValue = login_box.get_attribute("value")
        self.assertEqual("", clearedValue, "Field is not cleared")

if __name__ == "__main__":
    unittest.main() 