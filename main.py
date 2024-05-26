from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

google_form = "https://docs.google.com/forms/d/e/1FAIpQLSfwiXTS_i2fpUP9dk87q3y8FBq1NZ1IUbpaRin7nsfHmqMUwQ/viewform?usp=sf_link"

# ------selenium ------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.audible.com/search?keywords=book&node=18573211011")

# -----selenium Show Dropdown Item Per Page----
sleep(5)
driver.find_element(By.XPATH, '//*[@id="pagination-a11y-skiplink-target"]/div/div[1]/span[2]/select/option[4]').click()

# -----BS4 find all names----
images_link = driver.find_elements(By.CLASS_NAME, "bc-image-inset-border")
images_list = []
for link in images_link:
    link = link.get_attribute('src')
    images_list.append(link)

# -----selenium find all names----
names = driver.find_elements(By.CLASS_NAME, "bc-pub-break-word")
name_list = []
for name in names:
    name_list.append(name.text)

# ----selenium Find All subtitle-----
subtitles = driver.find_elements(By.CLASS_NAME, "subtitle")
subtitle_list = []
for subtitle in subtitles:
    subtitle_list.append(subtitle.text)

# ----- Find All Authors----
authors = driver.find_elements(By.CLASS_NAME, "authorLabel")
author_list = []
for author in authors:
    author = author.text
    author_list.append(author[4:])

# -----------Find all Narrated By-------
narrated_by = driver.find_elements(By.CLASS_NAME, "narratorLabel")
narrated_list = []
for narrated in narrated_by:
    narrated = narrated.text
    narrated_list.append(narrated[13:])

# -------Find All runtimeLabel-------
run_time_duration = driver.find_elements(By.CLASS_NAME, "runtimeLabel")
run_duration_list = []
for duration in run_time_duration:
    duration = duration.text
    run_duration_list.append(duration[8:])

# -------Find All Release Date-------
release_dates = driver.find_elements(By.CLASS_NAME, "releaseDateLabel")
release_dates_list = []
for date in release_dates:
    date = date.text
    release_dates_list.append(date[14:])

# -------Find All languageLabel-------
languages = driver.find_elements(By.CLASS_NAME, "languageLabel")
languages_list = []
for language in languages:
    language = language.text
    languages_list.append(language[10:])

# -------Find All ratingsLabel-------
ratings = driver.find_elements(By.CLASS_NAME, "ratingsLabel")
star_rating_list = []
number_ratings_list = []
for rating in ratings:
    rating = rating.text
    rating = rating.rstrip().split('\n')

    if len(rating) == 2:
        star_rating_list.append(rating[0][:-6])
        number_ratings_list.append(rating[1][:-8])

    else:
        star_rating_list.append(rating[0])
        number_ratings_list.append('Not rated yet')

driver.close()

# ------ selenium data save to google form-----
drivers = webdriver.Chrome(options=chrome_options)
drivers.get(google_form)

for images, name, subtitle, author, narrated, duration, release_dates, languages, star_rating, number_ratings in zip(
        images_list, name_list, subtitle_list, author_list, narrated_list, run_duration_list, release_dates_list,
        languages_list, star_rating_list, number_ratings_list):

    sleep(2)
    drivers.current_url

    drivers.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(images)
    drivers.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(name)
    drivers.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(subtitle)
    drivers.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(author)
    drivers.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(narrated)
    drivers.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(duration)
    drivers.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(release_dates)
    drivers.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(languages)
    drivers.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(star_rating)
    drivers.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(number_ratings)
    drivers.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

    sleep(2)
    drivers.current_url
    drivers.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()


drivers.quit()

