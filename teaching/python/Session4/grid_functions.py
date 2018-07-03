
#fancy stuff - but you can understand it all already!
def drawGridMark (ttl, x, y, isVertical):
    if isVertical :
        drawLine (ttl, x, y + 5, x, y - 5)
    else:
        drawLine (ttl, x - 5, y, x + 5, y)

def labelGridPoint (ttl, x, y, isVertical, text):
    if isVertical:
        labelPoint (ttl, x - 20, y - 20, text)
    else:
        labelPoint (ttl, x + 20, y, text)

def labelPoint (ttl, x, y, label):
    ttl.penup()
    ttl.goto (x, y)
    ttl.pendown()
    ttl.write (label)
    ttl.penup()

def drawGridScaled (ttl,scale):
    # draw the axes
    drawLine (ttl, -400, 0, 400, 0)
    drawLine (ttl, 0, 400, 0, -400)

    # label the x axis
    for x in [-300, -200, -100, 100, 200, 300]:
        drawGridMark (ttl, x, 0, True)
        labelGridPoint (ttl, x, 0, True, (x/scale, 0))

    # label the y axis
    for y in [-300, -200, -100, 100, 200, 300]:
        drawGridMark (ttl, 0, y, False)
        labelGridPoint (ttl, 0, y, False, (0, y/scale))
        
def drawLine (ttl, x1, y1, x2, y2):
    """
    turtle ttl draws a line between the points (x0,y0) and (x1,y1)
    """
    ttl.penup()
    ttl.goto (x1, y1)
    ttl.pendown()
    ttl.goto (x2, y2)
    ttl.penup()