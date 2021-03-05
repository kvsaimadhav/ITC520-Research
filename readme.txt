Documentation of kaza2v-research

PART 1: Follow the below steps to change the present working directory to src directory after unzipping the kaza2v-research file.

1. Change your present working directory to kaza2v-research directory.

2. Now, change your present working directory to src directory.

PART 2: Follow the below steps for the working of the detection of DDOS attack source files.

1. First, install python and the dataset from the below links.
	Dataset: https://www.kaggle.com/devendra416/ddos-datasets?select=ddos_balanced
	Python: https://www.python.org/downloads/
 
2. You need to install Jupyter Notebook for source files to be run in your computer.
   Please, follow this link to download jupyter notebook: 
   https://test-jupyter.readthedocs.io/en/latest/install.html

3. Install numpy, pandas, scikit-learn and pickle packages for popping up of no errors in the code. Do not skip this step. 
	As it is important for the files to run properly, we need to install these packages before going into step 7. 

4. Type the command in the command prompt: jupyter notebook 

5. You will see a chrome window opening automatically and go to the kaza2v-research folder and follow steps of part-1.

6. You need to run the commands written in the .ipynb files. There are 3 files which are self descriptive. 
	Tutorial for running commands can be followed in the attached below link:  
	https://www.codecademy.com/articles/how-to-use-jupyter-notebooks

7. Files to look into till Midterm Progress are src folder, week12-brief.ipynb, week34-training.ipynb and week56-analysis.ipynb.

8. You can look at the documentation folder inside the kaza2v-research folder for more details on the results till midterm progress.

PART 3: Follow the below steps for the working of the website in mitigating the DDOS attack project files.

1. Now, change the present working directory to project folder which is inside of the src folder.

2. Install Django pakcage for popping up no errors in the code.

3. Type the command in the command prompt:  python3 manage.py migrate

4. Type the command in the command prompt: python3 manage.py runserver

5. Now, open the below link in chrome window to access the website.
	http://127.0.0.1:8000/forms_project/

6. The website will ask you to enter the personal details like First Name and Last Name. After you enter the details, 
	the steps are self-explanatory to come to the final page. 

Note: This website considers simualted results of the test dataset from the original dataset, and ML model .sav is used in the website to predict whether
the local user is good traffic or bad traffic based on the predictors explained in the research paper. And if the user is good, then we allow the user to 
go the final page of the website.

	