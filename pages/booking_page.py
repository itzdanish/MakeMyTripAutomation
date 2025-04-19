import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class MAKEMYTRIP:

    def __init__(self,driver): # This must be set before initializing the driver
        self.driver=driver
        self.source_name=(By.XPATH, "//*[text()='From']")
        self.source_input=(By.XPATH, "//*[@aria-haspopup='listbox']//input")
        self.dest_name = (By.XPATH, "//*[text()='To']")
        self.dest_input = (By.XPATH, "//*[@aria-haspopup='listbox']//input")
        self.Date_caption=(By.XPATH, "//div[contains(@class,'DayPicker-Caption')][1]")
        self.right_navigator = (By.XPATH, "//span[contains(@role,'button')][2]")
        self.select_j_start_date=(By.XPATH,"//div[@class='DayPicker-Month'][1]/div[3]//div[@aria-disabled='false']//p[1]")
        self.return_label_click=(By.XPATH,"//span[contains(text(),'Return')]")
        self.return_date_select = (By.XPATH,"//div[@class='DayPicker-Month'][1]/div[3]//div[@aria-disabled='false']//p[1]")
        self.travel_class=(By.XPATH,"//span[contains(text(),'Travellers & Class')]")
        self.seat_count_select=(By.XPATH,"//div[contains(@class,'fltTravellers')]//ul[1]/li[contains(@data-cy,'adult')]")
        self.detail_apply_btn=(By.XPATH,"//button[contains(text(),'APPLY')]")

    # helper function to make dynamic change to destination
    def get_source_select_locator(self, source_code):
        return (By.XPATH, f"//*[text()='{source_code}']/parent::div")

    def select_source(self,source):
        self.driver.find_element(*self.source_name).click()
        time.sleep(2)
        search = self.driver.find_element(*self.source_input)

        search.send_keys(source)
        time.sleep(2)
        try:
           source_locator = self.get_source_select_locator(source)
           from_input=self.driver.find_element(*source_locator)
           ActionChains(self.driver).move_to_element(from_input).click().perform()
        except:
           pass

    # helper function to make dynamic change to destination
    def get_destination_select_locator(self, destination_code):
        return (By.XPATH, f"//*[text()='{destination_code}']/parent::div")

    def select_dest(self,destination):
        self.driver.find_element(*self.dest_name).click()
        time.sleep(2)
        search1 = self.driver.find_element(*self.dest_input)
        search1.send_keys(destination)
        try:
            destination_locator = self.get_destination_select_locator(destination)
            from_input = self.driver.find_element(*destination_locator)
            ActionChains(self.driver).move_to_element(from_input).click().perform()
            time.sleep(3)
        except:
           pass

    def select_start_date(self,date1,month,year):
        time.sleep(2)
        month_date1 = month + " " + year

        # Step 1: Navigate to the correct month
        while True:
            month_year = self.driver.find_element(*self.Date_caption).text
            if month_year == month_date1:
                break
            else:
                next_button = self.driver.find_element(*self.right_navigator)
                next_button.click()
                time.sleep(1)

        # Step 2: Select the date
        time.sleep(1)  # slight wait to ensure calendar finishes rendering
        dates = self.driver.find_elements(*self.select_j_start_date)

        for ele in dates:
            if ele.text.strip() == date1:
                ele.click()
                break  # Exit loop immediately after clicking

        time.sleep(2)  # Give time after clicking

    def select_return_date(self,date2,month2,year2):
        time.sleep(2)
        month_date2 = month2 + year2

        return_box=self.driver.find_element(*self.return_label_click)
        return_box.click()
        time.sleep(2)

        # Step 1: Navigate to the correct month
        while True:
            j_return_month_year = self.driver.find_element(*self.Date_caption).text
            if j_return_month_year == month_date2:
                break
            else:
                next_button = self.driver.find_element(*self.right_navigator)
                next_button.click()
                time.sleep(1)

        # Step 2: Select the date
        time.sleep(1)  # slight wait to ensure calendar finishes rendering
        return_dates = self.driver.find_elements(*self.return_date_select)

        for ele1 in return_dates:
            if ele1.text.strip() == date2:
                ele1.click()
                break  # Exit loop immediately after clicking

        time.sleep(2)  # Give time after clicking

    # def search_flight(self):
    #     self.driver.find_element(By.XPATH,"//a[contains(text(),'Search')]").click()
    #     self.driver.implicitly_wait(3)
    #
    # def booking_list(self):
    #     self.driver.implicitly_wait(20)
    #     button = self.driver.find_element(By.XPATH, "//a[contains(@class,'widgetSearchBtn')]")
    #     button.click()
    #     self.driver.implicitly_wait(10)
    #     print("Done")

    def traveller_class(self):
        self.driver.find_element(*self.travel_class).click()
        time.sleep(2)
        seats=3
        seat_list=self.driver.find_elements(*self.seat_count_select)
        for data in seat_list:
            if data.text.strip()==str(seats):
                data.click()
                print("Seat selected!")
                break  # Exit loop immediately after clicking

        apply=self.driver.find_element(*self.detail_apply_btn)
        apply.click()
        time.sleep(2)



