<p align="center">
<a href="https://github.com/PhinanceScientist"><img src = "https://raw.githubusercontent.com/PhinanceScientist/PhinanceScientist/main/assets/ln-logo.png" width = 100> </a>
</p>
<h1 align=center><font size = 5>Scikit-Learn excercises</font></h1>
<br>

# Introduction
<br>
This repository is a backup of the excercises done on the <a href="https://platzi.com/clases/scikitlearn-ml/">Scikiti-Learn course</a> in <a href="https://platzi.com/">Platzi</a>.<br>
For this project I will be using a virutal environment as a good practice for development.<br>
Please follow the instructions below for a proper setup where I'll include the libraries and the steps required.<br>
Special thanks to Profesor <a href="https://www.linkedin.com/in/arielortiz/">Ariel Ortiz</a> for this amazing course.

***

## Virtual environment setup for Windows using cmd
<br>
   <li> <b>Be sure Python is installed on your computer</b><br></li>
   <li> <b>Create a clean folder where the project will rest:</b>   Create a new empty folder for the project<br></li>
   <li> <b>Create or copy a "get-pip.py" file on the root folder: </b>You can find the file <a href="https://bootstrap.pypa.io/get-pip.py">here</a>, just right click it and choose the option "save as".<br></li>
   <li> <b>Run the get-pip.py using python:</b>   Once your "get-pip.py" file is on your project's folder run it with your terminal using the command <pre><code>python get-pip.py</code></pre></li>

   <li> <b>Install your virtual environment:</b>   After installing your pip module proceed to install your virtual environment with the command <pre><code>python -m pip install virtualenv</code></pre></li>
   <li> <b>Create and name the virtual environment:</b> For this example we will name the environment "venv".<br>  Create your virtual environment and name it using the command: <pre><code>python -m virtualenv venv</code></pre></li>
  A folder with the name of your environment will be automaticaly created.
   <li> <b>Run your environment:</b> Run your environment with the "activeate.bat" located on the Scripts folder inside your environment named folder, you can use the following the command:<br>  <pre><code>>venv\Scripts\activate.bat</code></pre></li>
   <li> <b>Verify your environment is running:</b> To verify if  your environment is running and you are actually working on it, please check your terminal displays the name of the environment before your current location on the project directory.<br> Example:<br>  <pre><code>(venv) D:\documentos\scikit-learn\</code></pre></li>




***
# Libraries<br>
  
   <li> <b>joblib:</b>   1.0.1<br></li>
   <li> <b>matplotlib:</b> 3.4.2 <br></li>
   <li> <b>numpy </b> 1.21.0<br></li>
   <li> <b>pandas:</b> 1.3.0<br></li>   
   <li> <b>scikit-learn:</b> 0.24.2<br></li>
   <li> <b>scipy:</b> 1.7.0 <br></li>
  <br>
  You can install each one using the command:
  <pre><code>python -m pip install pandas</code></pre></li>
  or just install everything at once using the "requirements.txt" file
  <pre><code>pip install -r requirements.txt</code></pre></li>

***
 # Data<br>


## <a href="https://www.kaggle.com/fivethirtyeight/the-ultimate-halloween-candy-power-ranking">The Ultimate Halloween Candy Power Ranking</a>
What’s the best (or at least the most popular) Halloween candy? That was the question this dataset was collected to answer. Data was collected by creating a website where participants were shown presenting two fun-sized candies and asked to click on the one they would prefer to receive. In total, more than 269 thousand votes were collected from 8,371 different IP addresses. (FiveThirtyEight, 2017) 

Don't miss the opportunity of reading about the article and watch a fun video of the experiment <a href="https://fivethirtyeight.com/videos/the-ultimate-halloween-candy-power-ranking/">here</a>

## <a href="https://www.kaggle.com/johnsmith88/heart-disease-dataset">Heart Disease Dataset</a>
This data set dates from 1988 and consists of four databases: Cleveland, Hungary, Switzerland, and Long Beach V. It contains 76 attributes, including the predicted attribute, but all published experiments refer to using a subset of 14 of them. The "target" field refers to the presence of heart disease in the patient. It is integer valued 0 = no disease and 1 = diseaset. (David Lapp, 2019)

## <a href="https://www.kaggle.com/johnsmith88/heart-disease-dataset">World Happiness Report</a>
The World Happiness Report is a landmark survey of the state of global happiness. The first report was published in 2012, the second in 2013, the third in 2015, and the fourth in the 2016. (Update) The World Happiness 2017, which ranks 155 countries by their happiness levels, was released at the United Nations at an event celebrating International Day of Happiness on March 20th. The report continues to gain global recognition as governments, organizations and civil society increasingly use happiness indicators to inform their policy-making decisions. Leading experts across fields – economics, psychology, survey analysis, national statistics, health, public policy and more – describe how measurements of well-being can be used effectively to assess the progress of nations. The reports review the state of happiness in the world today and show how the new science of happiness explains personal and national variations in happiness. (Sustainable Development Solutions Network, 2019)

***
 # Scikit-Learn<br>
 Scikit-learn is a free machine learning library for Python. It features various algorithms like support vector machine, random forests, and k-neighbours, and it also supports Python numerical and scientific libraries like NumPy and SciPy. (DATAQUEST, 2018)
***
 # Conclussion<br>
 Scikit-Learn is a simple yet powerfull tool that makes Data Science far easy for people. Using this library can help you with data modeling in really simple ways, however, if you wish to fully understand your data, Statistics and Calculus are knowledge that will boost your work. <br>
 In conclusion, doing excercises using real datasets will help to understand the possible applications on a professional basis, still, it is absolutely necessary to understand the implication of the organization and the data to make the most of it for data driven decisions.

 
 ## Bibliografy
https://scikit-learn.org/<br>
https://www.dataquest.io/blog/sci-kit-learn-tutorial/#:~:text=Scikit%2Dlearn%20is%20a%20free,libraries%20like%20NumPy%20and%20SciPy%20. <br>
https://medium.com/@jtpaasch/the-right-way-to-use-virtual-environments-1bc255a0cba7 <br>

***
 Made by <a href='https://www.linkedin.com/in/novelo-luis/'> Luis Novelo </a>