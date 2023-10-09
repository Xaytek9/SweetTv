import time
from components import config
from components.main_page import MainPage
from tests.utils.driver_initilization import driver_initialization


def test_login_with_invalid_sms_code():

    driver = driver_initialization()
    main_page = MainPage(driver)
    mobile = config.MOBILE

    main_page.click_on_sign_in()
    assert ("Sign in or sign up" in main_page.get_text() or "Увійди або зареєструйся" in main_page.get_text())
    main_page.click_on_login_phone()
    main_page.fill_in_mobile_field(mobile)
    main_page.click_on_get_sms_button_valid()
    assert ("Надісланого на номер +380" + mobile in main_page.get_text_from_multilogin_popup())
    main_page.fill_in_sms_field("0000")
    time.sleep(2)
    assert ("Упс, щось пішло не так. Повторіть спробу. Якщо це не допомогло, пишіть на info@sweet.tv" in main_page.get_text_error_wrong_sms())

def test_login_with_empty_mobile_bumber():

    driver = driver_initialization()
    main_page = MainPage(driver)

    main_page.click_on_sign_in()
    assert ("Sign in or sign up" in main_page.get_text() or "Увійди або зареєструйся" in main_page.get_text())
    main_page.click_on_login_phone()
    main_page.click_on_get_sms_button_invalid()
    assert ("Введіть номер телефону, щоб продовжити" in main_page.get_text_error_empty_mobile_number())

def test_login_with_empty_sms_code():

    driver = driver_initialization()
    main_page = MainPage(driver)
    mobile = config.MOBILE

    main_page.click_on_sign_in()
    assert ("Sign in or sign up" in main_page.get_text() or "Увійди або зареєструйся" in main_page.get_text())
    main_page.click_on_login_phone()
    main_page.fill_in_mobile_field(mobile)
    main_page.click_on_get_sms_button_valid()
    assert ("Надісланого на номер +380" + mobile in main_page.get_text_from_multilogin_popup())
    assert not main_page.is_button_disable()
