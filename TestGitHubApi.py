import unittest

from GitHubApi import getCommits, getRepos

class TestGitHubApi(unittest.TestCase):

    def testGetCommits(self):
        self.assertEqual(getCommits('robjweiss', ['Triangle567']), [6], 'There are 6 commits in this repo as of 02.14.2018')

    def testGetRepos(self):
        self.assertEqual(getRepos('robjweiss'), ['GitHubApi567', 'Movie-Data-Analytics', 'Triangle567'], 'GitHubApi567, Movie-Data-Analytics, and Triangle567 are the repos as of 02.14.2018')

if __name__ == '__main__':
    unittest.main()
