#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas nltk


# In[12]:


import pandas as pd
import nltk
from nltk.corpus import stopwords
from collections import Counter
import re

# Download stopwords from NLTK
nltk.download('stopwords')

# Define a function to preprocess and clean text
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation and numbers
    text = re.sub(r'\W+|\d+', ' ', text)
    # Tokenize and remove stopwords
    tokens = [word for word in text.split() if word not in stopwords.words('english')]
    return tokens

# Step 1: Load the Excel file
excel_path = "C:/Users/Giulia Evolvi/instagram_posts citizengo.xlsx"  # Replace with your Excel file path
data = pd.read_excel(excel_path)

# Step 2: Assuming the text is in a column named 'Content' (adjust as necessary)
data['Content'] = data['Content'].astype(str)  # Ensure text is treated as strings

# Step 3: Preprocess and tokenize the text
data['Tokens'] = data['Content'].apply(preprocess_text)

# Step 4: Combine all tokens into a single list
all_tokens = [token for tokens_list in data['Tokens'] for token in tokens_list]

# Step 5: Calculate word frequencies using Counter
word_frequencies = Counter(all_tokens)

# Step 6: Display the most common words
most_common_words = word_frequencies.most_common(20)  # Adjust the number to see more words
print("Most Common Words:")
for word, freq in most_common_words:
    print(f"{word}: {freq}")


# In[14]:


import matplotlib.pyplot as plt

# Convert most_common_words to a DataFrame for visualization
word_freq_df = pd.DataFrame(most_common_words, columns=['Word', 'Frequency'])

# Plot a bar chart
plt.figure(figsize=(10, 6))
plt.barh(word_freq_df['Word'], word_freq_df['Frequency'], color='skyblue')
plt.xlabel('Frequency')
plt.ylabel('Words')
plt.title('Top 20 Most Frequent Words')
plt.gca().invert_yaxis()  # Invert y-axis to show the highest frequency words at the top
plt.show()


# In[16]:


import pandas as pd
import nltk
from nltk.corpus import stopwords
from collections import Counter
import re

# Download stopwords from NLTK
nltk.download('stopwords')

# Define a function to preprocess and clean text
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation and numbers
    text = re.sub(r'\W+|\d+', ' ', text)
    # Tokenize and remove stopwords
    tokens = [word for word in text.split() if word not in stopwords.words('english')]
    return tokens

# Step 1: Load the Excel file
excel_path = "C:/Users/Giulia Evolvi/instagram_posts woc.xlsx"  # Replace with your Excel file path
data = pd.read_excel(excel_path)

# Step 2: Assuming the text is in a column named 'Content' (adjust as necessary)
data['Content'] = data['Content'].astype(str)  # Ensure text is treated as strings

# Step 3: Preprocess and tokenize the text
data['Tokens'] = data['Content'].apply(preprocess_text)

# Step 4: Combine all tokens into a single list
all_tokens = [token for tokens_list in data['Tokens'] for token in tokens_list]

# Step 5: Calculate word frequencies using Counter
word_frequencies = Counter(all_tokens)

# Step 6: Display the most common words
most_common_words = word_frequencies.most_common(20)  # Adjust the number to see more words
print("Most Common Words:")
for word, freq in most_common_words:
    print(f"{word}: {freq}")


# In[18]:


import matplotlib.pyplot as plt

# Convert most_common_words to a DataFrame for visualization
word_freq_df = pd.DataFrame(most_common_words, columns=['Word', 'Frequency'])

# Plot a bar chart
plt.figure(figsize=(10, 6))
plt.barh(word_freq_df['Word'], word_freq_df['Frequency'], color='skyblue')
plt.xlabel('Frequency')
plt.ylabel('Words')
plt.title('Top 20 Most Frequent Words')
plt.gca().invert_yaxis()  # Invert y-axis to show the highest frequency words at the top
plt.show()


# In[20]:


import pandas as pd
from collections import Counter
import re

# Step 1: Load the Excel file
excel_path = "C:/Users/Giulia Evolvi/instagram_posts woc.xlsx"  # Replace with your Excel file path
data = pd.read_excel(excel_path)

# Step 2: Assuming the text is in a column named 'Content' (adjust as necessary)
data['Content'] = data['Content'].astype(str)  # Ensure text is treated as strings

# Step 3: Define a function to extract hashtags from text
def extract_hashtags(text):
    # Use regular expression to find all hashtags (words starting with #)
    hashtags = re.findall(r'#\w+', text)
    return hashtags

# Step 4: Apply the function to extract hashtags from each post
data['Hashtags'] = data['Content'].apply(extract_hashtags)

# Step 5: Combine all hashtags into a single list
all_hashtags = [hashtag for hashtags_list in data['Hashtags'] for hashtag in hashtags_list]

# Step 6: Calculate hashtag frequencies using Counter
hashtag_frequencies = Counter(all_hashtags)

# Step 7: Display the most common hashtags
most_common_hashtags = hashtag_frequencies.most_common(20)  # Adjust number of hashtags if needed
print("Most Common Hashtags:")
for hashtag, freq in most_common_hashtags:
    print(f"{hashtag}: {freq}")


