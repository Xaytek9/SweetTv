from components import config
from components.main_page import MainPage
from tests.utils.driver_initilization import driver_initialization


def test_login():

    driver = driver_initialization()
    main_page = MainPage(driver)
    mail = config.MAIL
    password = config.PASSWORD

    main_page.click_on_sign_in()
    assert ("Sign in or sign up" in main_page.get_text() or "Увійди або зареєструйся" in main_page.get_text())
    main_page.click_on_google_logo()

    # Switching to a new window
    main_window = driver.window_handles[0]
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[1])

    main_page.fill_in_mail(mail)
    main_page.click_on_button_next_in_google_form_login()

    main_page.fill_in_password(password)
    main_page.click_on_button_next_in_google_form_password()
    main_page.confirm_sing_in()

    # Return to main window
    driver.switch_to.window(main_window)

    # Close promotion if apper
    main_page.select_promotion()

    # Check user data
    main_page.enter_cabinet_page()
    assert (mail in main_page.get_user_datas())
