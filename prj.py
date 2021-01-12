import projekti
import shah       #importimi i fajllave te te dy lojerave
import turtle

def dritarjakryesore():

    #Krijimi i ekranit per pjesen hyrese
    skenaa = turtle.Screen() 
    skenaa.title("Projekti") #Titulli i ekranit
    skenaa.bgpic("loja.png") #Background i ekranit 
    skenaa.setup(width=1000, height=600) #Gjeresia dhe gjatesia e ekranit

    #Shkruarja e fjalise hyrese
    vizato = turtle.Turtle()
    vizato.speed(0) 
    vizato.color("dark blue") 
    vizato.penup() 
    vizato.hideturtle()
    vizato.goto(0, 90)  #koordinatat ku duhet te filloje shkruarja e tekstit
    vizato.write("Zgjedhni cilen loje deshironi ta luani: ", align="center", font=("Segoe Print", 24, "bold"))
    
    pen=turtle.Turtle()
    pen.hideturtle()
    pen.fillcolor("royal blue")  #Ngjyra me te cilen mbushet figura e krijuar
    pen.pensize(3)   #Trashesia e vijes
    
    def rect(pen, message = 'Ping Pong'):  #Pjesa ku fillon vizatimi i butonit per te kaluar ne lojen Ping Pong
        
        pen.penup()
        pen.begin_fill()
        pen.goto(-50, -50)  #koordinatat ku duhet te filloje vizatimi
        pen.goto(-50 + 100, -50)
        pen.goto(-50 + 100, -50 + 50)
        pen.goto(-50, -50 + 50)
        pen.goto(-50, -50)
        pen.end_fill()
        pen.goto(-50 + 15, -50 + 15)
        pen.write(message, font = ('Segoe Print', 10, 'bold'))
      

    def rectt(pen, message = '   Shah'):  #Pjesa ku fillon vizatimi i butonit per te kaluar ne lojen Shah
        
        pen.penup()
        pen.begin_fill()
        pen.goto(-50, -110)
        pen.goto(-50 + 100, -110)
        pen.goto(-50 + 100, -110 + 50)
        pen.goto(-50, -110 + 50)
        pen.goto(-50, -110)
        pen.end_fill()
        pen.goto(-50 + 15, -110 + 15)
        pen.write(message, font = ('Segoe Print', 11, 'bold'))
     
      #Thirrja e metodave te mesiperme   
    rect(pen)
    rectt(pen)
    
    def klikobutonin(x,y):   #Metoda e cila i tregon programit se kur shtypet njeri buton cfare veprimi te beje 
     
     if -50 <= x <= -50 + 100:
        if -50 <= y <=-50 + 50:

            skenaa.clear()
            projekti.pingpong()  #Kalon tek loja Ping Pong
            
     if -50 <= x <= -50 + 100:
        if -110 <= y <=-110 + 50:
            
            skenaa.clear()
            shah.shah()     #Kalon tek loja Shah
    
    skenaa.onclick(klikobutonin)    #Aksioni i klikimit te butonit
       
dritarjakryesore()
