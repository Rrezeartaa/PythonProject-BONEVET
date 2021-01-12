import turtle
import prj

def shah():
    #Krijimi i ekranit per lojen Shah
    turtle.setup(600, 600)
    screen = turtle.Screen()
    screen.title('Loja Shah')
    #Regjistrimi i figurave te shahut
    turtle.register_shape('WK.gif')  
    turtle.register_shape('WQ.gif')
    turtle.register_shape('BK.gif')
    turtle.register_shape('BQ.gif')
    turtle.register_shape('WB.gif')
    turtle.register_shape('BB.gif')
    turtle.register_shape('WKn.gif')
    turtle.register_shape('BKn.gif')
    turtle.register_shape('WR.gif')
    turtle.register_shape('BR.gif')
    turtle.register_shape('WP.gif')
    turtle.register_shape('BP.gif')
    screen.bgcolor('orange')
    
    tabela = turtle.Turtle()
    tabela.speed(0)
    tabela.hideturtle()
    tabela.penup()
    tabela.setpos(0,200)
    tabela.pendown()

    #Vizatimi i tabeles
    for i in range(8):
        tabela.forward(200)
        tabela.right(90)
        tabela.forward(50)
        tabela.right(90)
        tabela.forward(400)
        tabela.right(90)
        tabela.forward(50)
        tabela.right(90)
        tabela.forward(200)
        tabela.right(90)
        tabela.forward(50)
        tabela.left(90)


    tabela2 = turtle.Turtle()
    tabela2.speed(0)
    tabela2.hideturtle()
    tabela2.penup()
    tabela2.setpos(200,0)
    tabela2.pendown()
    tabela2.setheading(270)
    for i in range(8):
        tabela2.forward(200)
        tabela2.right(90)
        tabela2.forward(50)
        tabela2.right(90)
        tabela2.forward(400)
        tabela2.right(90)
        tabela2.forward(50)
        tabela2.right(90)
        tabela2.forward(200)
        tabela2.right(90)
        tabela2.forward(50)
        tabela2.left(90)

    #Shkruarja e shkronjave dhe numrave
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(-195,-210)
    writer.pendown()
    writer.write('a')
    writer.penup()
    writer.goto(-145,-210)
    writer.pendown()
    writer.write('b')
    writer.penup()
    writer.goto(-95,-210)
    writer.pendown()
    writer.write('c')
    writer.penup()
    writer.goto(-45,-210)
    writer.pendown()
    writer.write('d')
    writer.penup()
    writer.goto(5,-210)
    writer.pendown()
    writer.write('e')
    writer.penup()
    writer.goto(55,-210)
    writer.pendown()
    writer.write('f')
    writer.penup()
    writer.goto(105,-210)
    writer.pendown()
    writer.write('g')
    writer.penup()
    writer.goto(155,-210)
    writer.pendown()
    writer.write('h')
    writer.penup()
    writer.goto(-205, -195)
    writer.write('1')
    writer.penup()
    writer.goto(-205,-145)
    writer.pendown()
    writer.write('2')
    writer.penup()
    writer.goto(-205, -95)
    writer.write('3')
    writer.penup()
    writer.goto(-205,-45)
    writer.pendown()
    writer.write('4')
    writer.penup()
    writer.goto(-205, 5)
    writer.write('5')
    writer.penup()
    writer.goto(-205, 55)
    writer.write('6')
    writer.penup()
    writer.goto(-205,105)
    writer.pendown()
    writer.write('7')
    writer.penup()
    writer.goto(-205, 155)
    writer.write('8')
    writer.penup()
    
   # Shperndarja e figurave ne tabele 
    wk = turtle.Turtle()
    wk.shape('WK.gif')
    wk.penup()
    wk.setpos(25,-175)
    wk.ondrag(wk.goto)  #Pjesa ku programi mundeson bartjen e figurave

 
    wq = turtle.Turtle()
    wq.shape('WQ.gif')
    wq.penup()
    wq.setpos(-25,-175)
    wq.ondrag(wq.goto)

    
    wb1 = turtle.Turtle()
    wb1.shape('WB.gif')
    wb1.penup()
    wb1.setpos(75,-175)
    wb1.ondrag(wb1.goto)

    wb2 = turtle.Turtle()
    wb2.shape('WB.gif')
    wb2.penup()
    wb2.setpos(-75,-175)
    wb2.ondrag(wb2.goto)

    
    wk1 = turtle.Turtle()
    wk1.shape('WKn.gif')
    wk1.penup()
    wk1.setpos(125,-175)
    wk1.ondrag(wk1.goto)

    wk2 = turtle.Turtle()
    wk2.shape('WKn.gif')
    wk2.penup()
    wk2.setpos(-125,-175)
    wk2.ondrag(wk2.goto)

    wr1 = turtle.Turtle()
    wr1.shape('WR.gif')
    wr1.penup()
    wr1.setpos(175,-175)
    wr1.ondrag(wr1.goto)

    wr2 = turtle.Turtle()
    wr2.shape('WR.gif')
    wr2.penup()
    wr2.setpos(-175,-175)
    wr2.ondrag(wr2.goto)

    wp1 = turtle.Turtle()
    wp1.shape('WP.gif')
    wp1.penup()
    wp1.setpos(25,-125)
    wp1.ondrag(wp1.goto)

    wp2 = turtle.Turtle()
    wp2.shape('WP.gif')
    wp2.penup()
    wp2.setpos(-25,-125)
    wp2.ondrag(wp2.goto)

    wp3 = turtle.Turtle()
    wp3.shape('WP.gif')
    wp3.penup()
    wp3.setpos(75,-125)
    wp3.ondrag(wp3.goto)

    
    wp4 = turtle.Turtle()
    wp4.shape('WP.gif')
    wp4.penup()
    wp4.setpos(-75,-125)
    wp4.ondrag(wp4.goto)

    
    wp5 = turtle.Turtle()
    wp5.shape('WP.gif')
    wp5.penup()
    wp5.setpos(125,-125)
    wp5.ondrag(wp5.goto)

    wp6 = turtle.Turtle()
    wp6.shape('WP.gif')
    wp6.penup()
    wp6.setpos(-125,-125)
    wp6.ondrag(wp6.goto)

    wp7 = turtle.Turtle()
    wp7.shape('WP.gif')
    wp7.penup()
    wp7.setpos(175,-125)
    wp7.ondrag(wp7.goto)
    wp8 = turtle.Turtle()
    wp8.shape('WP.gif')
    wp8.penup()
    wp8.setpos(-175,-125)
    wp8.ondrag(wp8.goto)

    bk = turtle.Turtle()
    bk.shape('BK.gif')
    bk.penup()
    bk.setpos(25,175)
    bk.ondrag(bk.goto)

    bq = turtle.Turtle()
    bq.shape('BQ.gif')
    bq.penup()
    bq.setpos(-25,175)
    bq.ondrag(bq.goto)

    bb1 = turtle.Turtle()
    bb1.shape('BB.gif')
    bb1.penup()
    bb1.setpos(75,175)
    bb1.ondrag(bb1.goto)

    bb2 = turtle.Turtle()
    bb2.shape('BB.gif')
    bb2.penup()
    bb2.setpos(-75,175)
    bb2.ondrag(bb2.goto)

    bk1 = turtle.Turtle()
    bk1.shape('BKn.gif')
    bk1.penup()
    bk1.setpos(125,175)
    bk1.ondrag(bk1.goto)

    bk2 = turtle.Turtle()
    bk2.shape('BKn.gif')
    bk2.penup()
    bk2.setpos(-125,175)
    bk2.ondrag(bk2.goto)

    br1 = turtle.Turtle()
    br1.shape('BR.gif')
    br1.penup()
    br1.setpos(175,175)
    bk1.ondrag(bk1.goto)

    br2 = turtle.Turtle()
    br2.shape('BR.gif')
    br2.penup()
    br2.setpos(-175,175)
    br2.ondrag(br2.goto)

    bp1 = turtle.Turtle()
    bp1.shape('BP.gif')
    bp1.penup()
    bp1.setpos(25,125)
    bp1.ondrag(bp1.goto)

    bp2 = turtle.Turtle()
    bp2.shape('BP.gif')
    bp2.penup()
    bp2.setpos(-25,125)
    bp2.ondrag(bp2.goto)

    bp3 = turtle.Turtle()
    bp3.shape('BP.gif')
    bp3.penup()
    bp3.setpos(75,125)
    bp3.ondrag(bp3.goto)

    bp4 = turtle.Turtle()
    bp4.shape('BP.gif')
    bp4.penup()
    bp4.setpos(-75,125)
    bp4.ondrag(bp4.goto)

    bp5 = turtle.Turtle()
    bp5.shape('BP.gif')
    bp5.penup()
    bp5.setpos(125,125)
    bp5.ondrag(bp5.goto)

    bp6 = turtle.Turtle()
    bp6.shape('BP.gif')
    bp6.penup()
    bp6.setpos(-125,125)
    bp6.ondrag(bp6.goto)

    bp7 = turtle.Turtle()
    bp7.shape('BP.gif')
    bp7.penup()
    bp7.setpos(175,125)
    bp7.ondrag(bp7.goto)


    bp8 = turtle.Turtle()
    bp8.shape('BP.gif')
    bp8.penup()
    bp8.setpos(-175,125)
    bp8.ondrag(bp8.goto)

    shkruaj = turtle.Turtle()
    shkruaj.speed(0) 
    shkruaj.color("blue") 
    shkruaj.penup() 
    shkruaj.hideturtle()
    shkruaj.goto(0, 250)
    shkruaj.write("Shtypni 'esc' per tu kthyer ne dritaren kryesore ", align="center", font=("Segoe Print", 16, "bold"))

    def prapa():

      screen.clear()
      prj.dritarjakryesore()
    #Krijimi i eventit per kthim prapa me ane te tastit 'esc'    
    screen.listen() 
    screen.onkeypress(prapa, "Escape") 

