# Cherry Leaf Mildew Detection Project

This project employs machine learning to train a model to predict if a cherry tree leaf is infected or not.

## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).
* The dataset contains over 4, 000 images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Hypothesis and Hypothesis Validation

### Hypothesis 1
There is a visible difference between infected and healthy cherry tree leaves due to the presence of a powdery mildew.

### Hypothesis 1 Validation: 
Conduct a study to visually differentiate a healthy leaf from an infected one. This will be done
with an average image study.


### Hypothesis 2
It is possible to train a model to predict, with at least **97%** accuracy, if an image of a cherry tree leaf is infected with powdery mildew or not.

### Hypothesis 2 Validation:
The hypothesis will be tested by training a model on a train and a test set of images and by calculating the accuracy with a validation set of images.


## The rationale to map the business requirements to the Data Visualisations and ML tasks

The CRISP-DM workflow was utilised throughout this project to achieve satisfactory results for the two business requirements.

### Business Requirement 1
- An average image study was selected for this business requirement as it allows the client to see what an average healthy leaf looks like and what an average infected leaf looks like.
- An image montage was created to allow the user peruse some examples of healthy and infected images.


### Business Requirement 2
- A machnine learning model was selected to address the second business requirement. A binary classifier was used to determine if an image from the dataset was healthy or infected.
- An option to upload a new cherry leave image is also available to the user to allow them to use the trained model on unseen images and download a report afterwards.

## Machine Learning Business Case
- As the project requires prediction, an ML binary classifcation model was chosen to be trained.
- As the task is binary classification, a supervised, 2-class, single-label model with an Adagrad optimizer was chosen.
- The model was required to produce predicition accuracy of at least 97%. This was achieved with the selected model.
- By using this trained model, the workers at Farmy & Foods can take action on treating or removing any infected cherry trees in order to protect their orchard from further infection and potential revenue reductions.


## Dashboard Design
Streamlit Multipage was used to create a 5 page dashboard.

* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.




## Unfixed Bugs
* You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.



## Acknowledgements (optional)
* Thank the people that provided support throughout this project.
