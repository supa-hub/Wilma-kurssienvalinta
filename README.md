# Wilma-kurssienvalinta
voi valita kurssit nopeasti ja tehokkaasti wilmasta. Ei tarvitse sitten itse kiirehtiä kurssivalintojen aikana

Koodi käyttää Pythonin Selenium pakettia ja Chromedriver:iä. Koodi avaa Chromen, josta se kirjautuu Wilmaan Microsoft login-toiminnon avulla ja sitten menee kurssivalintoihin.

tarkempi selitys tehty englanniksi:
---
The external python libraries used by the code:
Selenium,
pathlib

The code needs to have the same version of chromedriver, as the version of the chrome browser you have on your computer. 
The current chromedriver in the repository is chromedriver 99. I will try to update the chromedriver by time, but if I forget you can
download the current version of chromedriver from https://chromedriver.chromium.org/home  (I recommend using the stable release)

The code Cannot be executed in Visual studio code (it is and IDE issue by the developers of VS Code, not mine). 
The easiest way to execute it is by just using the normal python idle.

GUIDE TO USING THE CODE
---
First you need to open the code file and insert into the parts sähköposti and salasana, well, the things that the words mean. 
PLEASE NOTE that oyu haveto put the account Email and password into the quotemarks, SO THESE: "", so
for example: sähköposti = "juu@gmail.com",  salasana = "moi123"
Then you will have to use inspect element from chrome to get the full Xpath of every course block in the kurssitarjotin in Wilma. 
These Xpaths you have to insert into the list "elements_list", by putting the xpath between quote marks as before into the [] signs. 
There are 2 of those kinds of Xpaths already in the code, you can use them as example

Then voilà, just run the code.

