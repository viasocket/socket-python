import json
import requests

class sokt:

	def __init__(self,auth) :
		
		self.baseUrl = "https://sokt.io" 
		self.authkey = auth
		self.headers = {
			'authkey': auth,
			'content-type': "application/json"
			}

	def flowURLBuilder(self,flow_id) :
		return self.baseUrl + '/' +str(flow_id)


	def invoke(self,flow_id,args) :
		url = self.flowURLBuilder(flow_id)
		payload = json.dumps(args)

		response = requests.post(url,data=payload,headers=self.headers, verify=False)
		return response.status_code

		