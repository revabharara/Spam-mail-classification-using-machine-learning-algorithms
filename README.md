
# 🎯Email Spam Classification using Machine Learning Algorithms

This project is aimed at developing a machine learning model that can classify emails as either spam or ham. The project uses several popular algorithms, including logistic regression, decision trees, SVM, Naive Bayes, and random forest.




## 🚩About the Dataset
The provided dataset is a collection of emails that have been randomly selected and classified as either spam or ham. The dataset consists of two columns, with the first column indicating the classification of each email as spam or ham. The second column contains the content of the emails themselves.

| Column ID  | Column Name | Data type  | Description |
| ------------- | ------------- |------------- | ------------- |
| 0 | Category  | Object | classification of mails as spam or ham |
| 1  | Message  | Object | content of the emails  |


## 🛣️Roadmap

1. ### 🔭Data analysis (Priliminary and Exploratory)
The process typically involves multiple steps such as data exploration, data visualization, and statistical analysis to derive meaningful insights from the data.

2. ### ⚙️Data preprocessing
It includes handling missing or incorrect data, transforming data into a more useful format, and scaling or normalizing data.

3. ### 📊Model selection and prediction
This involves evaluating different models and selecting the one that best fits the data and is capable of making accurate predictions. 

4. ### ⛳ Model comparison
Model comparison involves comparing the performance of different models on a given task to identify which model is most effective.

5. ### 🏆Model implemetation and analysis
Once a suitable model has been selected, it can be implemented and trained on the data. The results can then be analyzed to identify areas for improvement in the model for better performance.

## ⚙️Data Preprocessing
* #### Dealing with missing values
The dataset had no values that were missing or irrelevant so there was no need tof preprocessing those.

* #### Label encoding
Since the labels were categorical I had to perfrom Label Encoding (Ham:0, Spam:1) for proper classification.

* ####  Creating feature vectors
the textual mail content was converted into feature vectors using the TfidfVectorizer from sklearn.

*TF-IDF (Term Frequency-Inverse Document Frequency) is a feature extraction method used in natural language processing to quantify the importance of words in a text document. The TfidfVectorizer converts a collection of raw text documents into a matrix of TF-IDF features, which can be used for various NLP tasks.*



## 📊Models prediction and comparison

| Models    | Accuracy score  | F1 score |
| ------------- | ------------- |------------- | 
| Logistic Regression	 | 0.858296	  | 0.792847| 
| Decision Tree	  | 0.961435	  | 0.960624 |
| SVM		  | 0.973094	  | 0.971891 |
| Naive Bayes  | 0.961435	  | 0.958821 | 
| Random Forest Classification	  | 0.973094	  | 0.971980 |

After thorough analysis, it was observed that the random forest algorithm outperformed the others in terms of accuracy and F1 score.

The results showed that the random forest algorithm had an accuracy of 97.3094% and an F1 score of 97.1980%.

![image](https://user-images.githubusercontent.com/89579327/224524629-b8d0eb63-c146-4170-b39c-7ef340cb219a.png)


![image](https://user-images.githubusercontent.com/89579327/224524637-82448763-f34c-4f3a-8ce7-77b15d0026d2.png)

 
## 🎯Model implemetation and analysis
The results showed that the random forest algorithm achieved the highest accuracy and F1 score among all the algorithms tested. This indicates that the algorithm had the best balance between precision and recall in classifying spam and ham emails.

<img width="356" alt="image" src="https://user-images.githubusercontent.com/89579327/224524679-2195b1e2-7264-4190-a6aa-fde3c7f7fba0.png">


![image](https://user-images.githubusercontent.com/89579327/224524656-18d0d6ec-e41b-4f21-ab53-3e225a14ea02.png)


## 🖌🎨GUI program
The Gui application allows the user to enter the content of the mail in the entry field and then using the Random Forest Classifier in the backend the application predicts whether the mail is spam or not.

#### Screenshots of the GUI project:

<img width="676" alt="image" src="https://user-images.githubusercontent.com/89579327/224524813-3ebdba10-59c5-4532-8316-6de4167cdf61.png">


#### 🖼️Output:

<img width="674" alt="image" src="https://user-images.githubusercontent.com/89579327/224524824-935ab661-0548-48a9-ba7a-14fcc4e32950.png">

#### ### 🎍Conclusion:
In conclusion, this data science project aimed to classify spam and ham mails using various machine learning algorithms. The algorithms used were logistic regression, decision trees, SVM, Naive Bayes, and random forest. After thorough analysis, it was observed that the random forest algorithm outperformed the others in terms of accuracy and F1 score.

The results showed that the random forest algorithm had an accuracy of 97.3094% and an F1 score of 97.1980%.

This project shows that the random forest algorithm is an effective method for classifying spam and ham mails. However, it is important to note that the performance of the algorithm can be improved by tuning hyperparameters or using other techniques such as feature selection.


### 🧮 Limitations:
1. Limited scope: The project focused solely on classifying emails as spam or ham and did not explore other email classification tasks, such as sentiment analysis or topic modeling.
2. Dataset size: The size of the dataset used in this project may be limited, which could affect the accuracy and generalization of the models. A larger dataset may lead to better results.

### 🔮 Future Prospects:
1. Real-time testing: Testing the models in real-time scenarios could help to identify and address unforeseen challenges and improve the practical application of the models.
2. Improved accuracy: Further research and experimentation with more advanced algorithms and feature engineering techniques could potentially lead to increased accuracy in email classification.
3. Integration with existing systems: Integrating the models into existing email systems, such as spam filters, could provide immediate practical benefits for users and organizations.


## Credits
*Reva Bharara*

*Email : revabharara@gmail.com, bhararareva@gmail.com*

*Linkedin : https://www.linkedin.com/in/reva-bharara-a83a78241/*
