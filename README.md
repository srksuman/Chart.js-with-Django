# Chart.js with Django 
Chart.js is a cool open source JavaScript library that helps you render HTML5 charts.
# Project Demo
![h](https://user-images.githubusercontent.com/67781881/127086841-c00cdb4d-942e-4a60-b46b-8494946e0c94.gif)
# Installation
Add the Chart.js lib to your HTML page:
<!--Chart js-->
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.min.js" integrity="sha256-Uv9BNBucvCPipKQ2NS9wYpJmi8DTOEfTA/nH2aoJALw=" crossorigin="anonymous"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.min.css" integrity="sha256-aa0xaJgmK/X74WM224KMQeNQC2xYKwlAt08oZqjeF0E="crossorigin="anonymous"/> <br>
You can also download it from <a href="https://www.chartjs.org/">Chart.js</a> official website and use it locally, or you can use it from a CDN using the URL above.

# Scenario
How to transform database data from so it can fit in a bar chart / line chart / etc.
### Step 1:
models.py
![image](https://user-images.githubusercontent.com/67781881/127086811-e3dbeec2-0413-4f76-a785-f86011b977d4.png)

After creating model make sure to:- <br>
1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py createsuperuser (optional)
### Step 2:
admin.py
![image](https://user-images.githubusercontent.com/67781881/127087018-49da8e2f-ee14-40bc-b7b5-feec1d09c6aa.png)

### Step 3:
forms.py
![image](https://user-images.githubusercontent.com/67781881/127087068-3863cf78-ed54-411c-943c-b9caead61524.png)

### Step 4:
urls.py
![image](https://user-images.githubusercontent.com/67781881/127087143-c21d1239-422d-4a66-98d7-9ed0c1c23343.png)

### Step 6:
views.py
![image](https://user-images.githubusercontent.com/67781881/127087300-3cdc7d01-531c-4c4f-87a3-58f08148b131.png)
![image](https://user-images.githubusercontent.com/67781881/127087327-2d114d35-4ce2-4099-9ff3-14018fd7aaaf.png)

### Step 7:
create templates folder 
![image](https://user-images.githubusercontent.com/67781881/127087212-4fa317f8-0c57-4874-94c9-c9383c143768.png)

## Technologies Used
* Python Django
* CSS, Bootstrap
* HTML
* JS
