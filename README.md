News Sentiment Analyzer:

Context:
After elections we see a surge in bipartisanship and attitudes becoming more extreme with recent elections
warranting threats of violence and harmful behaviors. This necessitates the need to understand the source of
voters' and citizens' frustrations and alignments with particular parties. While there are uncontrollable features
like family, friends, and more, one major source of American politics has always been News sources and their
overly biased "unbiased" news articles. 

Problem Statement:
With the 2024 election coming up to a wrap, we want to see how two major news channels, CNN and Fox News, that 
are very much Democrat and Republican leaning, respcetively, influence voter decisions. 

Approach:
In order to dictate this and figure out a quantitative way to measure something that is subjective, we decided 
to go to the websites, scrape hundreds of articles on different political topics from each of the news network 
websites and store them into a sqlite database. After scraping using the Python package Selenium, we insert 
into a lightweight sqlite database, from which we are able to convert into a csv file. 

After converting into a csv file, we move towards the sentiment analysis portion of the project where we use
tools like TextBlob or Vader to carry out the analysis and use plotting libraries like matplotlib and seaborn 
to generate data analysis to our standardized data that we formulated. 

Steps:
1. Scrape using Selenium
2. Store into SQLite Database
3. Save to CSV
4. Conduct analysis using pandas, TextBlob/Vader
5. Create Presentation.

Technologies:


