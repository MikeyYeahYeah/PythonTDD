from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True
        self.browser = webdriver.Firefox(capabilities=firefox_capabilities)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

# User hears about our site and visits our home page
        self.browser.get('http://localhost:8000')

# The site title reaffirms that this is in fact a To-Do list site
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
# The user is invited to enter a To-Do list entry right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter To-Do Item')

# The user Types "Buy Milk and Bread"
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy Milk and Bread' for row in rows))

# The user hits enter, the page updates, and presents "1: Buy Milk and Bread"

# The user sees a text box asking them to add another item.  User enters "Buy Chicken Breast"

# Just being thorough
        self.fail('Finish the test!')

# The page updates again and presents both items

# The user wonders if the site will remember their entries.  They see that a unique URL has been generated for them as well as some text explaining what the URL is for

# The user visits the URL and sees that their list is still there

# The user closes the page

if __name__ == '__main__':
    unittest.main(warnings='ignore')
