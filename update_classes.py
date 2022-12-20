import os
import re
from main import setup
from email_alerts import send_email

def check_openings(driver, course, section, crn, remaining_seats):
    ''' updates seat information for given class, sends email if the class opens up or the class closes, returns the updated amount of seats left '''
    driver.execute_script("document.getElementById('crit-keyword').value='" + crn + "';")
    driver.execute_script("document.getElementById('search-button').click();")
    driver.execute_script("await new Promise(r => setTimeout(r, 2000));")
    driver.execute_script("document.querySelectorAll('[data-key]')[1].click();")
    driver.execute_script("await new Promise(r => setTimeout(r, 2000));")
    driver.execute_script("console.log(document.getElementsByClassName(['course-section-all-sections-seats'])[" + str(int(section)-1) + "].textContent);")
    data_text = driver.get_log('browser')[0]['message']
    updated_seats_left = int(data_text[26:len(data_text) - 1])
    if (remaining_seats <= 0 and updated_seats_left > 0) or (remaining_seats > 0 and updated_seats_left <= 0):
        send_email(course, section, updated_seats_left)
    return updated_seats_left

driver = setup()
if os.path.exists('classes.txt'):
    openings = []
    with open('classes.txt', 'r') as fh:
        lines = fh.readlines()
        for line in lines: 
            data = re.split(',|: ', line)
            updated_seats_left = check_openings(driver, data[0]+': '+data[1], data[3], data[5], int(data[7]))
            openings.append(f'{data[0]}: {data[1]}, Section: {data[3]}, CRN: {data[5]}, Seats: {updated_seats_left}\n')
    openings[-1] = openings[-1].rstrip()
    with open('classes.txt', 'w') as fh:
        fh.writelines(openings)
else:
    print('Error: you have not added any courses yet')
driver.quit()