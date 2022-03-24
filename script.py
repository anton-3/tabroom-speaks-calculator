from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep

def get_link():
  while True:
    link = input('Enter a tabroom link of the tournament results page for any prelim round: ')
    if link.startswith('https://www.tabroom.com/'):
      break
    print('Invalid link')
  return link

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

link = get_link()

driver.get(link)
elements = driver.find_elements(by=By.CSS_SELECTOR, value='.marno.marvert') # this selects all the <a> elements that have links to each team's results page

team_links = []

for element in elements:
  team_links.append(element.get_attribute('href'))

# if there's an odd number of teams in the tournament there's an empty link at the end, get rid of that
if team_links[-1].endswith('='):
  team_links.pop(-1)

tournament_name = driver.find_element(by=By.CSS_SELECTOR, value='h2').text

print(f'\nGot {len(team_links)} teams at tournament {tournament_name}')

teams_info = {}

for team_link in team_links:
  driver.get(team_link)
  team_code = driver.find_element(by=By.CSS_SELECTOR, value='h2').text
  
  teams_info[team_code] = {}

driver.close()
