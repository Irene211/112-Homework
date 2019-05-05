#################################################################
# Hw8
# Your Name: Tianming Zhang
# Your Andrew ID: tianminz
# Your Section: H
#################################################################
import random, math
#################################################
# Hw8 Bird Classes and Subclasses
#################################################

def birdClassCollaborators():
    return "nobody"
    
#Define properties and methods of Brid
class Bird(object):
    #set up newly-created objects 
    #takes "self", "name" as input
    def __init__(self, name):
        self.name = name
        self.numEggs = 0
        self.evenNum = 2
    
    #Make print display the number of eggs for a name.
    def __repr__(self):
        if self.countEggs() % self.evenNum == 0:
            lastStr = "s"
        else:
            lastStr = ""
        return ("%s has %d egg%s" %
                (self.name, self.countEggs(), lastStr))
    
    #Set up the object's hash value
    def __hash__(self):
        return hash(self.name)
    
    #Evalute the equality of two objects
    def __eq__(self, other):
        return (isinstance(other,Bird) and (self.name == other.name))
    
    #Define fly method
    def fly(self):
        return "I can fly!"
    
    #Define countEggs method to call numEggs
    def countEggs(self):
        return self.numEggs
    
    #Define leyeggs method to edd one when called
    def layEgg(self):
        self.numEggs += 1
        return self.numEggs
    
# define properties and methods of subclass Penguin
class Penguin(Bird):
    #Redefine fly method
    def fly(self):
        return "No flying for me."
    #Define swim method
    def swim(self):
        return "I can swim!"

# define properties and methods of subclass Bird
class MessengerBird(Bird):
    #Overwrite the init method to add message
    def __init__(self, name, message=""): 
        super().__init__(name)
        self.message = message
    
    #Add a new method to deliever message
    def deliverMessage(self):
        return self.message


#################################################
# Hw8 Asteroid Functions
# All graphics must go under here to avoid angering the autograder!
# ignore_rest
#################################################
def asteroidCollaborators():
    return "nobody"

#### OOP Classes ####
#Asteroid and subclasses, ShrinkingAsteroid and SplittingAsteroid 
class Asteroid(object):
    # Model. Set up newly created objects.
    def __init__(self, cx, cy, r, speed, direction):
        # An asteroid has a position, size, speed, and direction
        self.cx = cx
        self.cy = cy
        self.r = r
        self.speed = speed
        self.direction = direction
    # View. Set up the purple asteroids.
    def draw(self, canvas, color="purple"):
        canvas.create_oval(self.cx - self.r, self.cy - self.r,
                           self.cx + self.r, self.cy + self.r, fill=color)
    # Controller. This function set up how asteroids move
    def moveAsteroid(self):
        self.cx += self.speed * self.direction[0]
        self.cy += self.speed * self.direction[1]
    # Check if the asteroid hits the wall or overlaps it at all
    def collidesWithWall(self, width, height):
        return self.cx - self.r <= 0 or self.cx + self.r >= width or \
            self.cy - self.r <= 0 or self.cy + self.r >= height
    #Determine whether asteroid has hit a wall and react appropriately.
    def reactToWallHit(self, width, height):
        if self.cx< 0:
            self.cx = width
        if self.cx > width:
            self.cx = 0
        if self.cy < 0:
            self.cy = height
        if self.cy > height:
            self.cy = 0
      
class ShrinkingAsteroid(Asteroid):
    # Model. Set up new method
    def __init__(self, cx, cy, r, speed, direction):
        # Shrinking Asteroids also track how fast they shrink
        super().__init__(cx, cy, r, speed, direction)
        self.shrinkAmount = 5 
    # View. Draw the pink asteroid
    def draw(self, canvas):
        super().draw(canvas, color="pink")
    # Controller. Let asteroid move based on pre-determined direction
    def changeDirection(self):
        dx, dy = self.direction
        dx *= -1
        dy *= -1
        self.direction = (dx, dy)
    #Shrink according to certain shrink amount
    def shrink(self):
        self.r -= self.shrinkAmount
        return self.r <= self.shrinkAmount
    
