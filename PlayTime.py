from tkinter import *
root=Tk()
#root.attributes('-fullscreen', True)
canvas=Canvas(root)
canvas.pack(fill = BOTH, expand = True)
canvas.config(bg='#ff0000') #hex red
def click(event):
    global prev
    prev=event

def draw(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x,event.y, width=3)
    R=int(255*abs(event.x/canvas.winfo_width()))
    G=int(255*abs(event.y/canvas.winfo_height()))
    B=int(255*abs(event.x/canvas.winfo_width())*abs(event.y/canvas.winfo_height()))
    #print(R,' : ', G, ' : ', B)
    canvas.config(bg='#{:02x}{:02x}{:02x}'.format(R,G,B))
    prev=event
    
def colors(event):
    R=int(255*abs(event.x/canvas.winfo_width()))
    G=int(255*abs(event.y/canvas.winfo_height()))
    B=int(255*abs(event.x/canvas.winfo_width())*abs(event.y/canvas.winfo_height()))
    #print(R,' : ', G, ' : ', B)
    canvas.config(bg='#{:02x}{:02x}{:02x}'.format(R,G,B))
    
def close_app(event):
    #print("Escape pressed")
    root.destroy()
    
root.bind('<ButtonPress>',click)
root.bind('<B1-Motion>',draw)
root.bind('<Motion>',colors)
root.bind('<Escape>',close_app)
#root.bind('<Escape>', lambda e: root.destroy())


root.mainloop()
