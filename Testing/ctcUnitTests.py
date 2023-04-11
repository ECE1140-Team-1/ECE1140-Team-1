import sys, unittest
sys.path.append('../Full System')
from CTC import CTC
import TrackParser

class TestCTC(unittest.TestCase):

    def testDispatch(self):
        track = TrackParser.parseTrack("TrackLayout.csv")
        ctc = CTC(track)
        self.assertEqual(ctc.nextID,1)
        ctc.greenDispatch(73)
        self.assertEqual(ctc.nextID,2)

unittest.main()