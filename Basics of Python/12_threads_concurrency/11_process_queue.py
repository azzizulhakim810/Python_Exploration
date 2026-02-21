from multiprocessing import Process, Queue

def prepare_chai(queue):
  queue.put("Masala Chai is ready")

if __name__ == "__main__":
  queue = Queue()

  processes = Process(target=prepare_chai, args=(queue,))
  processes.start()
  processes.join()
  print(queue.get())


# Queue (Task Distribution)
# Processes send results/messages to each other through a queue.
# Real-world uses:

# Web scraping: Multiple workers fetch different URLs, put results in queue for main process to save
# Image processing: Workers process different images, send completed ones through queue
# Task workers: Like a restaurant where multiple chefs (processes) prepare dishes and put them on the counter (queue) for servers to pick up
# Data pipelines: One process reads files, puts data in queue, other processes transform/save it

# Key point: Good when processes work independently and need to pass data/results around.