## Rocket class ##
class Rocket(object):
    # Model. Set up newly defined objects.
    def __init__(self, cx, cy):
        # A rocket has a position and a current angle it faces
        self.cx = cx
        self.cy = cy
        self.angle = 90
    # View. Draws a cool-looking triangle-ish shape
    def draw(self, canvas):
        size = 30
        angle = math.radians(self.angle)
        angleChange = 2*math.pi/3
        numPoints = 3
        points = []
        for point in range(numPoints):
            points.append((self.cx + size*math.cos(angle \
                           + point * angleChange),
                           self.cy - size*math.sin(angle \
                           + point * angleChange)))
        points.insert(numPoints-1, (self.cx, self.cy))
        canvas.create_polygon(points, fill="green2")
    # Controller. Rotate the rocket in certain degree
    def rotate(self, numDegrees):
        self.angle += numDegrees
    # Generates a bullet heading in the direction the ship is facing
    def makeBullet(self):
        offset = 35
        x = self.cx + offset*math.cos(math.radians(self.angle)) 
        y = self.cy - offset*math.sin(math.radians(self.angle))
        speedLow, speedHigh = 20, 40
        return Bullet(x, y, self.angle, \
                      random.randint(speedLow, speedHigh))

## Bullet Class ##
class Bullet(object):
    # Model. Set up new objects.
    def __init__(self, cx, cy, angle, speed):
        # A bullet has a position, a size, a direction, and a speed
        self.cx = cx
        self.cy = cy
        self.r = 5
        self.angle = angle
        self.speed = speed
        self.squareNum = 2
        self.rootingNum = 0.5
    # View. Draw the white bullet
    def draw(self, canvas):
        canvas.create_oval(self.cx - self.r, self.cy - self.r, 
                           self.cx + self.r, self.cy + self.r,
                           fill="white", outline=None)
    # Controller. # Move according to the original trajectory
    def moveBullet(self):
        self.cx += math.cos(math.radians(self.angle))*self.speed
        self.cy -= math.sin(math.radians(self.angle))*self.speed
    # Check if the bullet and asteroid overlap at all
    def collidesWithAsteroid(self, other):
        if(not isinstance(other, Asteroid)): # Other must be an Asteroid
            return False
        else:
            dist = ((other.cx - self.cx)** self.squareNum + (other.cy\
                    - self.cy)** self.squareNum)** self.rootingNum
            return dist < self.r + other.r
    # Check if the bullet has moved fully offscreen
    def isOffscreen(self, width, height):
        return (self.cx + self.r <= 0 or self.cx - self.r >= width) or \
               (self.cy + self.r <= 0 or self.cy - self.r >= height)

#### Graphics Functions ####
from tkinter import *
#Initialize the data
def init(data):
    data.halfNum = 2
    data.rocket = Rocket(data.width//data.halfNum, data.height//data.halfNum)
    data.score = 0
    
    data.bullets = []
    data.shrinkingAsteroids = []
    data.asteroids = []
    data.clock = 0

def mousePressed(event, data):
    pass
#Press "Right"/"Left"/"Space" and reate properly.
def keyPressed(event, data):
    numRot = 5
    if event.keysym == "Right":
        data.rocket.rotate(-numRot)
    elif event.keysym == "Left":
        data.rocket.rotate(numRot)
    elif event.keysym == 'space':
        bullet = data.rocket.makeBullet()
        data.bullets.append(bullet)

#Looping over time and simulating movement over time
def timerFired(data):
    data.clock += 1
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # create new asteroids
    generateNew = 10
    newPosition = 30
    if data.clock % generateNew == 0:
        data.clock = 0
        r = random.randint(0, 1)
        cx = random.randint(newPosition, data.width - newPosition)
        cy = random.randint(newPosition, data.height - newPosition)
        speed = random.randint(generateNew, generateNew * data.halfNum)
        direction = directions[random.randint(0, len(directions) - 1)]
        if r == 0: # purple
            r = newPosition
            data.asteroids.append(Asteroid(cx, cy, r, speed, direction))
        else: # pink
            r = random.randint(generateNew  * data.halfNum, newPosition)
            data.shrinkingAsteroids.append(ShrinkingAsteroid(cx, cy,\
                                           r, speed, direction))

    width, height = data.width, data.height
    # check if bullet is off screen
    bullet_to_be_removed = []
    for bullet in data.bullets:
        bullet.moveBullet()
        if bullet.isOffscreen(width, height):
            bullet_to_be_removed.append(bullet)
    # move asteroids
    for asteroid in data.asteroids + data.shrinkingAsteroids:
        asteroid.moveAsteroid()
    #Checks whether any of the bullets collide with any of the asteroids
    asteroid_to_be_removed = []
    for bullet in data.bullets:
        for asteroid in data.asteroids + data.shrinkingAsteroids:
            if bullet.collidesWithAsteroid(asteroid):
                if type(asteroid) == Asteroid:
                    asteroid_to_be_removed.append(asteroid)
                    bullet_to_be_removed.append(bullet)
                else:
                    die = asteroid.shrink()
                    if die:
                        asteroid_to_be_removed.append(asteroid)
                        bullet_to_be_removed.append(bullet)
    data.score += len(asteroid_to_be_removed)

    for bullet in bullet_to_be_removed:
        data.bullets.remove(bullet)
    for asteroid in asteroid_to_be_removed:
        if asteroid in data.asteroids: 
            data.asteroids.remove(asteroid)
        else:
            data.shrinkingAsteroids.remove(asteroid)

    for asteroid in data.asteroids:
        if asteroid.collidesWithWall(width, height):
            asteroid.reactToWallHit(width, height)

    for asteroid in data.shrinkingAsteroids:
        if asteroid.collidesWithWall(width, height):
            asteroid.changeDirection()


#Draw the background, bullet, asteroid, text.
def redrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="gray3")
    data.rocket.draw(canvas)
    for bullet in data.bullets:
        bullet.draw(canvas)
    for asteroid in data.asteroids + data.shrinkingAsteroids:
        asteroid.draw(canvas)
    canvas.create_text(data.width/2, data.height, \
                       anchor="s", fill="yellow",
                       font="Arial 24 bold", \
                       text="Score: " + str(data.score))
   
