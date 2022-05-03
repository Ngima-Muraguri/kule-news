import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("abc-news",'ABC NEWS',"Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.","https://abcnews.go.com","general")
    def tearDown(self):
        Source.clear_source()      
    def test_init(self):
        '''
        This will test if the use has been properly initialized
        '''
        self.assertEqual(self.new_source,"abc-news")
        self.assertEqual(self.new_source,"ABC NEWS")
        self.assertEqual(self.new_source,"Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.")
        self.assertEqual(self.new_source,"https://abcnews.go.com")
        self.assertEqual(self.new_source,"general")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
