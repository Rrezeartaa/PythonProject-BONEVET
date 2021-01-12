import turtle 
import prj
def pingpong():
    #Krijimi i ekranit per Ping Pong
    s = turtle.Screen() 
    s.title("Loja Ping Pong") 
    s.bgpic("tabela.png") 
    s.setup(width=1000, height=600)

    pen=turtle.Turtle()
    pen.hideturtle()
    pen.fillcolor("sea green")

    def kthehu(pen, message = '   Kthehu '):  #Metoda per butonin Kthehu
        
        pen.penup()
        pen.begin_fill()
        pen.goto(-500, 260)
        pen.goto(-500 + 100, 260)
        pen.goto(-500 + 100, 260 + 50)
        pen.goto(-500, 260 + 50)
        pen.goto(-500, 260)
        pen.end_fill()
        pen.goto(-500 + 15, 260 + 10)
        pen.write(message, font = ('Segoe Print', 10, 'normal'))
         

    def recti(pen, message = 'Luaj perseri '): #Metoda per butonin Luaj perseri
        
        pen.penup()
        pen.begin_fill()
        pen.goto(-50, -50)
        pen.goto(-50 + 100, -50)
        pen.goto(-50 + 100, -50 + 50)
        pen.goto(-50, -50 + 50)
        pen.goto(-50, -50)
        pen.end_fill()
        pen.goto(-50 + 15, -50 + 15)
        pen.write(message, font = ('Segoe Print', 9, 'normal'))
      
    
    def klikoobutonin(x,y):
     
      if -50 <= x <= -50 + 100:
          if -50 <= y <=-50 + 50:
 
            s.clear()
            pingpong()
                  
      if -500 <= x <= -500 + 100:
          if 260 <= y <= 260 + 50:
            
            s.clear()
            prj.dritarjakryesore()     

    # Pjesa ku vizatohen te dy drejtkendeshat me ngjyre te zeze te dy anet                
    anamajte = turtle.Turtle() 
    anamajte.speed(0) 
    anamajte.shape("square") 
    anamajte.color("black") 
    anamajte.shapesize(stretch_wid=6, stretch_len=2) 
    anamajte.penup() 
    anamajte.goto(-400, 0) 
         
    anadjathte = turtle.Turtle() 
    anadjathte.speed(0) 
    anadjathte.shape("square") 
    anadjathte.color("black") 
    anadjathte.shapesize(stretch_wid=6, stretch_len=2) 
    anadjathte.penup() 
    anadjathte.goto(400, 0) 

    # Pjesa e vizatimit te topit     
    topi = turtle.Turtle() 
    topi.speed(40) 
    topi.shape("circle") 
    topi.color("dark orange") 
    topi.penup() 
    topi.goto(0, 0) 
    topi.dx = 5
    topi.dy = -5
      
    lojtari1 = 0
    lojtari2 = 0

    #Paraqitja e pikeve
    vizato = turtle.Turtle() 
    vizato.speed(0) 
    vizato.color("red") 
    vizato.penup() 
    vizato.hideturtle() 
    vizato.goto(0, 230) 
    vizato.write("Lojtari 1 : 0   Lojtari 2: 0", align="center", font=("Segoe Print", 24, "bold")) 
      
      
    def paddleaup():   # Ngritja e drejtkendeshit ne anen e majte
        y = anamajte.ycor() 
        y += 20
        anamajte.sety(y) 
      
      
    def paddleadown():     # Ulja e drejtkendeshit ne anen e majte
        y = anamajte.ycor() 
        y -= 20
        anamajte.sety(y) 
      
      
    def paddlebup():       # Ngritja e drejtkendeshit ne anen e djathte
        y = anadjathte.ycor() 
        y += 20
        anadjathte.sety(y) 
      
      
    def paddlebdown():    # Ulja e drejtkendeshit ne anen e djathte
        y = anadjathte.ycor() 
        y -= 20
        anadjathte.sety(y)

    # Pjesa ku mund te veprojme me ekranit permes tastieres per t'i levizur dy drejtkendeshat e krijuar         
    s.listen() 
    s.onkeypress(paddleaup, "e") 
    s.onkeypress(paddleadown, "x") 
    s.onkeypress(paddlebup, "Up") 
    s.onkeypress(paddlebdown, "Down") 

    # Unaza while: perderisa eshte true topi vazhdon te levize dhe numerohen piket e lojtareve 
    while True:
        
        s.update() 

        #Pozicioni ku fillon levizja e topit
        topi.setx(topi.xcor()+topi.dx) 
        topi.sety(topi.ycor()+topi.dy) 
       
        if topi.ycor() > 280: 
            topi.sety(280) 
            topi.dy *= -1
      
        if topi.ycor() < -280: 
            topi.sety(-280) 
            topi.dy *= -1
            
        # Nese drejtekendeshi ne anen e djathte nuk e pret topin pika iu shtohet lojtarit te pare
        if topi.xcor() > 500: 
            topi.goto(0, 0) 
            topi.dy *= -1
            lojtari1 += 1
            vizato.clear() 
            vizato.write("Lojtari 1 : {}   Lojtari 2: {}".format(lojtari1, lojtari2), align="center", font=("Segoe Print", 24, "bold"))

        # Nese drejtekendeshi ne anen e majte nuk e pret topin pika iu shtohet lojtarit te dyte        
        if topi.xcor() < -500: 
            topi.goto(0, 0) 
            topi.dy *= -1
            lojtari2 += 1
            vizato.clear() 
            vizato.write("Lojtari 1 : {}   Lojtari 2: {}".format(lojtari1, lojtari2), align="center",font=("Segoe Print", 24, "bold")) 

        # Pjesa e cila e kontrollon kthimin (perplasjen) e topit 
        if (topi.xcor() > 360 and topi.xcor() < 370) and(topi.ycor() < anadjathte.ycor()+40 and topi.ycor() > anadjathte.ycor()-40): 
            topi.setx(360) 
            topi.dx*=-1
             
        if (topi.xcor()<-360 and topi.xcor()>-370) and(topi.ycor()<anamajte.ycor()+40 and topi.ycor()>anamajte.ycor()-40): 
            topi.setx(-360) 
            topi.dx*=-1
            
        # Loja mbaron kur njeri nga lojtaret t'i beje 5 pike
        if lojtari1==5 or lojtari2==5:

            #Krahasohen piket e lojtareve ne menyre qe te shpallet fituesi
            if lojtari1>lojtari2:
              
              s.clear()   # Fshirja e ekranit te lojes 
              vizato.clear() 
              s.bgpic("to.png")
              
              vizato.goto(0, 100) 
              vizato.write("Loja mbaroi! Fituesi eshte lojtari 1".format(), align="center",font=("Segoe Print", 24, "bold"))
              recti(pen)
              kthehu(pen)              
              s.onclick(klikoobutonin)  #Aksioni i klikimit te butonave             
              break
            
            elif lojtari1<lojtari2:
              
              s.clear()
              vizato.clear()
              s.bgpic("to.png")
              
              vizato.goto(0, 100) 
              vizato.write("Loja mbaroi! Fituesi eshte lojtari 2".format(), align="center",font=("Segoe Print", 24, "bold"))
              recti(pen)
              kthehu(pen)
              s.onclick(klikoobutonin)                         
              break
            
            
         
        
   