# In[22]:


import matplotlib.pyplot as plt

# Convert most_common_hashtags to a DataFrame for visualization
hashtag_freq_df = pd.DataFrame(most_common_hashtags, columns=['Hashtag', 'Frequency'])

# Plot a bar chart
plt.figure(figsize=(10, 6))
plt.barh(hashtag_freq_df['Hashtag'], hashtag_freq_df['Frequency'], color='skyblue')
plt.xlabel('Frequency')
plt.ylabel('Hashtags')
plt.title('Top 20 Most Used Hashtags')
plt.gca().invert_yaxis()  # Show most frequent hashtags at the top
plt.show()


# In[24]:


import pandas as pd
from collections import Counter
import re

# Step 1: Load the Excel file
excel_path = "C:/Users/Giulia Evolvi/instagram_posts citizengo.xlsx"  # Replace with your Excel file path
data = pd.read_excel(excel_path)

# Step 2: Assuming the text is in a column named 'Content' (adjust as necessary)
data['Content'] = data['Content'].astype(str)  # Ensure text is treated as strings

# Step 3: Define a function to extract hashtags from text
def extract_hashtags(text):
    # Use regular expression to find all hashtags (words starting with #)
    hashtags = re.findall(r'#\w+', text)
    return hashtags

# Step 4: Apply the function to extract hashtags from each post
data['Hashtags'] = data['Content'].apply(extract_hashtags)

# Step 5: Combine all hashtags into a single list
all_hashtags = [hashtag for hashtags_list in data['Hashtags'] for hashtag in hashtags_list]

# Step 6: Calculate hashtag frequencies using Counter
hashtag_frequencies = Counter(all_hashtags)

# Step 7: Display the most common hashtags
most_common_hashtags = hashtag_frequencies.most_common(20)  # Adjust number of hashtags if needed
print("Most Common Hashtags:")
for hashtag, freq in most_common_hashtags:
    print(f"{hashtag}: {freq}")


# In[26]:


import matplotlib.pyplot as plt

# Convert most_common_hashtags to a DataFrame for visualization
hashtag_freq_df = pd.DataFrame(most_common_hashtags, columns=['Hashtag', 'Frequency'])

# Plot a bar chart
plt.figure(figsize=(10, 6))
plt.barh(hashtag_freq_df['Hashtag'], hashtag_freq_df['Frequency'], color='skyblue')
plt.xlabel('Frequency')
plt.ylabel('Hashtags')
plt.title('Top 20 Most Used Hashtags')
plt.gca().invert_yaxis()  # Show most frequent hashtags at the top
plt.show()


# In[29]:


import pandas as pd
from collections import Counter
import re

# Step 1: Load the Excel file
excel_path = "C:/Users/Giulia Evolvi/instagram_posts woc.xlsx"   # Replace with your Excel file path
data = pd.read_excel(excel_path)

# Step 2: Assuming the text is in a column named 'Content' (adjust as necessary)
data['Content'] = data['Content'].astype(str)  # Ensure text is treated as strings

# Step 3: Define a function to extract account mentions from text
def extract_mentions(text):
    # Use regular expression to find all mentions (words starting with @)
    mentions = re.findall(r'@\w+', text)
    return mentions

# Step 4: Apply the function to extract mentions from each post
data['Mentions'] = data['Content'].apply(extract_mentions)

# Step 5: Combine all mentions into a single list
all_mentions = [mention for mentions_list in data['Mentions'] for mention in mentions_list]

# Step 6: Calculate mention frequencies using Counter
mention_frequencies = Counter(all_mentions)

# Step 7: Display the most common mentions
most_common_mentions = mention_frequencies.most_common(20)  # Adjust number if needed
print("Most Common Mentions:")
for mention, freq in most_common_mentions:
    print(f"{mention}: {freq}")


# In[31]:


import pandas as pd
from collections import Counter
import re

# Step 1: Load the Excel file
excel_path = "C:/Users/Giulia Evolvi/instagram_posts woc.xlsx"  # Replace with your Excel file path
data = pd.read_excel(excel_path)

# Step 2: Assuming the text is in a column named 'Content' (adjust as necessary)
data['Content'] = data['Content'].astype(str)  # Ensure text is treated as strings

# Step 3: Define a function to extract account mentions from text
def extract_mentions(text):
    # Use regular expression to find all mentions (words starting with @)
    mentions = re.findall(r'@\w+', text)
    return mentions

# Step 4: Apply the function to extract mentions from each post
data['Mentions'] = data['Content'].apply(extract_mentions)

# Step 5: Combine all mentions into a single list
all_mentions = [mention for mentions_list in data['Mentions'] for mention in mentions_list]

# Step 6: Calculate mention frequencies using Counter
mention_frequencies = Counter(all_mentions)

# Step 7: Display the most common mentions
most_common_mentions = mention_frequencies.most_common(20)  # Adjust number if needed
print("Most Common Mentions:")
for mention, freq in most_common_mentions:
    print(f"{mention}: {freq}")


# In[ ]:




