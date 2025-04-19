import pytest
from pages.booking_page import MAKEMYTRIP

@pytest.mark.regression
def test_booking(setup_driver):

    driver = setup_driver
    booking = MAKEMYTRIP(driver)

    booking.select_source("BOM")
    booking.select_dest("DEL")
    booking.select_start_date("10","August","2025")
    booking.select_return_date("23","September","2025")
    booking.traveller_class()

