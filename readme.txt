o. Start 'Powershell' in Admin mode
o. How to deploy using 'gcloud'
   %> gcloud app deploy --project 4pics1w


Notes:
1. In 'app.yaml', remove 'application' and 'version' keywords.
2. Enable Cloud Build api
   https://console.developers.google.com/apis/api/cloudbuild.googleapis.com/overview?project=4pics1w


o. Powershell (run as adminstrator)
   o. Outside the project directory:
      % > python -m venv env
      % > env/Scipts/activate
   o. Inside project Directory
      - Deploy to server
        %> gcloud app deploy

      - Run locally
        %> pip install -r requirements.txt
        %> python .\main.py
