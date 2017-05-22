# __Replicated Coding Challenge Submission__

## __Why Python?__
 
After correctly setting up Docker, my initial plan was to get up to speed on Golang, Ginkgo and Gomega - and complete the assignment accordingly.  I went through the resources provided as well as additional sites trying to learn the correct syntax and structure for the testing tools. 

**Ultimately, after some time spent not being able to get the markdown and membership tests to work, I felt that learning a new language and testing framework was pulling me away from the core objectives of this exercise:**  

* Correctness: Do your tests compile and run? Do they actually make calls to the API and verify results?

* Code Quality: Is your code maintainable, easy to understand, and conducive for future reuse or expansion?
Quality Focused: Does your choice of test case scenarios provide adequate, given the limits, confidence in the quality of the GitHub API endpoints tested?

* Communication: Are you able to defend why you picked your test case scenarios and explain what they do in your README and through other forms of communication?

To meet the goals of this exercise, I run my tests using Python and unit tests.  

#### *Directory contents: Functions file, test file and requirements.*  

## __METHODOLOGY__

In total, I tested 3 different endpoints that provided information on the following:
-Membership
-Markdown
-Branches 

### Membership:
Passing in the org name and user, the API returned a 204 or 404 status on whether or not the user was a member of the given org.  There were several scenarios to test:

		Basecase: Given the correct org and user, does the API confirm membership?

		Invalid/Incorrect org with user: Is the API correctly checking membership against a given org and not just across all orgs?

		Org with invalid/incorrect user: Given a valid org, is the API correctly checking against its members for the given user?  

### Markdown:
This API had multiple inputs - comments(to be delivered in json), mode, and repo context. 

		Comments
		The API was robust in handling comments provided as JSON.  Incorrect markdown syntax did not result in errors or inability to render the markdown. 

		Mode
		Entering anything other than "gfm" or "markdown" resulted in a failure.

		Repo Context
		This seemed to have no bearing on the output, API seemed to accept any string provided.  

### Branches:
The list_branches endpoint delivered an error if either owner or repo was invalid, or did not match.  As a result, I tested two scenarios - valid owner/valid repo and valid owner/invalid repo. 

		Valid State
		Here I not only wanted to confirm that a json output was returned, but that it was provided correct branch info.  To validate this, I set up the success function to return the sha of the branch.  In my tests, I could then assess whether the 'sha' matched the expected 'sha'value

		Invalid State
		The API delivers a standard error message stating 'Not Found'.  Using a try and except, the function returned the 'Not Found' when given any invalid inputs.  My tests could then assess for whether that message was returned for invalid inputs.  

## __RUNNING THE FILE__

Install the dependencies:
```python
pip install -r requirements.txt
```

Run the tests:
```python
python githubapi_tests.py
```

![Thank You!](/thank_you.gif)



