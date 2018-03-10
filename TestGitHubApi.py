import unittest
from unittest.mock import Mock, patch

from GitHubApi import getCommits, getRepos

class TestGitHubApi(unittest.TestCase):

    @patch('GitHubApi.requests.get')
    def testGetCommits(self, mockApiCall):
        aJson = [{'one'},{'two'},{'three'},{'four'},{'five'},{'six'}]
        mockApiCall.return_value = Mock(ok = True)
        mockApiCall.return_value.json.return_value = aJson
        self.assertEqual(getCommits('robjweiss', ['Triangle567']), [6], 'There are 6 commits in this repo as of 02.14.2018')

    @patch('GitHubApi.requests.get')
    def testGetRepos(self, mockApiCall):
        aJson = [{'name': 'GitHubApi567'},{'name': 'Movie-Data-Analytics'},{'name': 'Triangle567'}]
        mockApiCall.return_value = Mock(ok = True)
        mockApiCall.return_value.json.return_value = aJson
        self.assertEqual(getRepos('robjweiss'), ['GitHubApi567', 'Movie-Data-Analytics', 'Triangle567'], 'GitHubApi567, Movie-Data-Analytics, and Triangle567 are the repos as of 02.14.2018')

if __name__ == '__main__':
    unittest.main()
