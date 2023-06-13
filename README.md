# clairvoyant

#Setup

Clone the repo in the local folder

**git clone** <repo-name>
  
 After installing Docker 
 **docker compose build** - to build the image
  **docker compose up** - to start the container and the app
  
  **OR**
run the bash script
  ./run.sh
  
  ------DB models created 
  
      Tenant , ProjectMetadata 
  
  To run unittest cases, please keep the mongo db instance running in local machine, connected to local host
  sample connection string **mongodb://localhost:27017**
  
  -------The data is the famous Boston Housing data, found in housing.csv
  
  -------Generated model, Linear Regression
  
  -------Model saved to S3 (bucket name: codingtaskclair) , the connection credentials are currently open on s3 Module. Please change the credentials if testing.
  
  
  
  
