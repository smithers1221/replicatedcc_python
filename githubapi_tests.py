import githubapi
import githubapi_membership
import githubapi_other
import unittest

class GithubAPIEndpointTestCase(unittest.TestCase):
	"""add docstring"""

	#testcase 1: confirm github is up and running
	def test_confirm_github(self):
		assert githubapi.confirm_github() == True

	#testcase 2: Check with valid org/username 
	def test_check_member_1(self):
		assert githubapi.check_member("replicatedcom", "marccampbell") == True

	#testcase 3: Check with valid org/invalid username
	def test_check_member_2(self):
		assert githubapi.check_member("replicatedcom", "smithers1221") == False

	#testcase 4: Check with invalid org/username
	def test_check_member_3(self):
	 	assert githubapi.check_member("timbercove", "marccampbell") == False

	#testcase 5: Check with valid comment, gfm mode, and repo context
	def test_create_gfm(self):
		self.assertTrue(githubapi.create_markdown("Hello world github/linguist#1 **cool**, and #1!", "gfm", "github/gollum" ))

	# #testcase 6: Check with valid comment, markdown mode, no repo context
	def test_create_markdown_without_context(self):
	 	self.assertTrue(githubapi.create_markdown("Hello world/linguist#1 *cool**, and #1!", "markdown", "" ))

	#testcase 7: Check with valid comment, markdown, unnecessary repo context
	def test_create_markdown_with_context(self):
		self.assertTrue(githubapi.create_markdown("Hello world github/linguist#1 **cool**, and #1!", "markdown", "github/gollum" ))

	#testcase 8: Check with valid comment, wrong mode, no context
	def test_create_markdown_with_emptystring(self):
		self.assertFalse(githubapi.create_markdown("Hello world github/linguist#1 **cool**, and #1!", "notmarkdown", "" ))

	# #testcase: Valid user/valid repo
	def test_get_repo_branches_all_valid(self):
		self.assertEqual(githubapi.get_repo_branches("smithers1221", "democrazee"), "142485d3e64ff741706623a7f918cdef03d409c7")

	# #testcase: Invalid user/valid repo or Valid user/Invalid Repo
	def test_get_repo_branches_invalid(self):
		self.assertEqual(githubapi.get_repo_branches("smithers1221", "fakerepo"), "Not Found")

	





if __name__ == '__main__':

	unittest.main()