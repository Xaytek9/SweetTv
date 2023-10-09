import time
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


sign_in_button = "//*[@class='tabs-login load-login load-btn']"
login_phone = "//*[@class='l__login-phone-btn-google l__login-phone-btn']"
google_button = "//*[@class='social__buttons-google auth-modal__btn']"
google_form_button_next = "//*[@id='identifierNext']"
google_form_button_next_password = "//*[@id='passwordNext']"
mail_input = "//*[@type='email']"
password_input = "//*[@type='password']"
sms_input = "//*[@id='inputSMS']"
mobile_input = "//*[@id='loginInput']"
text_sign_in_or_sign_up = "//*[@translate='MULTILOGIN.LOGIN']"
google_form_confirm_sign_in = "//*[@id='confirm_yes']"
promotion = "//*[@ng-show='promotions.image_url']"
seven_free_days_button = "(//span[@class='promotions__text-top ng-binding'])[1]"
user_data = "//*[@class='lk-info-tab lk-info-tab1']//*[@class='user-login__text ng-binding']"
skip_button_promotion = "//*[contains(text(), 'Пропустити')]"
skip_button_promotion = "//*[contains(text(), 'Skip')]"
text_multilogin_popup = "//*[@class='l__login-title l__login-title-phone l__login-title-sms ng-scope']"
text_error_wrong_sms = "(//*[@ng-show='!!error'])[1]"
text_error_empty_mobile_number = "//*[@class='l__input-phone__info text-center']"
button_login_by_sms = "//button[@ng-disabled='activeauth.$invalid || blocked || !code']"
button_get_sms_valid = "//button[@class='l__login-phone-btn get-sms l__login-phone-btn-valid']"
button_get_sms_invalid = "//button[@class='l__login-phone-btn get-sms l__login-phone-btn-invalid']"
skip_button_promotion2 = "//*[contains(text(), 'Пропустити')]"
cabinet_button = "//*[@class='tabs-login']"


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        driver.get("https://sweet.tv/")

    def enter_cabinet_page(self):
        self.driver.find_element(By.XPATH, cabinet_button).click()

    def is_button_disable(self):

        button = self.driver.find_element(By.XPATH, button_login_by_sms)
        if button.is_enabled():
            return True
        else:
            return False

    def get_text_error_empty_mobile_number(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, text_error_empty_mobile_number))).text

    def get_text_error_wrong_sms(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, text_error_wrong_sms))).text

    def get_text_from_multilogin_popup(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, sms_input)))
        return self.driver.find_element(By.XPATH, text_multilogin_popup).text

    def get_user_datas(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, user_data))).text

    def select_promotion(self):
        run_time = 5
        start_time = time.time()
        while time.time() - start_time < run_time:
            try:
                self.driver.find_element(By.XPATH, skip_button_promotion).click()
            except (NoSuchElementException, ElementNotInteractableException):
                pass
                try:
                    self.driver.find_element(By.XPATH, skip_button_promotion2).click()
                except (NoSuchElementException, ElementNotInteractableException):
                    pass

    def confirm_sing_in(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, google_form_confirm_sign_in))).click()
        except:
            pass

    def get_text(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, text_sign_in_or_sign_up))).text

    def click_on_sign_in(self):
        self.driver.find_element(By.XPATH, sign_in_button).click()

    def click_on_login_phone(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, login_phone))).click()

    def click_on_get_sms_button_valid(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, button_get_sms_valid)))
        self.driver.find_element(By.XPATH, button_get_sms_valid).click()

    def click_on_get_sms_button_invalid(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_get_sms_invalid))).click()
        self.driver.find_element(By.XPATH, button_get_sms_invalid).click()

    def click_on_button_next_in_google_form_login(self):
        self.driver.find_element(By.XPATH, google_form_button_next).click()

    def click_on_button_next_in_google_form_password(self):
        self.driver.find_element(By.XPATH, google_form_button_next_password).click()

    def click_on_google_logo(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, google_button))).click()

    def fill_in_mail(self, mail):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, mail_input))).click()
        self.driver.find_element(By.XPATH, mail_input).send_keys(mail)

    def fill_in_password(self, password):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, password_input))).click()
        self.driver.find_element(By.XPATH, password_input).send_keys(password)

    def fill_in_mobile_field(self, mobile):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, mobile_input))).click()
        self.driver.find_element(By.XPATH, mobile_input).send_keys(mobile)

    def fill_in_sms_field(self, sms):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, sms_input))).click()
        self.driver.find_element(By.XPATH, sms_input).send_keys(sms)
