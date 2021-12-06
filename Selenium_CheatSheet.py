
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



##Esperar que cargue el DOM entero 
options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
# Navigate to url
driver.get("http://www.google.com")

def clear_cache(driver, timeout=60):
    """Clear the cookies and cache for the ChromeDriver instance."""
    # navigate to the settings page
    driver.get('chrome://settings/clearBrowserData')

    # wait for the button to appear
    wait = WebDriverWait(driver, timeout)
    wait.until(driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm'))

    # click the button to clear the cache
    driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm').click()

    # wait for the button to be gone before returning
    wait.until_not(driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm'))

def chromeConExtension(driver,pathCRX, timeout=60):
	options = Options()
	options.addExtensions(new File("/path/to/extension.crx")); #Esto es java, hay que translate a python xd
	browser = webdriver.Chrome(path, options= options)

def optionsChrome(driver)
	options = Options()
	options.add_argument("--headless")
	options.add_argument("--start-maximized")
	options.add_argument("--incognito")

	#Si no quieres tener problemas con SSL...->
	options.add_argument('--allow-running-insecure-content')
	options.add_argument('--ignore-certificate-errors')

	opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")


	return options

def opcionesCierre(driver):
	driver.quit()

	def tearDown(self):
		self.driver.quit()


	try:
		#WebDriver code here...
	finally:

def jsChrome(driver):
	##Document root level
	javaScript = "document.getElementsByName('username')[0].click();"
	javaScript2 = "document.getElementsByClassName('ola')[0].click()"
	javaScript3 = "document.getElementsByID('intro').click()"            #No hace falta index porque se supone que el ID es único
	driver.execute_script(javaScript)
	text = driver.execute_script('return document.getElementById("fsr").innerText')



	##Js at element level
	userName = driver.find_element_by_xpath("//button[@name='username']")
	password = driver.find_element_by_xpath("//button[@name='password']")
	driver.execute_script("arguments[0].click();arguments[1].click();", userName, password)

	##Scroll
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	#Maximize
	driver.maximize_window()

def waits():
	#Implicit
	driver.implicitly_wait(15)

	#Explicit
	wait = WebDriverWait(self.driver, timeout)
	wait.until(expected_conditions.visibility_of_element_located((By.ID, 'quoteElementPiece5')))
	wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "img-wrap")))


