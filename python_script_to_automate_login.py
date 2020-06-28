import json 
import requests
import pprint
import datetime
  
# Opening JSON file 
headers={
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
def login():
	#starting time 
	time_start = datetime.datetime.utcnow()
	
	# Opening JSON file
	f = open('login.json',) 
	  
	# returns JSON object as a dictionary 
	data = json.load(f) 
	
	#initializing the success parameter
	success=bool  
	# Iterating through the json list 
	
	with requests.Session() as s:
		#creating the object of url 
		url="https://www.propertyguideline.com/login" 
		
		#sending the data to the website
		req=s.post(url,data=data,headers=headers) 
		
		#end time
		time_end=datetime.datetime.utcnow()
		#checking for success 
		if(req.status_code==200):
			success=True
		else:
			success=False
		if(req.status_code==200):
			detail='the user logedin successfully'
		else:
			detail=str(req.status_code)
		#creating the dictonary of the result
		result = {
			"websitename": "https://www.propertyguideline.com",
        	"success": success,
        	"start_time": str(time_start),
        	"end_time": str(time_end),
        	"usage_time": str(time_end - time_start),
        	"detail": detail,
		}

		#converting the dict to json
		result_json=json.dumps(result)
		
		#initilizing the pretty print module
		pp = pprint.PrettyPrinter(indent=4, width=40, compact=False)
		
		#printing the json data
		pp.pprint(result_json)
	
	# Closing file 
	f.close() 



def register():
	
	# initilizing the start time
	time_start = datetime.datetime.utcnow()
	
	# Opening JSON file 
	f=open('register.json')
	
	#return a object as a dictionary
	data = json.load(f)
	
	#initilizing the success parameter
	success=bool
	
	#itterate through the json list
	with  requests.session() as s:
		#creating the request url 
		url="https://www.propertyguideline.com/%E0%B8%AA%E0%B8%A1%E0%B8%B1%E0%B8%84%E0%B8%A3%E0%B8%AA%E0%B8%A1%E0%B8%B2%E0%B8%8A%E0%B8%B4%E0%B8%81"
		#sending the data to the website
		req=s.post(url,data=data,headers=headers)
		#end time 
		time_end=datetime.datetime.utcnow()
		#checking for success 
		if(req.status_code==200):
			success=True
		else:
			success=False
		if(req.status_code==200):
			detail='the user registerd successfully'
		else:
			detail=str(req.status_code)
		#result dict
		result = {
			"websitename": "https://www.propertyguideline.com",
        	"success": success,
        	"start_time": str(time_start),
        	"end_time": str(time_end),
        	"usage_time": str(time_end - time_start),
        	"detail": detail,
		}

		#converting dict to json
		result_json=json.dumps(result)
		#initilizing the pretty print module
		pp = pprint.PrettyPrinter(indent=4, width=80, compact=False)
		#printing the json data
		pp.pprint(result_json)
	# Closing file 
	f.close() 
		


def main():
	num=int(input("press 1 for login from json file \n press 2 for register from json file :   "))
	if(num==1):
		login()
	elif (num==2):
		register()
	else:
		print("please enter the valid choice")



if __name__ == "__main__":
    main()