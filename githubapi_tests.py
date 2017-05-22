import githubapi
import unittest

class GithubAPIEndpointTestCase(unittest.TestCase):
	"""add docstring"""

	#testcase 1: Confirm github API is up and running
	def test_confirm_github(self):
		self.assertTrue(githubapi.confirm_github())

    
    #Membership tests

	#testcase 2: Check public membership with valid org/username
	def test_check_member_1(self):
		self.assertTrue(githubapi.check_member("replicatedcom", "marccampbell"))

	#testcase 3: Check public membership failure with valid org/invalid username to make sure username is used
	def test_check_member_2(self):
		self.assertFalse(githubapi.check_member("replicatedcom", "smit1221"))

	#testcase 4: Check public membership failure with invalids org/valid username to make sure org name is used
	def test_check_member_3(self):
	 	self.assertFalse(githubapi.check_member("timbercove", "marccampbell"))

    
    #Markdown tests

	#testcase 5: Check Markdown API with valid comment, gfm mode, and repo context
	def test_create_gfm(self):
		self.assertTrue(githubapi.create_markdown("Hello world github/linguist#1 **cool**, and #1!", "gfm", "github/gollum" ))

	#testcase 6: Check Markdown API with valid comment, markdown mode, no repo context (also passed some slightly incorrect markdown to show that the API ignores that)
	def test_create_markdown_without_context(self):
	 	self.assertTrue(githubapi.create_markdown("Hello world/linguist#1 *cool**, and #1!", "markdown", "" ))

	#testcase 7: Check Markdown API with evalid comment, markdown, unnecessary repo context
	def test_create_markdown_with_context(self):
		self.assertTrue(githubapi.create_markdown("Hello world github/linguist#1 **cool**, and #1!", "markdown", "github/gollum" ))

	#testcase 8: Check Markdown API failure with valid comment, incorrect mode option, no context
	def test_create_markdown_with_emptystring(self):
		self.assertFalse(githubapi.create_markdown("Hello world github/linguist#1 **cool**, and #1!", "notmarkdown", "" ))

    
    #Branches tests

	#testcase 9: Check Branches API by verifying the Sha returned from a Valid user a/valid repo
	def test_get_repo_branches_all_valid(self):
		self.assertEqual(githubapi.get_repo_branches("smithers1221", "democrazee"), "142485d3e64ff741706623a7f918cdef03d409c7")

	#testcase: Checek Branches API response with an Invalid user/valid repo or Valid user/Invalid Repo
	def test_get_repo_branches_invalid(self):
		self.assertEqual(githubapi.get_repo_branches("smithers1221", "fakerepo"), "Not Found")





if __name__ == '__main__':

	unittest.main()




