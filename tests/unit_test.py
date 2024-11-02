import unittest
from src.word_frequency import frequency_check
from src.circular_queue import CircularQueue
from src.password_validator import validate

class TestWordFrequency(unittest.TestCase):
    def test_word_frequency(self):
        text = "which is better python 2 or python 3"
        result = frequency_check(text)
        expected = [('2', 1), ('3', 1), ('better', 1), ('is', 1), ('or', 1), ('python', 2), ('which', 1)]
        self.assertEqual(result, expected)

    def test_enqueue(self):
        nums = CircularQueue(5)
        for i in range(1,8):
            nums.enqueue(str(i)) 
        result = list(nums.queue.values())
        expected = ['3', '4', '5', '6', '7']  # Expected queue state after enqueuing 7 items
        self.assertEqual(result, expected)
        
    def test_validate_passwords(self):
        passwords = ['Asqwr1234@1', 'aF145#', '2w3E*', '2We3345']
        result = validate(passwords)
        expected = ["Asqwr1234@1", "aF145#"]
        self.assertEqual(result, expected)
        
if __name__ == "__main__":
    unittest.main()
