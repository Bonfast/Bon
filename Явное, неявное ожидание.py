import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPetFriendsPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://petfriends.skillfactory.ru/my_pets")

    def tearDown(self):
        self.driver.quit()

    def test_all_pets_present(self):
        pets = self.driver.find_elements(By.XPATH, "//div[@class='card-pet card']//h4")
        self.assertGreater(len(pets), 0, "Список питомцев пуст")

    def test_at_least_half_pets_have_photos(self):
        pets = self.driver.find_elements(By.XPATH, "//div[@class='card-pet card']//h4")
        pet_photos = self.driver.find_elements(By.XPATH, "//div[@class='card-pet card']//img")
        self.assertGreaterEqual(len(pet_photos), len(pets) / 2, "Меньше половины питомцев имеют фото")

    def test_all_pets_have_name_age_breed(self):
        pets = self.driver.find_elements(By.XPATH, "//div[@class='card-pet card']")
        for pet in pets:
            pet_info = pet.text
            self.assertTrue("Имя:" in pet_info and "Возраст:" in pet_info and "Порода:" in pet_info, "У питомца нет имени, возраста или породы")

    def test_all_pets_have_unique_names(self):
        pets = self.driver.find_elements(By.XPATH, "//div[@class='card-pet card']//h4")
        names = [pet.text for pet in pets]
        self.assertEqual(len(names), len(set(names)), "Есть питомцы с повторяющимися именами")

    def test_no_duplicate_pets_in_the_list(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='infinity-loading']"))
        )
        pets = self.driver.find_elements(By.XPATH, "//div[@class='card-pet card']//h4")
        self.assertEqual(len(pets), len(set(pets)), "Есть повторяющиеся питомцы в списке")

if __name__ == "__main__":
    unittest.main()
