# Scrapy-Redis---Python
Apply a distributed system onto web-scraping. This project is an advancement from my other project Scrapy---Python, so it is recommended to read through Scrapy---Python first for basic understandings.

In a nutshell, the master passes url to the slave and retrives data back from the slave, storing the data into the database. The slave is mainly responsible for scraping the urls.

NOTE: This is not a complete version of the actual project, since it only consists of my part (the master part) of the code. My colleagues's code (the slave part of the code) is not shown here.

WARNING: Redis utilizes RAM memory for speed (which only applies to the master since the master collects scraped data from the slave), so it is STRONGLY RECOMMENDED that the master machine should have RAM of at least 8GB. For example, my computer has 4GB RAM memory, and the data collected totalled 1.5GB, causing massive delays in the storing process.
