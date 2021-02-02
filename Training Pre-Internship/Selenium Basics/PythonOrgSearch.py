#Using Selenium to write tests, basic example

#all basic modules are imported: unittest provides a frameowkr for organizing the test cases, selenium.webdriver provides WebDriver implementations, and the Keys class provides keys like RETURN, F1, etc
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#the test case class is inherited from unittest.TestCase. Inheriting from Test-Case class is the way to tell unittest module that this is the test case
class PythonOrgSearch(unittest.TestCase):

    #setUp is part of initialization. It gets called before every test function you write in the test case class. Here you create the instance of Firefox WebDriver
    def setUp(self):
        self.driver = webdriver.Firefox()

    #Below is the test case method. It should always start with the characters "test". The first line inside this method creates a local reference to the driver object created in setUp
    def test_search_in_python_org(self):
        
        driver = self.driver
        #driver.get naviages to a page given by the URL. WebDriver waits until the page is fully loaded before returning control to your test/script. Sometimes, if your page uses a lot of AJAX on load then WebDriver may not know when it has completely loaded.
        driver.get("http://www.python.org")
        #the next line is an assertion to confirm the title of the called page has "Python" in it
        self.assertIn("Python", driver.title)
        #WebDriver has 8 element locator techniques. Below, we use the name method
        elem = driver.find_element_by_name("q")
        #"Sending keys" is similar to entering keys using your keyboard. Special keys can be sent using Keys class imported from selenium.webdriver.common.keys
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        #After submission of the page, you should get the result as per search if there is any. To ensure that some results are found, make an assertion
        assert "No results found." not in driver.page_source

    #The tearDown method gets called after every test method. This is a place to do all cleanup actions; for example, here, the browser window is "closed." You can also call the "quit" method. Quit will exit the entire browser, whereas close will close a tab, but if it is the only tab only, many times the whole browser will close as well.
    def tearDown(self):
        self.driver.close()

#final lines are boiler place code to run the test suite
if __name__ == "__main__":
    unittest.main()
    
#You can run the above test case from a shell like this: 

python test_python_org_search.py
