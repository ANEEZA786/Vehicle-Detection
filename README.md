# Overview
Vehicle detection, tracking and counting is the basic need of the society for trouble free and safer travelling in cities. Vehicle detection helps to solve my societal issues such as:
•	Helps to collect the Toll tax at motorway according to vehicle’s size
•	Traffic violation detection
To collect toll tax at motorway we have to detect the vehicles to collect reasonable toll from the particular vehicle according to its size. For this purpose, classify the small vehicles i.e. cars have less toll tax as compare to the large vehicles i.e. truck which is quite laborious work for human and there are maximum chances of errors.
The solution of this problem is to classify the vehicles by using the supervised machine learning model. As data is labeled, that is weight, height/length, no. of passengers sits in particular vehicle & try to predict the upcoming vehicles on the basis of previous experience on which it is trained. That is ultimately helps to improve the economy of the country. 

#Details
<h3>Pre Processing</h3
  At first, preprocessing of data is important which transform our raw data in a useful and efficient format. So, that machine learning model can easily parse it. As there many missing values are in our specific data in particular column “tire”.
  After analyzing the data drop the column which contains the useless information as in our scenario car’s id contain useless information which has no role to predict the toll tax of vehicle which ultimately helps to improve accuracy. So, we drop that particular column.
  After that filled the missing values by taking the mean or average values of that particular column in which missing values are present. We may drop the rows of missing values but that’s not a good approach as it affects the accuracy of model.

<h3>Details</h3>
After processing of data, training & testing of data is important because it is a supervised learning. Then, we apply classification models on data. As our data is discrete and different classes such as our vehicle either a car or truck are present. So, apply different classification models like K-Nearest Neighbor (KNN), Support Vector Machine (SVM), Naïve- Bayes & Decision Trees. After applying all the model, we obtain approximately, 94% accuracy by SVM that is better than other classification models because classifier is having the ability to provide the high accuracy in classification while, working with high dimensional data. SVM classifier actually comes under kernel based algorithmic approaches. In this approach, the data dependency is also identified as the functional computation to generate the feature space. The advantages of the work are defined in terms of non-linear decision boundaries defined under method specification for linear classification. This classifier is defined along with the specification of kernel function that itself provides the fixed dimensional vector representation with sequence generation and structural representation. There are different types of kernels are used as our data is balanced that’s why we used simplest SVM along with linear kernel. 

#Conclusion
Support Vector Machine (SVM) is a supervised machine learning algorithm which can be used for both classification and regression challenges but mostly used for classification problems. As we apply all classification models on our data but obtained better accuracy with SVM because this model is good for sparse features and provide simple decision boundary which doesn’t have any kind of issues with overfitting and of following reasons:
•	It uses Kernel trick.
•	It is Optimal margin based classification technique in Machine Learning.
•	There are good number of algorithms are proposed which utilizes problem structures and other smaller, smaller things like problem shrinking during optimization etc.
To concluded, preprocessing is important technique to convert raw data into clean data which machine can easily parse it to provide good results. After preprocessing different kinds of classification models like Decision tree and KNN applied which provides good accuracy almost 93% to our data but SVM provides better accuracy i.e. 94% because of our balanced dataset and SVM provides optimized result at smaller things like problem shrinking as compare to other models.

