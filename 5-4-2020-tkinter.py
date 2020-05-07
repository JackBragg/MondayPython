from tkinter import *

class obs_interface(object):

  def __init__(self):
    self.listeners = []
    self.assets = []

  def register_listener(self, listener):
    if listener not in self.listeners:
      self.listeners.append(listener)

  def update_listeners(self):
    for listener in self.listeners:
      listener.update_me(self.assets)

class lis_interface(object):
  
  def __init__(self):
    self.assets = []

  def update_me(self, *args, **kwargs):
    self.assets = args

def main():
  # def update_var():

  def do_a_thing():
    value = lis_box.get(lis_box.curselection())
    ttt = value
  #   temp_obs.assets = usr_entry.get()
  #   temp_obs.update_listeners()
  # temp_obs = obs_interface()
  # temp_obs.assets = 'hello!'
  # temp_lis = lis_interface()
  # temp_obs.register_listener(temp_lis)
  # temp_obs.update_listeners()
  ttt = 'hello'
  window = Tk()
  window.title("welcome")
  window.geometry('350x200')
  lis_box = Listbox(window,bg='Blue')
  lis_box.grid(column=5, row=5)
  lis_box.insert(1, 'red')
  lis_box.insert(2, 'green')
  lis_box.insert(3, 'blue')
  lis_box.insert(4, 'indigo')
  lis_box.insert(5, 'violet')
  lis_box.insert(6, 'tacos')
  usr_entry = Entry(window, bg='black', fg='white', textvariable=ttt)
  usr_entry.grid(column=2, row=1)
  lbl = Label(window, textvariable=ttt)
  lbl.grid(column=0, row=0)
  btn = Button(window, text="click this", fg="black", command=do_a_thing)
  btn.grid(column=1, row=0)
  window.mainloop()


if __name__ == '__main__':
  main()
