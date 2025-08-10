i have created a heart disease prediction app using logistic regression and deployed it with streamlit 


steps and challenges :-
1.IMPORT LIBRARIES 
imported all required libraries 
-pandas 
-numpy
-sickit-learn
-streamlit

2.EDA

perform eda although data was clean but ther eis one minor issue with this data set its gender imbalanced
at first i didnt understood why my model wanst giving good output and confusion metrics was showing 11 ,21
for  type 1 and type 2 error i was so confused what to do then i reach to my friends but couldnt find a solution 
then after few days i saw post on ig that clicked me about concept "imbalanced dataset"  i used value_count()
ceck te ratio of male vs female as expected there was a diffrence of 30-70 i did rnd then i used logistic regression and used 
(class_weight = "balanced") hyperparameter and proceed to next part

3.DEPLOYMENT 

deployement :- i got various issues while deploying this project some time input erorrs where there some time "label-encoder" issued 
-i used fit transform on categorical data anf then gave values for input using standard sclaer because of length difference of numeric values in columns 

 4. STREAMLIT AND GITHUB
 used streamlit to deploy was kinda tiring for the first time managed to learn deployement by connecting streamlit-cloud with git-hub
app link:-https://heartpredictionapp.streamlit.app/


YOUR VIEW?
if you have any advice for me i would be glad to hear it am always eager to learn more 
