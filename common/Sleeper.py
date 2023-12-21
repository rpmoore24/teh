import json, os, requests

## Class used to make API calls
class Sleeper():
   
   ## Download data if it does not exist
   ## and then read it
   # @param file      The str for file to write to
   # @param request   The str for request
   def download(self, file, request):
      # Write data to file if does not exist
      if not os.path.exists(file):
         r = requests.get(request)
         with open(file, 'w') as f:
            json.dump(r.json(), f)
            
      # Read data and store to object
      with open(file, 'r') as f:
         r = json.load(f)
         # Create attribute for each key if dictionary
         if isinstance(r, dict):
            for name, value in r.items():
               setattr(self, name, value)
         # Create data attribute for lists
         elif isinstance(r, list):
            setattr(self, 'data', r)