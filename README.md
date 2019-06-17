# safe-driver-sweet-lover

## Proof of Concept

I joined too late and with multiple projects at the moment. So I failed to train neural networks in time for this challenge. I intend to continue working on this repo during my pockets of free time in between my commitments. For now, I will just outline the methodology of my proposed solution for today's submission. :) 

I chose to work on Safety data because of my geospatial background and my experience as a Grab rider whenever I am in Metro Manila. 

I experienced one dangerous driving incident from a booking a few weeks ago and I noticed that the support feedback from Grab happened 3 days after my ride. It was excellent feedback from Grab, but it was sent too late. 

I realized that the data model solution is just one part of the solution. There is a data engineering component to my proposal that collects with a closer feedback time from the customer using AWS technologies. (My background is also now more on systems engineering than formal data science, so perhaps this explains my approach to this problem.)

## Proposed Methodology

The solution I propose is two-pronged: the data model solution and the cloud-based data engineering solution. 

### Data Model Solution

#### 1. Pre-processing the features before feature engineering
a. The GPS bearing needs to be converted into absolute coordinate system reference to help detect anomalies better. (Discussion on the concept here: https://pro.arcgis.com/en/pro-app/help/mapping/properties/coordinate-systems-and-projections.htm)
b. The features of accelerometer and gyrometer need to be linked with the known road roughness of the road being traversed. The DPWH National Road Roughness Survey data (https://www.carmudi.com.ph/journal/dpwh-conducts-national-road-roughness-survey/), for example, will help assign weights to rough roads so that jerking movements from the accel and gyro readings will not be introduced with noise from roads with inherent roughness and require jerking movements during the navigation of driver and customer. 
c. Greater weight must be assigned to trips with longer time in seconds or sequences (this is from a related lit outlined in the ipynb file)

#### 2. Test different models highlighting different features from raw dataset 
Researching Grab's publications, rules-based algorithms have been implemented previously (https://www.grab.com/sg/blog/grabs-telematics-show-safer-more-comfortable-rides-in-a-year/) with positive responses. I assume there is a rule-based algorithm that already exists. 

Here are the models I intend to test out and the features that will be highlighted in them: 
* 
* 




### Data Engineering Solution
From what I noticed during my Grab rides, Grab issues a 60 km/hour limit to its drivers and that is their preventive dangerous driving measure (I also interviewed a Grab driver and he confirmed this to me). 

I introduce or suggest the AWS Feedback Loop as a way to get information from customers during the ride than after. 

I propose that when realtime telematics data from Grab (presumably using AWS Kinesis Fire Hose) enters the Grab server, derivatives or the rates of change in the y accelerometer and Z gyroscope readings can be calculated in 2-3 minute intervals and stored in an S3 bucket. 

It will trigger an AWS Lambda feature that once there is an unusual spike detected from that calculation stored in S3, so the AWS system will then send a notification to the customer asking him or her: "Hello, we detected an unusual spike in movement from your booking. Are you comfortable with your current Grab ride? Please reply Yes or No to confirm."

This message will be sent back and encoded as an additional safety marker from the customer during the ride itself. Grab will no longer have to wait until after the ride is over to get realtime feedback on their data streams and this improves customer service. 


## Timeline
I won't be able to finish this model submission in time for June 17, but I intend to work on the sample dataset until October this year. =) 
