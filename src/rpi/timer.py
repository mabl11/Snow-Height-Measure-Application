from threading import Timer


class CTimer():

   def __init__(self,reps,do_function):
      self.reps=reps
      self.do_function = do_function
      self.timed_thread = Timer(self.reps,self.handle_function)

   def handle_function(self):
      """new thread for each timer operation"""
      self.do_function()
      self.timed_thread = Timer(self.reps,self.handle_function)
      self.timed_thread.start()

   def start(self):
      """start timer"""
      self.timed_thread.start()

   def stop(self):
      """stop timer"""
      self.timed_thread.cancel()
   
   def alive(self):
      """check if timer is alive (running)
      
      Returns:
         state: if running, True, else False (boolean)
      """
      running = self.timed_thread.is_alive()
      if running:
         return True
      else:
         return False
   

if __name__ == '__main__':
   # pass 
   def printer():
      print("a")
      # return "a"

   t = CTimer(5,printer)

   t.start()
   if t.alive():
      print("lebt")
      t.stop()
   
