import turtle

t=turtle.Turtle()

def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="LEC/StarterFiles/images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("LEC/StarterFiles/images/hurricane.gif")
    t.shape("LEC/StarterFiles/images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()

    # your code to animate Irma here

    lon = []
    lat = []
    wind = []
    float_lon = []
    float_lat = []
    wind_float = []
        
        
    data = open("LEC/StarterFiles/data/irma.csv", "r")
    separate_line = data.readlines()
    for line in separate_line[1:]:
        line = line.strip()
        list_of_line_data = line.split(',') 
        lon.append(list_of_line_data[3])
        lat.append(list_of_line_data[2])
        wind.append(list_of_line_data[4])
    
    for x in lon:
        float_lon.append(float(x))
        
    print(len(float_lon))
    print()
    
    for y in lat:
        float_lat.append(float(y))
        
    print(float_lat)

    for new_wind in wind:
        wind_float.append(float(new_wind))


# trying out the use of dictionaries here
    caty = ['', '1', '2', '3', '4', '5']
    category = {}
    for cycl in range(6):
        category[cycl] = [caty[cycl]]


    def makeline(x, y, wind, category):
        
        for B in range(len(x)):
            t.goto(x[B], y[B])
            
            
            if 0 <= wind[B] <= 74:
                list1 = category[0]
                t.color("White")
                t.width(1)
                t.write(list1[0], font=("Arial", 10, "normal")) #this uses the dictionary to write the category number on the map
                
            elif 74 < wind[B] <= 95:
                list1 = category[1]
                t.color("Blue")
                t.width(2)
                t.write(list1[0], font=("Arial", 10, "normal")) #so does this one
                
            elif 95 < wind[B] <= 110:
                list1 = category[2]
                t.color("Green")
                t.width(3)
                t.write(list1[0], font=("Arial", 10, "normal")) #and this one
                
            elif 111 <= wind[B] <= 129:
                list1 = category[3]
                t.color("Yellow")
                t.width(4)
                t.write(list1[0], font=("Arial", 10, "normal")) #this one too
                
            elif 130 <= wind[B] <= 156:
                list1 = category[4]
                t.color("Orange")
                t.width(5)
                t.write(list1[0], font=("Arial", 10, "normal")) #as well as this one
                
            elif wind[B] > 156:
                list1 = category[5]
                t.color("Red")
                t.width(6)
                t.write(list1[0], font=("Arial", 10, "normal")) #and lastly this one too lol
                

    makeline(float_lon, float_lat, wind_float, category)
    wn.exitonclick()
        
if __name__ == "__main__":
    irma()