from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from faker import Faker
from datetime import datetime
import pytest

fake = Faker()

class Test_Otomation_Full:

    def test_full(self):

        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get("https://localhost:7042/")

        #Başarısız giriş denemesi
        username_input = self.driver.find_element(By.ID, "form2Example17")
        username_input.send_keys(1)
        sleep(1)
        password_input = self.driver.find_element(By.ID,"form2Example27")
        password_input.send_keys(1)
        sleep(1)
        login_button = self.driver.find_element(By.CLASS_NAME, "btn")
        login_button.click()
        errorMessage = self.driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/div/div[2]/div/form/div[5]")
        assert errorMessage.text == "Kullanıcı adı veya parola yanlış girildi!"

        sleep(1)

        #Başarılı giriş denemesi
        username_input = self.driver.find_element(By.ID, "form2Example17")
        username_input.send_keys("ismet")
        sleep(1)
        password_input = self.driver.find_element(By.ID,"form2Example27")
        password_input.send_keys("1")
        sleep(0.5)
        login_button = self.driver.find_element(By.CLASS_NAME, "btn")
        login_button.click()

        sleep(1)
    
        #ana sayfa
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(1)
        self.driver.execute_script("window.scrollTo(0,0)")
        sleep(1)

        #hasta kayıt
        sleep(1)
        patient_register_menu = self.driver.find_element(By.XPATH,"//*[@id='sidebar']/div/div[2]/ul/li[5]/a/span")
        patient_register_menu.click()
        sleep(1)
        first_name_input = self.driver.find_element(By.ID, "Ad")
        first_name_input.send_keys(f"{fake.first_name()}")
        sleep(1)
        last_name_input = self.driver.find_element(By.ID, "Soyad")
        last_name_input.send_keys(f"{fake.last_name()}")
        sleep(1)
        gender_input = self.driver.find_element(By.ID,"Cinsiyet")
        gender_input.send_keys("E")
        sleep(1)
        birth_date_input = self.driver.find_element(By.ID,"DogumTarihi")
        birth_date_input.send_keys(f"{fake.date_of_birth()}")
        sleep(1)
        phone_input = self.driver.find_element(By.ID,"Telefon")
        phone_input.send_keys("05510123456")
        sleep(1)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(1)
        email_input = self.driver.find_element(By.ID,"Eposta")
        email_input.send_keys(f"{fake.email()}")
        sleep(1)
        adress_input = self.driver.find_element(By.ID,"Adres")
        adress_input.send_keys(f"{fake.address()}")
        sleep(1)
        registration_date_input = self.driver.find_element(By.NAME,"KayitTarihi")
        registration_date_input.send_keys("2023-12-28")
        sleep(1)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(1)
        save_btn = self.driver.find_element(By.CLASS_NAME, "btn")
        save_btn.click()
        
        sleep(1)
        self.driver.back()
        self.driver.back()

        #hasta listesi
    
        patient_list_menu = self.driver.find_element(By.XPATH,"//*[@id='sidebar']/div/div[2]/ul/li[6]/a/span")
        patient_list_menu.click()
        sleep(1.5)
        self.driver.execute_script("window.scrollTo(0,2000)")

        page_link_2 = self.driver.find_element(By.XPATH, "//*[@id='yourTableId_paginate']/span/a[2]")
        sleep(1)
        self.driver.execute_script("arguments[0].click();", page_link_2)
        sleep(1)
        page_link_3 = self.driver.find_element(By.XPATH,"//*[@id='yourTableId_paginate']/span/a[3]")
        sleep(1)
        self.driver.execute_script("arguments[0].click();", page_link_3)
        sleep(1)
        page_link_4 = self.driver.find_element(By.XPATH,"//*[@id='yourTableId_paginate']/span/a[4]")
        sleep(1)
        self.driver.execute_script("arguments[0].click();", page_link_4)
        sleep(1)
        page_link_5 = self.driver.find_element(By.XPATH,"//*[@id='yourTableId_paginate']/span/a[5]")
        sleep(1)
        self.driver.execute_script("arguments[0].click();", page_link_5)
        sleep(1)
        page_link_1 = self.driver.find_element(By.XPATH,"//*[@id='yourTableId_paginate']/span/a[1]")
        sleep(1)
        self.driver.execute_script("arguments[0].click();", page_link_1)

        self.driver.execute_script("window.scrollTo(0,0)")
        sleep(1)

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
        sleep(1)
        select_patient_2 = self.driver.find_element(By.XPATH,"//*[@id='Ameliyat_HastaId']/option[1]")
        select_patient_2.click()
        select_doctor_1 = self.driver.find_element(By.ID,"Ameliyat_DoktorId")
        select_doctor_1.click()
        sleep(1)
        select_doctor_2 = self.driver.find_element(By.XPATH,"//*[@id='Ameliyat_DoktorId']/option[1]")
        select_doctor_2.click()
        sleep(1)
        surgery_input = self.driver.find_element(By.ID,"Ameliyat_AmeliyatAdi")
        surgery_input.click()
        sleep(1)
        surgery_input_2 = self.driver.find_element(By.XPATH,"//*[@id='Ameliyat_AmeliyatAdi']/option[1]")
        surgery_input_2.click()
        sleep(1)
        surgery_date_input = self.driver.find_element(By.ID,"Ameliyat_AmeliyatTarihi")
        surgery_date_input.send_keys("2023-12-30")
        sleep(1)
        surgery_save_btn = self.driver.find_element(By.CLASS_NAME,"btn")
        surgery_save_btn.click()
        sleep(1)
        self.driver.back()
        self.driver.back()
        sleep(1)

        #edit  
        go_to_edit_link = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/main/div/div[2]/div/table/tbody/tr[2]/td[8]/a[3]")
        sleep(1)
        self.driver.execute_script("arguments[0].click();", go_to_edit_link)
        sleep(1)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(1)
        adres_textbox = self.driver.find_element(By.ID, "Adres")
        adres_textbox.send_keys(f"{fake.address()}")
        sleep(1)
        save_btn = self.driver.find_element(By.CLASS_NAME, "btn")
        save_btn.click()
        sleep(1)
        self.driver.back()

        #ameliyat plan
        surgery_plan_menu = self.driver.find_element(By.XPATH,"//*[@id='sidebar']/div/div[2]/ul/li[3]/a/span")
        surgery_plan_menu.click()
        sleep(1)
        select_patient_1 = self.driver.find_element(By.ID,"Ameliyat_HastaId")
        select_patient_1.click()
        sleep(1)
        select_patient_2 = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/main/div[2]/div/form/div[1]/select/option[4]")
        select_patient_2.click()
        sleep(1)
        select_doctor_1 = self.driver.find_element(By.ID,"Ameliyat_DoktorId")
        select_doctor_1.click()
        sleep(1)
        select_doctor_2 = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/main/div[2]/div/form/div[2]/select/option")
        select_doctor_2.click()
        sleep(1)
        surgery_input = self.driver.find_element(By.ID,"Ameliyat_AmeliyatAdi")
        surgery_input.send_keys("Apandist")
        sleep(1)
        surgery_date_input = self.driver.find_element(By.ID,"Ameliyat_AmeliyatTarihi")
        surgery_date_input.send_keys("2023-12-24")
        sleep(1)
        surgery_save_btn = self.driver.find_element(By.CLASS_NAME,"btn")
        surgery_save_btn.click()

        #ameliyat plan listesi
        surgery_plan_list_menu = self.driver.find_element(By.XPATH, "//*[@id='sidebar']/div/div[2]/ul/li[4]/a/span")
        surgery_plan_list_menu.click()
        sleep(1)

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

        #doktor kayıt

        deoctor_registration_menu = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/ul/li[7]/a/span")
        deoctor_registration_menu.click()
        sleep(1)

        doctor_name_input = self.driver.find_element(By.NAME,"Ad")
        doctor_name_input.send_keys(f"{fake.first_name()}")
        sleep(1)
        doctor_lastname_input = self.driver.find_element(By.ID,"Soyad")
        doctor_lastname_input.send_keys(f"{fake.last_name()}")
        sleep(1)
        gender_input = self.driver.find_element(By.ID,"Cinsiyet")
        gender_input.send_keys("E")
        sleep(1)
        doctor_phone_input = self.driver.find_element(By.ID,"Telefon")
        doctor_phone_input.send_keys(f"{fake.phone_number()}")
        sleep(1)
        doctor_email_input =self.driver.find_element(By.ID,"Eposta")
        doctor_email_input.send_keys(f"{fake.email()}")
        sleep(1)
        current_datetime = datetime.now()

        # Belirli bir formata dönüştür (YYYY-MM-DDTHH:mm)
        formatted_datetime = current_datetime.strftime('%Y-%m-%dT%H:%M')

        # WebElement'i bul ve değeri gönder
        date_input = self.driver.find_element(By.ID, "KayitTarihi")
        date_input.send_keys(formatted_datetime)

        save_btn = self.driver.find_element(By.CLASS_NAME,"btn")
        save_btn.click()
        

        #doktor listesi
        doctor_list_menu = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/ul/li[8]/a")
        doctor_list_menu.click()

        sleep(1)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(1)
        self.driver.execute_script("window.scrollTo(0,0)")

        #profile git
        go_to_profile_link = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/main/div/div[2]/table/tbody/tr[1]/td[8]/a[1]")
        sleep(1)
        self.driver.execute_script("arguments[0].click();", go_to_profile_link)
        sleep(1)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(1)
        self.driver.back()
        sleep(1)

        #AMELİYATLAR
    
        #anti reflu
        ameliyatlar_menu = self.driver.find_element(By.XPATH,"//*[@id='sidebar']/div/div[2]/ul/li[9]/a")
        ameliyatlar_menu.click()
        anal_atrezi_add_menu = self.driver.find_element(By.XPATH,"//*[@id='sidebar']/div/div[2]/ul/li[9]/ul/li[1]/a")
        anal_atrezi_add_menu.click()

        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(1)
        self.driver.execute_script("window.scrollTo(0,0)")
        sleep(1)

        new_record = self.driver.find_element(By.XPATH,"//*[@id='main']/div/main/div/div[2]/a")
        new_record.click()
        sleep(1)
        
        choose_sergery = self.driver.find_element(By.ID,"AmeliyatId")
        choose_sergery.click()
        sleep(1)
        choose_sergery_option = self.driver.find_element(By.XPATH,"//*[@id='AmeliyatId']/option[2]")
        choose_sergery_option.click()
        sleep(1)

        surgery_type = self.driver.find_element(By.ID,"AmeliyatTipi")
        surgery_type.send_keys("antiR")
        sleep(1)

        gaa_pvi = self.driver.find_element(By.ID,"GAA_PVI")
        gaa_pvi.send_keys("evet")
        sleep(1)
        ozefagus = self.driver.find_element(By.ID,"OzefagusSerbest")
        ozefagus.send_keys("evet")
        sleep(1)
        fundoplikasyon = self.driver.find_element(By.ID,"Fundoplikasyon")
        fundoplikasyon.send_keys("evet")
        sleep(1)
        gastrostomiAcilmasi = self.driver.find_element(By.ID,"GastrostomiAcilmasi")
        gastrostomiAcilmasi.send_keys("evet")
        sleep(1)
        kanama_kontrol = self.driver.find_element(By.ID,"KanamaKontrolu")
        kanama_kontrol.send_keys("evet")
        sleep(1)
        komplikasyonDurumu = self.driver.find_element(By.ID,"KomplikasyonDurumu")
        komplikasyonDurumu.send_keys("evet")
        sleep(1)

        save_button = self.driver.find_element(By.XPATH,"//*[@id='multiple-column-form']/div/div/div/div[2]/div/form/div/div[9]/button[1]")
        #save_btn.click()
        self.driver.execute_script("arguments[0].click();", save_button)