#################################################################
# use the run function as-is
#################################################################

def runAsteroids(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")



#################################################
# Hw8 Test Functions
#################################################

def getLocalMethods(clss):
    import types
    # This is a helper function for the test function below.
    # It returns a sorted list of the names of the methods
    # defined in a class. It's okay if you don't fully understand it!
    result = [ ]
    for var in clss.__dict__:
        val = clss.__dict__[var]
        if (isinstance(val, types.FunctionType)):
            result.append(var)
    return sorted(result)

def testBirdClasses():
    print("Testing Bird classes...", end="")
    # A basic Bird has a species name, can fly, and can lay eggs
    bird1 = Bird("Parrot")
    assert(type(bird1) == Bird)
    assert(isinstance(bird1, Bird))
    assert(bird1.fly() == "I can fly!")
    assert(bird1.countEggs() == 0)
    assert(str(bird1) == "Parrot has 0 eggs")
    bird1.layEgg()
    assert(bird1.countEggs() == 1)
    assert(str(bird1) == "Parrot has 1 egg")
    bird1.layEgg()
    assert(bird1.countEggs() == 2)
    assert(str(bird1) == "Parrot has 2 eggs")
    tempBird = Bird("Parrot")
    assert(bird1 == tempBird)
    tempBird = Bird("Wren")
    assert(bird1 != tempBird)
    nest = set()
    assert(bird1 not in nest)
    assert(tempBird not in nest)
    nest.add(bird1)
    assert(bird1 in nest)
    assert(tempBird not in nest)
    nest.remove(bird1)
    assert(bird1 not in nest)
    assert(getLocalMethods(Bird) == ['__eq__','__hash__','__init__', 
                                     '__repr__', 'countEggs', 
                                     'fly', 'layEgg'])
    
    # A Penguin is a Bird that cannot fly, but can swim
    bird2 = Penguin("Emperor Penguin")
    assert(type(bird2) == Penguin)
    assert(isinstance(bird2, Penguin))
    assert(isinstance(bird2, Bird))
    assert(not isinstance(bird1, Penguin))
    assert(bird2.fly() == "No flying for me.")
    assert(bird2.swim() == "I can swim!")
    bird2.layEgg()
    assert(bird2.countEggs() == 1)
    assert(str(bird2) == "Emperor Penguin has 1 egg")
    assert(getLocalMethods(Penguin) == ['fly', 'swim'])
    
    # A MessengerBird is a Bird that can optionally carry a message
    bird3 = MessengerBird("War Pigeon", message="Top-Secret Message!")
    assert(type(bird3) == MessengerBird)
    assert(isinstance(bird3, MessengerBird))
    assert(isinstance(bird3, Bird))
    assert(not isinstance(bird3, Penguin))
    assert(not isinstance(bird2, MessengerBird))
    assert(not isinstance(bird1, MessengerBird))
    assert(bird3.deliverMessage() == "Top-Secret Message!")
    assert(str(bird3) == "War Pigeon has 0 eggs")
    assert(bird3.fly() == "I can fly!")

    bird4 = MessengerBird("Homing Pigeon")
    assert(bird4.deliverMessage() == "")
    bird4.layEgg()
    assert(bird4.countEggs() == 1)
    assert(getLocalMethods(MessengerBird) == ['__init__', 'deliverMessage'])
    print("Done!")


a = []
a.append([1,2,3])
a.append([2,3])
#################################################
# Hw4 Main
#################################################
def testAll():
    testBirdClasses()
    runAsteroids(600, 600)

def main():
    testAll()

if __name__ == '__main__':
    main()
