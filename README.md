# Face_Detector

-> A basic python Scripted Algorithm used to detect some random faces, a simple flow of the whole algorithm is :-
  1.) Training or extracting Features and saving them for the future prediction on testing data...
  2.) Testing or predicting a new face of a user using the trained model...
  
 -> The whole process is simply divided in these two steps only..
 
 # Let's look into the technologies or libraries used to implement above steps...
   

Key Technologies used are: - 

a) For Training part : - openCV which is very popular library used for the pre-processing of images and videos as well, openCV enabling the algorithm to take some snapshots and saved their features into a individual file location in npy format because features of a face is given in numpy array format..

b) For feature extraction : - Haar Cascade classifiers are an effective way for object detection. This method was proposed by Paul Viola and Michael Jones in their paper Rapid Object Detection using a Boosted Cascade of Simple Features .Haar Cascade is a machine learning-based approach where a lot of positive and negative images are used to train the classifier and responsible to extract features of image.

c) For Testing part: - In this step a new face features recorded by our haar cascade using openCV is compared with all other faces features by using the concept of Machine Learning i.e KNN Algorithm, this algorithm basically works upon Euclidean Distances to compare the things and then predict the most likely one which is nearest to our testing point in a space..

# So this is the required description of whole project..
:))
