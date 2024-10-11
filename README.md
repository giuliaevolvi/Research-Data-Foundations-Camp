# Researdh-Data-Foundations-Camp
This is a repository with my project for the Research Data Foundations Camp Microcredential

## Project Description and Research Question
The Research Question comes from a larger project that I am conducting, called MERGE- Media, religion, and gender: transnational digital media actions of progressive and conservative social movements. I want to explore topics and discourses used by Catholic groups that discuss family and gender related issues. In particular, I have identified two groups, Women’s Ordination Conference and CitizenGO, the first one is progressive and the second is conservative. They are both active on Instagram. The question I will explore first is:

RQ: What are the most frequently-used words in the Instagram pages of Women’s Ordination Conference and CitizenGO?

In order to do so, I created two datasets collecting all the posts of the two groups from their official Instagram profile. Then, I have focused on the text only, and created an excel file with all of the posts. Then, I found the 20 most frequently used words in each dataset and I visually represented them. 


## Python Script and Analysis Output

I created a dataset by downloading all of the data from Instagram using Instaloader. Then, I have put the .txt files into an excel (first I had put all the txt. Files in a separate folder from the pictures and the videos). For this specific project I am not using the pictures. Finally, I asked Python to create a list of the most used words in these texts and visually represent them. 

```python
# Python script
import pandas as pd

# Example code
data = pd.read_csv('data.csv')
print(data.head())

## Data Set Evaluation

My dataset is part of a European Union funded project called MERGE- Media, religion, and gender: transnational digital media actions of progressive and conservative social movements, under the Marie Skłodowska-Curie Actions (MSCA). Thiis funding scheme requires that all the dataset I create operate under FAIR principles, and that they are made accessible and open access. My host institution is the University of Bologna, that already has an open repository that complies with the FAIR principles, called AMSActa (https://amsacta.unibo.it/). As per my Data Management Plan, I will deposit my data in the trusted data repository AMSActa, which will attribute a unique persistent identifier (PID) to the deposited items [DOI]. In order to make sure that the data comply with FAIR principles, what I will do is:
•	converting the files to standard open formats; 
•	providing all relevant documentation and explanation for the data and the datasets;
•	anonymizing and aggregating the data
For dataset naming, in order to improve data visibility, discoverability, citation and permanent online tracking, the following naming will be chosen:
[PROJECT ACRONYM]_TaskNumber_Coverage or other content specifications_Date(YYYYMMDD)_VersionNumber.fileExtention
Example: 
MERGE_Dataset1_240124_v0.1.odt
In terms of ethics, the data come from public Instagram pages and do not generally contain names of specific users, as they reflect the views of an organization. I will not collect comments, since they can be written by private users that do not wish to have their data analyzed. It is important to notice that the two groups under analysis are campaign organizations, and therefore there is an expectation that they create online content with the intent of making it public. 


