-# Udacity Data scientist Nanodegree 
This repository consists of Udacity Nano-degree Data Scientist projects and notebook files.

## List of Projects

## 1. Data Science Blog Post
In this project, I have done the analysis of [Stack Overflow Developer Survey, 2019](https://www.kaggle.com/stackoverflow/so-survey-2017/data). You can find my Medium Blog Post in this [link](xyz.com) for the full report. The jupyter notebook for this project is located in folder `Blog-post`.

**Tools Used**: Matplotlib, numpy, pandas, sklearn


## 2. Disaster Response Pipeline Project

## 3. Data Scientist Capstone Project

**Overview**<br>
The objective of this project is to classify as an image of the dog into its 133 dog breed categories and if in case if it detects humans, it maps to what dog breed the detected human look like.

**Libraries**<br>
- Keras
- OpenCV
- Matplotlib
- Numpy

**Files**<br>
- dog_app.ipynb: jupyter Notebook having all the algorithms and the model implementation
- dog_app.html: A copy of dog_app.ipynb in html format.
- Haarcascades folder: Xml file used in open cv for finding the human face in the image
- images: sample images given in the udacity dataset

**Contents**<br>
The workflow is broken down as follows:<br>
Step 0: Import Datasets<br>
Step 1: Detect Humans<br>
Step 2: Detect Dogs<br>
Step 3: Create a CNN to Classify Dog Breeds (from Scratch)<br>
Step 4: Use a CNN to Classify Dog Breeds (using Transfer Learning)<br>
Step 5: Create a CNN to Classify Dog Breeds (using Transfer Learning)<br>
Step 6: Write your Algorithm<br>
Step 7: Test Your Algorithm<br>

**Results**<br>
I have used the Inception V3 model as this works well with this image classification as it is trained on millions of images and it is a very good feature extractor and in general it gives very good results in less time. The test accuracy obtained was 0.8 with 20 epoch.
