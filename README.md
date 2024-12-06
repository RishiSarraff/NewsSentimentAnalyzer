<h1 align="center">News Sentiment Analyzer</h1>

<div align="center">
  <img src="images/foxvscnn.webp" alt="Fox Vs. CNN Image" title="Fox News vs. CNN" style="width: 100%; max-width: 800px; border-radius: 10px;">
</div>

<hr>

<h2>Context</h2>
<p>
After elections, there is often a surge in bipartisanship and extreme attitudes, with recent events leading to threats of violence and harmful behaviors. 
This highlights the need to understand the sources of voters' and citizens' frustrations and alignments with specific political parties.
</p>
<p>
While uncontrollable factors like family and social circles play a role, one significant influence on American politics is news media and its often-biased portrayal of "unbiased" information.
</p>

<hr>

<h2>Problem Statement</h2>
<p>
With the 2024 election wrapping up, we aim to examine how two major news networks — <strong>CNN</strong> (Democrat-leaning) and <strong>Fox News</strong> (Republican-leaning) — influence voter decisions.
</p>
<p>
To address this, we developed a quantitative method to measure subjective political sentiment using tools like web scraping, data analysis, and sentiment analysis.
</p>

<hr>

<h2>Approach</h2>
<p>Our approach involves the following steps:</p>
<ol>
  <li><strong>Data Collection</strong>: 
    Scrape political articles from CNN and Fox News websites using the Python Selenium library and store the scraped data in a lightweight <strong>SQLite database</strong>.
  </li>
  <li><strong>Data Conversion</strong>: 
    Export the data from SQLite into a structured <strong>CSV file</strong> for easier analysis.
  </li>
  <li><strong>Sentiment Analysis</strong>: 
    Use tools like <strong>TextBlob</strong> to analyze sentiment in the articles.
  </li>
  <li><strong>Data Visualization</strong>: 
    Utilize <strong>matplotlib</strong> and <strong>seaborn</strong> to generate insightful visualizations from the standardized sentiment data.
  </li>
  <li><strong>Presentation</strong>: 
    Create a detailed presentation showcasing the analysis and findings.
  </li>
</ol>

<hr>

<h2>Steps</h2>
<ol>
  <li>Scrape articles using <strong>Selenium</strong>.</li>
  <li>Store the data into a <strong>SQLite database</strong>.</li>
  <li>Export the data to a <strong>CSV file</strong>.</li>
  <li>Analyze sentiment using <strong>pandas</strong>, <strong>TextBlob</strong>.</li>
  <li>Visualize results using <strong>matplotlib</strong> and <strong>seaborn</strong>.</li>
</ol>

<hr>

<h2>Technologies Used</h2>
<ul>
  <li><strong>Web Scraping</strong>: Selenium</li>
  <li><strong>Database</strong>: SQLite</li>
  <li><strong>Data Analysis</strong>: pandas, TextBlob</li>
  <li><strong>Visualization</strong>: matplotlib, seaborn</li>
  <li><strong>Data Handling</strong>: CSV</li>
</ul>

<hr>

<h2>Deliverables</h2>
<ul>
  <li>A structured <strong>SQLite database</strong> of news articles.</li>
  <li>A <strong>CSV file</strong> for sentiment analysis.</li>
  <li>Sentiment analysis visualizations (e.g., bar plots, line charts).</li>
  <li>A <strong>presentation</strong> summarizing findings and insights.</li>
</ul>
