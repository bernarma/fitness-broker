# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

To run tests: python -m unittest test.test_main


Before running the test - start mosquitto (assume it's localhost 1883)

Ubuntu: install "mosquitto" package


Example code to encapsulate the properties of self to the class - maybe do that for our other 2 threads

class workerthread(threading.Thread):
        def __init__(self,queue):
                threading.Thread.__init__(self)
                self.queue=queue
        def run(self):
                print 'In Worker Class'
                while True:
                        counter=self.queue.get()
                        print 'Going to Sleep'
                        time.sleep(counter)
                        print ' I am up!'
                        self.queue.task_done()
queue=Queue.Queue()

for i in range(10):
        worker=workerthread(queue)
        print 'Going to Thread!'
        worker.daemon=True
        worker.start()
for j in range(10):
        queue.put(j)
queue.join()