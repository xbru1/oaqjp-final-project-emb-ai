from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):

    # Test the emotion detector
    def test_emotion_detector(self):
        # Tests are defined with this array to make adding more easier
        tests = [ ['I am glad this happened', 'joy'], ['I am really mad about this', 'anger'], ['I feel disgusted', 'disgust'], ['I am so sad about this', 'sadness'], ['I am really afraid that this will happen', 'fear'] ]

		# Loop through the tests
        for i in tests:
            result = emotion_detector(i[0])
            self.assertEqual(result['dominant_emotion'], i[1])

unittest.main()