'''
Created on Aug 22, 2014

@author: sdc50
'''
import unittest
from condorpy import Job

try:
    import htcondor
except ImportError:
    import condorpy.pseudohtcondor as htcondor

try:
    import classad
except ImportError:
    import condorpy.pseudoclassad as classad

def load_tests(loader, tests, pattern):
    return unittest.TestLoader().loadTestsFromTestCase(JobTest)

class JobTest(unittest.TestCase):


    def setUp(self):
        self.job = Job()


    def tearDown(self):
        pass


    def test_constructor(self):
        self.job = Job()
        self.assertIsInstance(self.job.ad,classad.ClassAd, 'ad must be instance of classad.Classad')
        self.assertIsNone(self.job.cluster_id,'cluster id should be set to None')
        self.assertIsInstance(self.job.schedd,htcondor.Schedd,'schedd must be an instance of htcondor.Schedd')

        ad = classad.ClassAd({'Foo':'Bar'})
        self.job = Job(ad)
        self.assertEqual(ad, self.job.ad,'ad was not properly assigned')

        '''
        ad = None
        if not ad:
            ad = classad.ClassAd()
        if not ad:
            print 'why not?'
        assert(isinstance(ad,classad.ClassAd))
        self.job = Job(ad)
        self.assertEqual(ad, self.job.ad,'ad was not properly assigned')
        '''

##########################################
#
#    Unit Tests
#
##########################################
'''
def runTests():
    print 'testing'
    # call tests here
    test1()
    testTemplates()
    noCmdTest()
    condorErrorTest()
    print 'passed'

def test1():
    job = Job()
    print job
    job.set('executable', 'echo')
    print job
    job = Job()
    print job
    #job.submit()

def testTemplates():
    print 'Testing classad templates . . .'
    import classad_templates as tmplt
    job = Job(tmplt.ST_GSSHA)
    job.set('initialdir', './test')
    print job
    #job.submit(2)

def noCmdTest():
    print 'Testing no executable . . .'

    job = Job()
    print job
    try:
        job.submit()
        raise
    except NoExecutable as e:
        print str(e)

def condorErrorTest():
    print 'Testing condor errors'
    job = Job()
    job.set('executable', 'job.py')
    job.set('not_an_attr', 'foobar')
    try:
        job.submit()
    except Exception as e:
        print str(e)'''

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()