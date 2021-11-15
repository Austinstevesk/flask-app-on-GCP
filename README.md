# flask-app-on-GCP  

# Requirements  
-Python  
-pip  
-git  
-Docker  
-Text editor of your choice  

  
# To Do 
# On the Cloud 
- Create a Google Cloud Platform Account  
- Create a GCP Project  
- Create a cluster (define it as autopilot)  
- Create a repository on artifact registry
- Create a service account, don't give it the roles yet  
- Copy the service account email  
- Get to the repository created and check the checkbox on your left  
- Navigate to permissions and click add principal  
- Paste the service account email on new principal and select role as artifact ```registry writer``` -> Least Privilege  
  
# On your machine  
- Clone this repository  
- Get to the workflows part and change the following  
    - ```PROJECT_ID``` to match your name  
    - ```IMAGE_REPO``` to match your repo name on the artifact registry  
    - The ```us-central1-docker.pkg.dev``` to match your region name eg if your region is us-east1,
    you should have us-east1-docker.pkg.dev   
- Be sure to delete the .git file downloaded so that you are not linked to my github  
  
# On github  
- Create a repo and name it anywhat you want  
- Configure and link it with your local directory using "git remote add origin"   
- Create a secret on setting and paste the content of the Key you downloaded earlier  
- Push the code from you local machine  
  
# Deployment  
- Get to the artifact registry and navigate to the latest image  
- Click on the image and at the top click deploy  
- Use the defaults including the selected cluster and deploy  
- Expose the ports to match the internal port (port 80, Target port 5000)  
- Click the external IP address given and there is your application  