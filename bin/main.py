from src.word_frequency import word_frequency
from src.circular_queue import circular_queues
from src.password_validator import validate_passwords
from threading import Thread

def main():
    try:
        t1 = Thread(target=word_frequency)
        t2 = Thread(target=circular_queues)
        t3 = Thread(target=validate_passwords)
        
        t1.start()
        t2.start()
        t3.start()
        
        t1.join()
        t2.join()
        t3.join()    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
if __name__=="__main__":
    main()
    
        