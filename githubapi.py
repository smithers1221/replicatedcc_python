
import requests
import json
import urllib2

BASE_URL = "https://api.github.com"

def confirm_github():
	"""Confirm Github is up and running"""
	url = BASE_URL
	r = requests.get(url)

	if r.status_code == 200:
		# print "status code:", r.status_code, "(github is working)"
		return True
	else:
		# print "github is down"
		return False



def check_member(org_name, member_name):
	"""Check if a user is a member of a given org"""

	#Based on validity of either org or member, API response has two status responses - 204 or 404
	url = BASE_URL+"/orgs/%s/public_members/%s" % (org_name, member_name)
	
	r = requests.get(url)

	if r.status_code == 204:
		# print member_name, "is a member of", org_name
		return True

	elif r.status_code == 404:
		# print member_name, "is not a member of", org_name
		return False



def create_markdown(comment, mode, repo_context):
	"""Validating whether markdown has been rendered"""

	#Added a try-except to account for '400: Bad Reqeust' when incorrect POST is made
	try:
		comment_data = {
			"text": "%s" % comment, 
			"mode": "%s" % mode,
			"context": "%s" % repo_context
		}

		req = urllib2.Request(BASE_URL+"/markdown")
		req.add_header('Content-Type', 'application/json')

		r = urllib2.urlopen(req, json.dumps(comment_data))

		
		if r.getcode() == 200:
			#print "markdown doc rendered"
			return True

	except:
		return False



def get_repo_branches(owner, repo):
	"""Return branch info for a given repo by a owner"""
	#Endpoint delivers error message if either owner or repo provided is invalid
	try:
		url = BASE_URL+"/repos/%s/%s/branches" % (owner, repo)
		r = requests.get(url)

		repo_branches = r.json()

		#print "branches: ", repo_branches
		#print repo_branches["message"]
		
		return repo_branches[0]["commit"]["sha"]

	except:
		return repo_branches["message"]











