# MSRC-Scraper
Scrapes Microsoft's Security Response Center's Vulnerabilities to pull relevant fields + download security updates in xlsx format using Python in combination with Selenium WebDriver. 

Keep in mind I used Selenium to scrape data from Microsoft's Security Response Data and each CVE had similar XPath elements which allowed me to pinpoint the data I was looking to obtain but some CVE's may have elements which are misaligned to what I was looking for in particular. 

More information about Selenium (I suggest reading this before proceding with creating a project): https://www.selenium.dev/documentation/webdriver/ 
	
  
###Start###

1. Install Selenium within your IDE terminal (mine was PyCharm Community Edition:https://www.jetbrains.com/pycharm/download), this is the Python library and tool we will be utilizing for this project.
	a. "pip install selenium"

2. Install WebDriver for the particular browser you will test/automate against (I used Chrome), this is the process which will open up the browser automatically and navigate to websites for testing.
	a. Chrome WebDriver: https://chromedriver.chromium.org/downloads. 

3. At this point, you will have to locate XPath (which are used to navigate through elements and attributes in an XML document) and locate what you are searching for. Locate XPath will be the bread and butter of Selenium as you are grabbing XML elements for which you will test/automate against. 
	a. I downloaded SelectorsHub (a chrome extension) which helps with locating XPaths but some will require more crafting to locate the proper element. 
	b. Useful locators: https://www.selenium.dev/documentation/webdriver/elements/locators/
