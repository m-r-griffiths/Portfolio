# Using Natural Langauge Processing (NLP) to identify options for operational improvements in a restaurant chain

![Preview](./word_cloud.png)
- **Background**: This was an assessed project that I completed as part of my course on Data Science, with Machine Learning and AI, at the University of Cambridge. The reviewer kindly described the insights derived as 'excellent' and 'likley to be very useful to stakeholders'.  
- **Problem**: Use NLP techniques to identify, from on-line reviews of a restaurant chain, options for improving the customer experience.
- **Data**: The original datasets were real on-line reviews of a wellbeing chain. For privacy reasons, the analysis here has been carried out on synthetic data.
- **Deliverables**: Gooogle Collab notebook with full workflow and visuals, PDF report with findings and recommendations.

## Approach
- **Data cleaning**:
  - Remove reviews with missing long-text content.
  - Remove reviews not in English.
- **Data preparation**:
  - Tokenise text and remove stop-words.    
- **Analysis Stages**:
  - Identify the most frequently occuring words in i) all customer reviews and ii) negative reviews.
  - Use BERTopic to to identify the themes in:
    i) negative reviews
    ii) reviews from restaurant locations that generate the most negative reviews, and
    iii) reviews where anger is the dominant emotion
  - Use a large language model, in combination with BERTopic, to do the same.
- **Visualisations**:
  - Word frequency counts and word clouds
  - Geographic mapping of restaurants that generate the most negative reviews
  - BERTopic visualisations

## Key Results
- Focusing on reviews where anger is the dominant emotion is most likley to reduce customer churn. Key improvement opportunities here are: reducing waiting time for food, improving order accuracy and ensuring the cleanliness of tables.
- Five London restuarants are priorities for site specific improvements. 

## How to Reproduce
1. Open Applying supervised learning to predict student dropout .ipynb
2. Ensure dependencies are installed
3. Run cells sequentially. The notebook loads data from the two csv files in this folder:.
