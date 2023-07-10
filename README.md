# FileUploadNull
This repository demonstrates file/resume upload functionality

### HOW-TO (fileUploadFunctionality)
1. First login using localhost:port/admin
2. Create a user
3. Go to localhost:port/fileUploadFunctionality/main

### HOW-TO (POST/GET API Related development)
1. Run the server
2. I've created models for two objects i.e., Jobs and Person    
    1. Jobs URL: `/api/v1/jobs`
    2. Person URL: `/api/v1/person`
3. Now when you'll get an interface to make a post/get request, here    
you can do following things :    
    1. Make a POST request to Jobs/Person object with their relevant fields
    2. GET data based on specific ids, for example:    
       `/api/v1/jobs/{id}`: Return the Jobs data belong to id 1    
       `/api/v1/person/{id}`: Does the same thing as above    
       `/api/v1/person/{id}/jobs`: Return the Jobs applied by the person with specific "id" (this functionality is available for person only)    
       `/api/v1/jobs?company="xyz"&location="xyz"`: Get data of jobs based on company and location filter.    
