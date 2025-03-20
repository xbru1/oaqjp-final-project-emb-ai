from EmotionDetection.emotion_detection import emotion_detector

# Tests are defined in this array so that more can be easily added
tests = [ ['I am glad this happened', 'joy'], ['I am really mad about this', 'anger'], ['I feel disgusted just hearing about this', 'disgust'], ['I am so sad about this', 'sadness'], ['I am really afraid that this will happen', 'fear'] ]
# Number of tests failed
failed = 0

# Loop through the tests
for i in tests:
    result = emotion_detector(i[0])
    if (result['dominant_emotion'] != i[1]):
        print(f"Test failed for string '{i[0]}', expected result '{i[1]}' but received '{result['dominant_emotion']}'")
        failed += 1

# Print whether or not all tests passed and how many failed if not
if (failed == 0):
    print("All tests succeeded")
else:
    print(f"{failed} tests failed")
