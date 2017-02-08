import requests
import json


class Use_github_API:
   """Class defines methods that use the GitHub API to grab details of my GitHub repos"""
    
   def __init__(self):
       """Constructor initialises the required attributes"""
       
       self.url = ''
       self.result = ''
       self.dict_keys = ''
       self.errorCode = ''
       
   def set_url(self,url):
       """Method sets the current request url"""
       
       self.url = url
       return self.url
       
       
   def get_repositories_list(self,url):
       """Method fetches list of my (depends on url given) github repos and prints it"""
       
       response = requests.get(url)
       
       self.errorCode = response.status_code
       if self.errorCode == 200:       
           self.result = json.loads(response.text)
           if type(self.result) == list:
      
               for key in range(len(self.result)):
                  if type(self.result[key]) == dict:
                      self.dict_keys = self.result[key].keys()
                      for dictkey in self.dict_keys:
                          if dictkey not in ['id','name','full_name','owner']:
                              continue
                          print('{0} : {1}'.format(dictkey,self.result[key][dictkey]),'\n')           
                      
               print("\n\n","#"*100,"\n\n")       
       else:
           return response.status_code
           
           
   def get_repository_language(self,url):
       """Method fetches the programming languages used in my repo files,
          given repo url"""
       
       response = requests.get(url)
       
       self.errorCode = response.status_code
       if self.errorCode == 200:       
           self.result = json.loads(response.text)
           return self.result           
       
       else:
           return self.errorCode 



   def get_repository_contributors(self,url):
       """Method fetches the contributors to the repo pointed to by url"""
          
       response = requests.get(url)
       
       self.errorCode = response.status_code
       if self.errorCode == 200:       
           self.result = json.loads(response.text)
           return self.result           
       
       else:
           return self.errorCode 
           
        
   def display_results(self,text):
      """Method displays results of API responses"""
          
      if type(text) == list:
      
          for key in range(len(text)):
              if type(text[key]) == dict:
                  self.dict_keys = text[key].keys()
                  for dictkey in self.dict_keys:
                      
                      print('{0} : {1}'.format(dictkey,text[key][dictkey]),'\n')
               
   
      if type(text) == dict:
          self.dict_keys = text.keys() 
          
          for key in self.dict_keys:
              print('{0} : {1}'.format(key,text[key]),'\n')

      if type(text) != list and type(text) != dict:
          
          if self.errorCode != 200:
          
              print("Request failed - error code: ",text)
          else:
              print(text)
          
      print("\n\n","#"*100,"\n\n")    

          
a = Use_github_API()

repo_list_url = a.set_url("https://api.github.com/users/bmulobi/repos")
repo_list = a.get_repositories_list(repo_list_url)
#a.display_results(repo_list)

repo_language_url = a.set_url("https://api.github.com/repos/bmulobi/bootcamp_day1/languages")
languages = a.get_repository_language(repo_language_url) 
a.display_results(languages)

repo_contributors_url = a.set_url("https://api.github.com/repos/bmulobi/bootcamp_day1/contributors")
contributors = a.get_repository_contributors(repo_contributors_url)
a.display_results(contributors)





      
