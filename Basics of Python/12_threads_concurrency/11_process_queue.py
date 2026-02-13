from multiprocessing import Process, Queue

def prepare_chai(queue):
  queue.put("Masala Chai is ready")

if __name__ == "__main__":
  queue = Queue()

  processes = Process(target=prepare_chai, args=(queue,))
  processes.start()
  processes.join()
  print(queue.get())