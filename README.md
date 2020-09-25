# Face Mask Detection
<p>Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. 
The COVID-19 virus spreads primarily through droplets of saliva or discharge from the nose when an infected person coughs or sneezes.
At this time, there are no specific vaccines or treatments for COVID-19.</p>
<p align="center">
<img src="https://www.who.int/images/default-source/health-topics/coronavirus/gettyimages-1203376093.tmb-1024v.png?Culture=en&sfvrsn=6e0c1bc7_6%201024w" width=500 height=300>
</p>
<p> To stop the spread of corona virus, social distancing and observing hygiene standards like compulsory wearing of mask, use of hand gloves, face shield, use of sanitizer and washing hands frequently is very important.</p>
<p> This project focuses on detecting face mask using OpenCV and python.</p>

**There are two main steps involved in this project-**
1. Identifying human face and mouth in each frame.
2. Checking if the person is wearing a mask.

# Requirements
1. OpenCV
2. Numpy
3. HaarCascade files for mouth and face

# Truth Table

| Face (gray)  |  Face (black & white)  | Mouth | Mask |
|--------------|:----------------------:|------:|-----:|
| 0 |  0 | NA | No face found |
| 0 |  1 | NA | White mask detected |
| 1 | 0 or >1 | 0 | Mask Found |
| 1 | 0 or >1 | 1 | No mask found |   




