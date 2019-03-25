def setup():
    background(255, 204, 0)
    size(400,400)
    textSize(120)
    textAlign(CENTER)
def draw():
    if keyPressed == True:
        fill(0, 0, 250,250)
    if key == 'b':
        text("B", width/2+100, height/2)
    if mousePressed:
        text("A", width/2-100, height/2)
        fill(204, 102, 0)

    

    
        
    s = createShape()
    s.beginShape()
    s.fill(30, 20, 55, 55)
    s.noStroke()
    s.vertex(100, height/3*2)
    s.vertex(width/2-50, height/3*2-50)
    s.vertex(width/2, height/3*2)
    s.vertex(width/2+50, height/3*2+50)
    s.vertex(width-100, height/3*2)
    s.endShape(CLOSE)
    shape(s, 25, 25)