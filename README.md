# Integrated Health Care for Senior Citizens

A holistic health care system for senior citizens encompassing everything from diagnosis to delivery of medicines.

Work in progress22

## Hardware components

| Component | Quantity |
|-----------|----------|
| Arduino Nano R3 | 1 |
| Arduino UNO | 1 |
| Raspberry Pi 3 Model B | 1 |
| Raspberry Pi Camera Module | 1 |
| Maxim Integrated MAX30102 High-Sensitivity Pulse Oximeter and Heart-Rate Sensor for Wearable Health | 1 |
| 1800mAh Li-on Battery | 1 |
| TurtleBot 3 Burger | 1 |

## Story

1. Problem Statement:
   The average age of many parts of the world is increasing drastically. This phenomenon is observed in countries like Japan and Korea, where the cost of caring for elderly people is increasing. Many elderly people are being pushed into old age homes due to the lack of resources and not getting the care they need due to a shortage of nurses and doctors.

2. Solution:
   We came up with a solution to address the gaps in the entire structure. First, we are building a diagnostic device, i.e., a smartwatch that collects the people's vitals and transmits them to a local node that pre-processes the data and, if any abnormality is detected, alerts the doctor present. The data from the smartwatch is also collected periodically and stored in an online database that the doctor or relative can view regularly. We are also developing a website where the doctor can add the prescription for a patient and upload it. The pharmacist on-site will get the notification for this and place the medicines on a delivery bot which will then deliver the medicines to the designated patient.

## Code

### Steps to setup backend server
- Clone the repo by using the command ``git clone https://github.com/vinayakv22/Integrated_Healthcare_for_Senior_Citizens.git``
- cd into the medicare directory
- Do ```pipenv shell```
- ```pipenv install```
- Now makemigrations using ```python manage.py makemigrations```
- ```python manage.py migrate```
- Create SuperUser account for admin privileges ``` python manage.py createsuperuser```
- To run server ```python manage.py runserver```

## Team Members
- Vinayak Verma(Team Leader)
- Likhith Ayinala
- Adarsh Palaskar
- Bhavani Shankar Challa
- Joel Thomas
