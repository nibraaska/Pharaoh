# Pharoah 

This project is meant for learning web development and providing the Collage Magazine at MTSU with a website. The frontend of the website will be made with React and the back end will be handled with Django for the time being. 

To run the website on a local server:
1. Install anaconda (optional)
2. Create an environment (optional)
3. Install python packages (optional)
4. Run the script ```run``` on a Linux machine with ```./run```.
    - The script does the following to make working with the website easier:
       - Install all packages with ```npm install```
       - Use get requests to get all the information needed for the database
       - Build the database
       - Seed the database
       - Create a superuser
       - Run npm for debugging
       - Start the Diango server
    - The following bash script get everything up and running
       - 
          #!/bin/bash
          
          npm install
          cd seedDataParse
          python parse_request.py
          cd ..
          mkdir collagewebsite/media
          cd seedDataParse
          mv -f issues/ ../collagewebsite/media/
          mv collage_parsed.json issues.json
          mv issues.json ../collagewebsite/issues/fixtures
          cd ..
          python collagewebsite/manage.py makemigrations
          python collagewebsite/manage.py migrate
          python collagewebsite/manage.py loaddata issues
          python collagewebsite/manage.py createsuperuser
          npm run dev &
          python collagewebsite/manage.py runserver
         
