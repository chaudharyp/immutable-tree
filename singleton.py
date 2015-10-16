import threading

# Creating a singleton class for thread safety
class Singleton(object):
	__singleton_lock = threading.Lock()
	__singleton_instance = None

	def instance(cls):
		if not cls.__singleton_instance:
			with cls.__singleton_lock:
				if not cls.__singleton_instance:
					cls.__singleton_instance = cls()
		return cls.__singleton_instance