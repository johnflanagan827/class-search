#!/usr/bin/env python3

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def setup() -> any:
    """ performs basic setup for selenium to browse https://classsearch.nd.edu, returns driver """
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.set_capability("goog:loggingPrefs", {'browser': 'ALL'})
    driver = webdriver.Chrome(options=options)
    driver.get('https://classsearch.nd.edu')
    driver.get_log('browser')
    return driver


def menu() -> int:
    """Displays a menu and returns the user selection (1-4)."""
    print('\nWhat would you like to do?')
    print('1: Add or update a class\n2: Remove a class\n3: Display saved classes\n4: Exit')

    while True:
        try:
            selection = int(input('\nMake a selection: '))
            if selection in {1, 2, 3, 4}:
                return selection
            else:
                print('Error: please enter a valid selection')
                time.sleep(1.5)
        except ValueError:
            print('Error: please enter a valid selection')
            time.sleep(1.5)


def search(driver: any) -> list[str]:
    """ prompts user to search for class, returns list with search results """
    usr_class = input('\nWhat class do you want to take: ')
    driver.execute_script("document.getElementById('crit-keyword').value='" + usr_class + "';")
    driver.execute_script("document.getElementById('search-button').click();")
    driver.execute_script("await new Promise(r => setTimeout(r, 2000));")
    driver.execute_script("console.log(document.querySelectorAll('[data-key]').length);")
    data_text = driver.get_log('browser')[0]['message']
    num_classes = int(data_text[17:])
    results = []
    for i in range(1, num_classes):
        driver.execute_script("console.log(document.querySelectorAll('[data-key]')[" + str(i) + "].textContent);")
        data_text = driver.get_log('browser')[0]['message']
        results.append(data_text[17:].split("\\n")[1] + ': ' + data_text[17:].split("\\n")[2])
    return results


def search_results(driver: any, results: list[str]) -> str:
    """ displays all classes from search results, returns class based on user selection """
    print('\nSearch Results:')
    for pos, course in enumerate(results, start=1):
        print(f'{pos}: {course}')
    print(f'{len(results) + 1}: Back to search')
    course = input("\nWhat class you want to check: ")

    try:
        if int(course) == len(results) + 1:
            print()
            results = search(driver)
            search_results(driver, results)
        else:
            driver.execute_script("document.querySelectorAll('[data-key]')[" + course + "].click();")
            driver.execute_script("await new Promise(r => setTimeout(r, 2000));")
            return results[int(course) - 1]
    except:
        print('\nError: must select a valid course')
        time.sleep(2)
        search_results(driver, results)


def check_seats(driver: any) -> tuple[int, str, int]:
    """  displays the remaining seats in each section of class from search_results, returns section, crn, 
    and remaining seats based on user selection"""
    print('\nSections:')
    driver.execute_script("console.log(document.getElementsByClassName(['course-section-all-sections-seats']).length);")
    data_text = driver.get_log('browser')[0]['message']
    num_sections = int(data_text[17:])

    seats_left = []
    for i in range(num_sections):
        driver.execute_script(
            "console.log(document.getElementsByClassName(['course-section-all-sections-seats'])[" + str(
                i) + "].textContent);")
        data_text = driver.get_log('browser')[0]['message']
        seats_left.append(int(data_text[26:len(data_text) - 1]))
        print(f'Section {i + 1}: {seats_left[i]} Seats')

    section = int(input("\nWhat section do you want to track: "))
    remaining_seats = seats_left[section - 1]

    driver.execute_script(
        "console.log(document.getElementsByClassName(['course-section-crn'])[" + str(section - 1) + "].textContent);")
    data_text = driver.get_log('browser')[0]['message']
    crn = data_text[24:len(data_text) - 1]

    return section, crn, remaining_seats


def update_file(driver: any, course: str, section: int, crn: str, remaining_seats: int) -> None:
    """ updates classes.txt based on course, section, crn, and remaining seats parameters"""
    data_text = []
    open('classes.txt', 'a').close()
    with open('classes.txt', 'r') as fh:
        updated = False
        for line in fh.readlines():
            if crn in line:
                data_text.append(f'{course}, Section: {section}, CRN: {crn}, Seats: {remaining_seats}\n')
                updated = True
            else:
                data_text.append(line)
        if not updated:
            data_text.append(f'{course}, Section: {section}, CRN: {crn}, Seats: {remaining_seats}\n')

        if len(data_text) > 1:
            data_text[-2] += '\n'
        data_text[-1] = data_text[-1].rstrip()

    with open('classes.txt', 'w') as fh:
        fh.writelines(data_text)

    driver.execute_script("document.getElementsByClassName('fa fa-caret-left')[0].click();")


def remove_class() -> None:
    """ removes class from classes.txt based on user input"""
    if os.path.exists('classes.txt'):
        with open('classes.txt', 'r') as fh:
            lines = fh.readlines()
            if not lines:
                print('Error: you do not have any courses added')
                time.sleep(1.5)
            else:
                print('\nClasses:')
                for pos, line in enumerate(lines, start=1):
                    print(f'{pos}: {line.rstrip()}')
                remove = int(input('\nSelect which class you want to remove: '))
                try:
                    lines.pop(remove - 1)
                    with open('classes.txt', 'w') as fh:
                        fh.writelines(lines)
                except:
                    print('Error: please enter a valid selection')
                    time.sleep(1.5)
                    remove_class()
    else:
        print('Error: you have not added any courses yet')
        time.sleep(1.5)


def display_classes() -> None:
    """ displays classes in classes.txt"""
    print()
    if os.path.exists('classes.txt'):
        with open('classes.txt', 'r') as fh:
            lines = fh.readlines()
            if not lines:
                print('Error: you do not have any courses added')
                time.sleep(1.5)
            else:
                print('\nClasses:')
                for pos, line in enumerate(lines, start=1):
                    print(f'{pos}: {line.rstrip()}')
                input()
    else:
        print('Error: you do not have any courses added')
        time.sleep(1.5)


def main() -> None:
    # main execution
    driver = setup()

    done = False
    while not done:
        choice = menu()
        if choice == 1:
            results = search(driver)
            course = search_results(driver, results)
            section, crn, remaining_seats = check_seats(driver)
            update_file(driver, course, section, crn, remaining_seats)
        elif choice == 2:
            remove_class()
        elif choice == 3:
            display_classes()
        elif choice == 4:
            print('Goodbye!')
            done = True
    driver.quit()


if __name__ == '__main__':
    main()
