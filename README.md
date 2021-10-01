# NYC Parking Violations

The Open Parking and Camera Violations data set consists of more than 62 million rows. For this analysis, over 1 million rows are processed to find meaningful patterns. Resources used include; AWS EC2, Docker, Elasticsearch, Kibana, Python and associated libraries such as Sodapy, Elasticsearch and Argparse.

## Folder Structure


+-- Dockerfile

+-- requirements.txt

+-- src/
+-- +-- main.py

+-- assets/
+-- +-- kibana_visualization1.png
+-- +-- kibana_visualization2.png
+-- +-- kibana_visualization3.png
+-- +-- kibana_visualization4.png
+-- +-- kibana_visualization5.png

+-- README

## How to build and the docker image

Step 1: Build the Docker image by running the below command on your instance. 

docker build -t bigdata1:1.0 project01/

Step 2: Open the project folder.

cd project01

Step 3: Run the container by entering the below command.

docker run -v ${PWD}:/app -e DATASET_ID="nc67-uf89" -e APP_TOKEN=“XXX” -e ES_HOST=“XXX” -e ES_USERNAME=“XXX” -e ES_PASSWORD=“XXX” bigdata1:1.0 --page_size=2 --num_pages=3 

## Some insights about parking violations happening

*School zone speed violation is the most common violation.

*Manhattan has the most parking violations compared to other neighborhoods.

*The most common fine amount is $115. 
