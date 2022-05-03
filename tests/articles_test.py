import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Articles("Alfred Liu","Canada Study Says Rogers Shaw Bid Must Hinge on Unit Sale: Globe - BloombergQuint","Canada Study Says Rogers Shaw Bid Must Hinge on Unit Sale: Globe","https://www.bloombergquint.com/onweb/canada-study-says-rogers-shaw-bid-must-hinge-on-unit-sale-globe","https://gumlet.assettype.com/bloombergquint%2F2018-08%2F3a8e2237-2edb-4494-bcf2-231993fb6108%2FBLOOMBERG_LOGO.png?rect=0%2C56%2C1920%2C1008&w=1200&auto=format%2Ccompress&ogImage=true","2022-02-26T10:04:24Z", "(Bloomberg) -- A Canadian House of Commons committee has recommended the government withhold approval for Rogers Communications Inc.s planned takeover of Shaw Communications Inc. unless it disposes o… [+981 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))
        
    def tearDown(self):
        Articles.clear_articles()
        
    def test_init(self):
        '''
        This will test if the use has been properly initialized
        '''
        self.assertEqual(self.new_articles.author,'Alfred Liu')
        self.assertEqual(self.new_articles.title,'Canada Study Says Rogers Shaw Bid Must Hinge on Unit Sale: Globe - BloombergQuint')
        self.assertEqual(self.new_articles.description, "Canada Study Says Rogers Shaw Bid Must Hinge on Unit Sale: Globe ")
        self.assertEqual(self.new_articles.url,"https://www.bloombergquint.com/onweb/canada-study-says-rogers-shaw-bid-must-hinge-on-unit-sale-globe")
        self.assertEqual(self.new_articles.urlToImage,"https://gumlet.assettype.com/bloombergquint%2F2018-08%2F3a8e2237-2edb-4494-bcf2-231993fb6108%2FBLOOMBERG_LOGO.png?rect=0%2C56%2C1920%2C1008&w=1200&auto=format%2Ccompress&ogImage=true")
        self.assertEqual(self.new_articles.publishedAt,"2022-02-26T10:04:24Z")
        self.assertEqual(self.new_articles.content,"(Bloomberg) -- A Canadian House of Commons committee has recommended the government withhold approval for Rogers Communications Inc.s planned takeover of Shaw Communications Inc. unless it disposes o… [+981 chars]")  
