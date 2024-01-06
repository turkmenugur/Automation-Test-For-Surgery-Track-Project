from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from pathlib import Path
from datetime import date
from datetime import datetime

import pytest

fake = Faker()

class Test_Otomation: 
    
    #setup -> func ->  teardown

    #her testten önce çağırılır
    @classmethod
    def setup_method(cls):
        #chrome_options = Options()
        #chrome_options.add_argument("--headless")
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://localhost:7042/")

        #günün tarihini al bu tarih ile bir klasör var mı kontrol et yoksa oluştur
        cls.folderPath = str(date.today()) # 27.12.2023
        Path(cls.folderPath).mkdir(exist_ok=True)

    #her testten sonra çağırılır.
    @classmethod
    def teardown_method(cls):
        cls.driver.quit()

    #giriş sayfası
    @pytest.mark.parametrize("username,password",[("1","1"),("kullaniciadim","sifrem")] )
    def test_invalid_login(self, username, password):
        #Kullanıcı adı veya parola yanlış girildi!
        self.setup_method()
        username_input = self.driver.find_element(By.ID, "form2Example17")
        username_input.send_keys(username)
        sleep(0.5)
        password_input = self.driver.find_element(By.ID,"form2Example27")
        password_input.send_keys(password)
        sleep(0.3)
        self.driver.save_screenshot(f"{self.folderPath}/valid_login.png")
        login_button = self.driver.find_element(By.CLASS_NAME, "btn")
        login_button.click()
        errorMessage = self.driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/div/div[2]/div/form/div[5]")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert errorMessage.text == "Kullanıcı adı veya parola yanlış girildi!"
        #print(errorMessage)

    #giriş sayfası
    @pytest.mark.dependency(name="valid_login", scope="class")
    def test_valid_login(self):
        self.setup_method()
        username_input = self.driver.find_element(By.ID, "form2Example17")
        username_input.send_keys("ismet")
        sleep(0.5)
        password_input = self.driver.find_element(By.ID,"form2Example27")
        password_input.send_keys("1")
        sleep(0.3)
        self.driver.save_screenshot(f"{self.folderPath}/valid_login.png")
        login_button = self.driver.find_element(By.CLASS_NAME, "btn")
        login_button.click()
    
    def test_main_page(self):
        self.test_valid_login()
        sleep(0.5)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(1)
        # page_link_2 = self.driver.find_element(By.XPATH, "//*[@id='main']/div/main/div/section/div/div[2]/div/div[3]/nav/ul/li[2]/a")
        # sleep(1)
        # self.driver.execute_script("arguments[0].click();", page_link_2)
        # sleep(1)
        # page_link_3 = self.driver.find_element(By.XPATH,"//*[@id='main']/div/main/div/section/div/div[2]/div/div[3]/nav/ul/li[3]/a")
        # sleep(1)
        # self.driver.execute_script("arguments[0].click();", page_link_3)
        # sleep(1)

    #hasta kayıt
    @pytest.mark.dependency(name="valid_login_required", depends=["valid_login"], scope="class")
    def test_patient_registration(self):
        self.test_valid_login()
        sleep(1)
        patient_register_menu = self.driver.find_element(By.XPATH,"//*[@id='sidebar']/div/div[2]/ul/li[5]/a/span")
        patient_register_menu.click()
        sleep(0.5)
        first_name_input = self.driver.find_element(By.ID, "Ad")
        first_name_input.send_keys(f"{fake.first_name()}")
        sleep(0.5)
        last_name_input = self.driver.find_element(By.ID, "Soyad")
        last_name_input.send_keys(f"{fake.last_name()}")
        sleep(0.5)
        gender_input = self.driver.find_element(By.ID,"Cinsiyet")
        gender_input.send_keys("E")
        sleep(0.5)
        birth_date_input = self.driver.find_element(By.ID,"DogumTarihi")
        birth_date_input.send_keys(f"{fake.date_of_birth()}")
        sleep(0.5)
        phone_input = self.driver.find_element(By.ID,"Telefon")
        phone_input.send_keys("05510123456")
        sleep(0.25)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(0.25)
        email_input = self.driver.find_element(By.ID,"Eposta")
        email_input.send_keys(f"{fake.email()}")
        sleep(0.5)
        adress_input = self.driver.find_element(By.ID,"Adres")
        adress_input.send_keys(f"{fake.address()}")
        sleep(0.5)
        registration_date_input = self.driver.find_element(By.NAME,"KayitTarihi")
        registration_date_input.send_keys("2023-12-28")
        sleep(0.5)
        self.driver.save_screenshot(f"{self.folderPath}/registration_page_of_patient_with_fake_datas.png")
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(1)
        save_btn = self.driver.find_element(By.CLASS_NAME, "btn")
        save_btn.click()

    #hasta listesi
    @pytest.mark.dependency(name="valid_login_required", depends=["valid_login"], scope="class")
    def test_patient_list(self):
        self.test_valid_login()
        patient_list_menu = self.driver.find_element(By.XPATH,"//*[@id='sidebar']/div/div[2]/ul/li[6]/a/span")
        patient_list_menu.click()
        sleep(1.5)
       #self.driver.execute_script("window.scrollTo(0,500)")
        
        #profile git
        go_to_profile_link = self.driver.find_element(By.XPATH, "//*[@id='yourTableId']/tbody/tr[4]/td[8]/a[1]")
        sleep(1)
        self.driver.execute_script("arguments[0].click();", go_to_profile_link)
        sleep(1)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(1)
        self.driver.back()
        sleep(1)

        #ameliyat planı
        go_to_surgery_plan_link = self.driver.find_element(By.XPATH, "//*[@id='yourTableId']/tbody/tr[4]/td[8]/a[2]")
        sleep(1)
        self.driver.execute_script("arguments[0].click();", go_to_surgery_plan_link)
        select_patient_1 = self.driver.find_element(By.ID,"Ameliyat_HastaId")
        select_patient_1.click()
        sleep(0.5)
        select_patient_2 = self.driver.find_element(By.XPATH,"//*[@id='Ameliyat_HastaId']/option[1]")
        select_patient_2.click()
        select_doctor_1 = self.driver.find_element(By.ID,"Ameliyat_DoktorId")
        select_doctor_1.click()
        sleep(0.5)
        select_doctor_2 = self.driver.find_element(By.XPATH,"//*[@id='Ameliyat_DoktorId']/option[1]")
        select_doctor_2.click()
        sleep(0.5)
        surgery_input = self.driver.find_element(By.ID,"Ameliyat_AmeliyatAdi")
        surgery_input.click()
        sleep(0.5)
        surgery_input_2 = self.driver.find_element(By.XPATH,"//*[@id='Ameliyat_AmeliyatAdi']/option[1]")
        surgery_input_2.click()
        sleep(0.5)
        surgery_date_input = self.driver.find_element(By.ID,"Ameliyat_AmeliyatTarihi")
        surgery_date_input.send_keys("2023-12-30")
        sleep(0.5)
        surgery_save_btn = self.driver.find_element(By.CLASS_NAME,"btn")
        surgery_save_btn.click()
        sleep(0.5)
        self.driver.back()
        self.driver.back()
        sleep(1)

        #edit  
        go_to_edit_link = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/main/div/div[2]/div/table/tbody/tr[2]/td[8]/a[3]")
        sleep(1)
        self.driver.execute_script("arguments[0].click();", go_to_edit_link)
        sleep(0.25)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(0.25)
        adres_textbox = self.driver.find_element(By.ID, "Adres")
        adres_textbox.send_keys(f"{fake.address()}")
        sleep(0.5)
        save_btn = self.driver.find_element(By.CLASS_NAME, "btn")
        save_btn.click()
        sleep(0.25)
        self.driver.back()

        #remove
        click_to_remove_link = self.driver.find_element(By.XPATH, "//*[@id='yourTableId']/tbody/tr[4]/td[8]/a[4]")
        sleep(1)
        self.driver.execute_script("arguments[0].click();", click_to_remove_link)

    #ameliyat plan
    @pytest.mark.dependency(name="valid_login_required", depends=["valid_login"], scope="class")
    def test_surgery_plan(self):
        self.test_valid_login()
        surgery_plan_menu = self.driver.find_element(By.XPATH,"//*[@id='sidebar']/div/div[2]/ul/li[3]/a/span")
        surgery_plan_menu.click()
        sleep(0.5)
        select_patient_1 = self.driver.find_element(By.ID,"Ameliyat_HastaId")
        select_patient_1.click()
        sleep(0.5)
        select_patient_2 = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/main/div[2]/div/form/div[1]/select/option[4]")
        select_patient_2.click()
        sleep(0.5)
        select_doctor_1 = self.driver.find_element(By.ID,"Ameliyat_DoktorId")
        select_doctor_1.click()
        sleep(0.5)
        select_doctor_2 = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/main/div[2]/div/form/div[2]/select/option")
        select_doctor_2.click()
        sleep(0.5)
        surgery_input = self.driver.find_element(By.ID,"Ameliyat_AmeliyatAdi")
        surgery_input.send_keys("Apandist")
        sleep(0.5)
        surgery_date_input = self.driver.find_element(By.ID,"Ameliyat_AmeliyatTarihi")
        surgery_date_input.send_keys("2023-12-24")
        sleep(0.5)
        surgery_save_btn = self.driver.find_element(By.CLASS_NAME,"btn")
        surgery_save_btn.click()

    #ameliyat plan listesi
    @pytest.mark.dependency(name="valid_login_required", depends=["valid_login"], scope="class")
    def test_surgery_plan_list(self):
        self.test_valid_login()
        surgery_plan_list_menu = self.driver.find_element(By.XPATH, "//*[@id='sidebar']/div/div[2]/ul/li[4]/a/span")
        surgery_plan_list_menu.click()
        sleep(0.5)

        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(1)
        self.driver.execute_script("window.scrollTo(0,0)")
        
        #Detay
        go_to_surgery_details_link = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/main/div/div[2]/table/tbody/tr[1]/td[5]/a[1]")
        sleep(1)
        self.driver.execute_script("arguments[0].click();", go_to_surgery_details_link)
        sleep(1)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(1)
        self.driver.back()
        sleep(1)

        #edit  
        go_to_edit_link = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/main/div/div[2]/table/tbody/tr[1]/td[5]/a[2]")
        sleep(1)
        self.driver.execute_script("arguments[0].click();", go_to_edit_link)
        sleep(0.25)
        adres_textbox = self.driver.find_element(By.ID, "AmeliyatTarihi")
        adres_textbox.send_keys("2023-01-05")
        sleep(0.5)
        save_btn = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/main/div[2]/div/form/div[5]/button")
        save_btn.click()

        # #remove
        # click_to_remove_link = self.driver.find_element(By.XPATH, "//*[@id='yourTableId']/tbody/tr[8]/td[5]/a[3]")
        # sleep(1)
        # self.driver.execute_script("arguments[0].click();", click_to_remove_link)


    # #doktor kayıt menü
    # @pytest.mark.dependency(name="valid_login_required", depends=["valid_login"], scope="class")
    # def test_doctor_registration_menu(self):
    #     self.test_valid_login()
    #     doctor_registration_menu = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/ul/li[7]/a")
    #     doctor_registration_menu.click()

    #doktor kayıt
    #@pytest.mark.dependency(name="valid_login_required", depends=["valid_login"], scope="class")
    def test_doctor_registration(self):
        self.test_valid_login()

        deoctor_registration_menu = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/ul/li[7]/a/span")
        deoctor_registration_menu.click()
        sleep(0.5)

        doctor_name_input = self.driver.find_element(By.NAME,"Ad")
        doctor_name_input.send_keys(f"{fake.first_name()}")
        sleep(0.5)
        doctor_lastname_input = self.driver.find_element(By.ID,"Soyad")
        doctor_lastname_input.send_keys(f"{fake.last_name()}")
        sleep(0.5)
        gender_input = self.driver.find_element(By.ID,"Cinsiyet")
        gender_input.send_keys("E")
        sleep(0.5)
        doctor_phone_input = self.driver.find_element(By.ID,"Telefon")
        doctor_phone_input.send_keys(f"{fake.phone_number()}")
        sleep(0.5)
        doctor_email_input =self.driver.find_element(By.ID,"Eposta")
        doctor_email_input.send_keys(f"{fake.email()}")
        sleep(0.5)
        current_datetime = datetime.now()

        # Belirli bir formata dönüştür (YYYY-MM-DDTHH:mm)
        formatted_datetime = current_datetime.strftime('%Y-%m-%dT%H:%M')

        # WebElement'i bul ve değeri gönder
        date_input = self.driver.find_element(By.ID, "KayitTarihi")
        date_input.send_keys(formatted_datetime)

        # registration_date_input = self.driver.find_element(By.ID,"KayitTarihi")
        # self.driver.execute_script("arguments[0].value = '1980-06-30T00:00:00Z';", registration_date_input)

        save_btn = self.driver.find_element(By.CLASS_NAME,"btn")
        save_btn.click()
        

    #doktor listesi
    @pytest.mark.dependency(name="valid_login_required", depends=["valid_login"], scope="class")
    def test_doctor_list(self):
        self.test_valid_login()
        doctor_list_menu = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/ul/li[8]/a")
        doctor_list_menu.click()

        #profile git
        go_to_profile_link = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/main/div/div[2]/table/tbody/tr[1]/td[8]/a[1]")
        sleep(1)
        self.driver.execute_script("arguments[0].click();", go_to_profile_link)
        sleep(1)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(1)
        self.driver.back()
        sleep(1)

        #edit  
        go_to_edit_link = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/main/div/div[2]/table/tbody/tr[1]/td[8]/a[2]")
        sleep(1)
        self.driver.execute_script("arguments[0].click();", go_to_edit_link)
        #adres_textbox = self.driver.find_element(By.NAME, "Eposta")
        eposta_textbox = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "Eposta")))
        eposta_textbox.send_keys(f"{fake.email()}")
        sleep(0.5)
        save_btn = self.driver.find_element(By.CLASS_NAME, "btn")
        save_btn.click()
        sleep(0.25)
        self.driver.back()

        # #remove
        # # click_to_remove_link = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/main/div/div[2]/table/tbody/tr[1]/td[8]/a[3]")
        # click_to_remove_link = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div/main/div/div[2]/table/tbody/tr[2]/td[8]/a[3]")))
        # self.driver.execute_script("arguments[0].click();", click_to_remove_link)

    #AMELİYATLAR
    
    #anal atrezi ekle
    def test_antireflu(self):
        self.test_valid_login()
        ameliyatlar_menu = self.driver.find_element(By.XPATH,"//*[@id='sidebar']/div/div[2]/ul/li[9]/a")
        ameliyatlar_menu.click()
        anal_atrezi_add_menu = self.driver.find_element(By.XPATH,"//*[@id='sidebar']/div/div[2]/ul/li[9]/ul/li[1]/a")
        anal_atrezi_add_menu.click()

        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(1)
        self.driver.execute_script("window.scrollTo(0,0)")
        sleep(0.5)

        new_record = self.driver.find_element(By.XPATH,"//*[@id='main']/div/main/div/div[2]/a")
        new_record.click()
        
        choose_sergery = self.driver.find_element(By.ID,"AmeliyatId")
        choose_sergery.click()
        sleep(0.25)
        choose_sergery_option = self.driver.find_element(By.XPATH,"//*[@id='AmeliyatId']/option[2]")
        choose_sergery_option.click()

        surgery_type = self.driver.find_element(By.ID,"AmeliyatTipi")
        surgery_type.send_keys("antiR")

        gaa_pvi = self.driver.find_element(By.ID,"GAA_PVI")
        gaa_pvi.send_keys("evet")
        ozefagus = self.driver.find_element(By.ID,"OzefagusSerbest")
        ozefagus.send_keys("evet")
        fundoplikasyon = self.driver.find_element(By.ID,"Fundoplikasyon")
        fundoplikasyon.send_keys("evet")
        gastrostomiAcilmasi = self.driver.find_element(By.ID,"GastrostomiAcilmasi")
        gastrostomiAcilmasi.send_keys("evet")
        kanama_kontrol = self.driver.find_element(By.ID,"KanamaKontrolu")
        kanama_kontrol.send_keys("evet")
        komplikasyonDurumu = self.driver.find_element(By.ID,"KomplikasyonDurumu")
        komplikasyonDurumu.send_keys("evet")
        

        save_button = self.driver.find_element(By.XPATH,"//*[@id='multiple-column-form']/div/div/div/div[2]/div/form/div/div[9]/button[1]")
        #save_btn.click()
        self.driver.execute_script("arguments[0].click();", save_button)

    #anal atrezi listele
    # def test_antireflu(self):
    #     #Ameliyat detayları
    #     go_to_surgery_details_link = self.driver.find_element(By.XPATH, "//*[@id='yourTableId']/tbody/tr/td[14]/a[1]")
    #     sleep(1)
    #     self.driver.execute_script("arguments[0].click();", go_to_surgery_details_link)
    #     sleep(1)
    #     self.driver.execute_script("window.scrollTo(0,500)")
    #     sleep(1)
    #     self.driver.back()
    #     sleep(1)

    #     #edit  
    #     go_to_edit_link = self.driver.find_element(By.XPATH, "//*[@id='yourTableId']/tbody/tr/td[14]/a[2]")
    #     sleep(1)
    #     self.driver.execute_script("arguments[0].click();", go_to_edit_link)
    #     sleep(0.25)
    #     self.driver.execute_script("window.scrollTo(0,500)")
    #     sleep(0.25)
    #     insizyon_yapilmasi = self.driver.find_element(By.ID,"AnalAtreziss_InsizyonYapilmasi")
    #     insizyon_yapilmasi.send_keys("hayır")
    #     sleep(0.5)
    #     save_btn = self.driver.find_element(By.CLASS_NAME, "btn")
    #     save_btn.click()
    #     sleep(0.25)
    #     self.driver.back()

    #     #remove
    #     click_to_remove_link = self.driver.find_element(By.XPATH, "//*[@id='yourTableId']/tbody/tr/td[14]/a[3]")
    #     sleep(1)
    #     self.driver.execute_script("arguments[0].click();", click_to_remove_link)

# testOtomClass = Test_Otom()
# testOtomClass.test_invalid_login
# testOtomClass.test_valid_login
# testOtomClass.test_patient_registration
# testOtomClass.test_surg_plan
# testOtomClass.test_surg_plan_list
# testOtomClass.test_patient_list
# testOtomClass.test_doctor_registration_menu
# testOtomClass.test_doc_reg
# testOtomClass.test_doc_list