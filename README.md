# MSRC-Scraper
Scrapes Microsoft's Security Response Center's Vulnerabilities to pull relevant fields + download security updates in xlsx format using Python in combination with Selenium WebDriver. 

Keep in mind I used Selenium to scrape data from Microsoft's Security Response Data website (https://msrc.microsoft.com/update-guide/vulnerability). Each CVE had similar XPath elements properties which allowed me to pinpoint the data I was looking to obtain for multiple URL's, but some CVE's may have XPath elements which are misaligned or not present for particular URL's. 

More information about Selenium (I suggest reading this before proceding with creating a project): https://www.selenium.dev/documentation/webdriver/ 
	
  
###Start###

1. Install Selenium within your IDE terminal (mine was PyCharm Community Edition:https://www.jetbrains.com/pycharm/download). Selenium is the Python library and tool we will be utilizing for this project to automate and interact with XPath elements. 
	a. "pip install selenium"

2. Install WebDriver for the particular browser you will test/automate against (I used Chrome), this is the process which will open up the browser automatically and navigate to designated websites for testing.
	a. Chrome WebDriver: https://chromedriver.chromium.org/downloads. 

3. At this point, you will have to locate XPath (which are used to navigate through elements and attributes in an XML document) and locate what you are searching for. Locating XPath is the bread and butter of Selenium as you are grabbing XML elements for testing/automation.
	a. I downloaded SelectorsHub (a chrome extension) which helps locate simple and unique XPaths. Most if not the majority of XPath elements require more crafting.
	b. Useful locators: https://www.selenium.dev/documentation/webdriver/elements/locators/
	
	
At this point you can look through my previous python script and get a familiarity of how I wrote my code and how it was formatted. 
