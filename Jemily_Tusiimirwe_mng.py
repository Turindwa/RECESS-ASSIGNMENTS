 #CONTEXT MANAGER
                   
"""Context managers are used to set up and tear down temporary contexts, establish and resolve custom settings, and acquire and release resources. 
The open() function for opening files is one of the most familiar examples of a context manager.."""

#Context manager implementation in file handling
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

# Usage:
with FileManager("Jemily.txt", "w") as file:
    file.write("Good morning!")
    

    #context manager for managing a database connection
    import sqlite3

class DatabaseConnection:

    def __init__(self, db_file):
        self.db_file = db_file

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_file)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

def main():
    with DatabaseConnection('my_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        for row in cursor:
            print(row)

if __name__ == '__main__':
    main()
    
#MULTI THREADING
"""Multithreading in Python is a way of running multiple tasks at the same time within a single process. 
This can be used to improve the performance of your program by allowing it to do more work in parallel.
It enables you to run multiple threads of execution simultaneously, leveraging
the capabilities of modern processors with multiple cores or executing
tasks concurrently while waiting for I/O operations."""
 
# EXAMPLE OF MULTI THREADING
import threading

def fact(n):
    # Code to be executed by the thread
    print(f"Thread {n} started")

# Number of threads to create
num_threads = 8

# Create a list to hold the thread objects
threads = []

# Create and start the threads
for i in range(num_threads):
    thread = threading.Thread(target=fact, args=(i,))
    thread.start()
    threads.append(thread)

#Wait for all the threads to complete
for thread in threads:
    thread.join()

print("Threads completed")
                        
                        
#MULTI PROCESSING
import multiprocessing

def process (city):
    print(f"Running {city}")
    
#Loop for the processes
pool=multiprocessing.Pool(processes=5)

#Sending tasks into the pool
for i in range(8):
    pool.apply_async(process,args=(f"Process {i}",))


#closing the pool and waiting for all processes to finish
pool.close()
pool.join()
                        
                        
                    
