import Math

def main():
    global nVerts = int(input("How many vertices are in your polygon?: "))
    global arrayOfCoords = []
    organiseCoords()
    
def organiseCoords():
    for i in range(1, nVerts):
        tempArray = []
        tempArray.append(int(input("Please enter the X coordinate: ")))
        tempArray.append(int(input("Please enter the Y coordinate: ")))
        arrayOfCoords.append(tempArray)
    calculation()
    
def calculation():
    for i in arrayOfCoords:
        
    
