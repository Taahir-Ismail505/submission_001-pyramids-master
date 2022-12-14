####################################################################################################################

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    '''
    takes user input and directs it to specific shapes
    '''
    shape = input("Shape?: ").lower()
    if shape == 'pyramid' or shape == 'square' or shape == 'triangle' or shape =='diamond' or shape =='rectangle' or shape =='Downtri':      
        return shape
    else:  
        return get_shape()
####################################################################################################################

# TODO: Step 1 - get height (it must be int!)
def get_height():
    '''
    gets user height and checks if input is an interger
    '''
    while True:
        height = input("Height?: ")
        try:
            height=int(height)
        except :
            continue
        break
    if (0<height<81) :
        return height
    else :
        return get_height()

        
        
        
           
        
     
####################################################################################################################

# TODO: Step 2
def draw_pyramid(height, outline):
    '''
    uses height and shape input construct 
    '''
    if outline == False:
        for i in range(1 ,height+1):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            print(" "*(height - i)+ "*"*(2*i-1))
    if outline == True:
        Mstar = 1
        for i in range(1 ,height+1):
            if i == 1 or i == height :
                print(" "*(height - i)+ "*"* Mstar)
     
            if  1 < i < height :
                print(" "*(height - i)+"*" +" "*(Mstar-2) +"*")
            Mstar += 2
####################################################################################################################

# TODO: Step 3
def draw_square(height, outline):
    '''
    uses height and shape input construct 
    '''

    middle = height - 2
    
    if outline == False :
        for i in range(1 ,height+1):
            print("*"*(height)+ ""*i)
    if outline == True :
        print("*" * height)

        for i in range(1, middle+1):
            print("*" +" "*(middle)+"*")
        print("*" * height)
####################################################################################################################    
# TODO: Step 4
def draw_triangle(height, outline):
    '''
    uses height and shape input construct 
    '''

    Mstar = 1     
    if outline == False :
        for i in range (1 ,height+ 1 ):
            print("*"*(i))

    Mstar = 1
    if outline == True :
        Mstar = 1
        #triangle
        for i in range(1 ,height+1):
            if i == 1 or i == height :
                print("* "*(i))

            if  1 < i < height :
                print("*" +" "*(Mstar -2) +"*")
            Mstar += 2

####################################################################################################################
def draw_diamond(height,oultine) :
    '''
    uses height and shape input construct 
    '''
        for  i in range(height , 0, -1) :
            print(" " *(height -i) + "* "* i)
    

####################################################################################################################
    
def draw_Rect(height,outline):
    '''
    uses height and shape input construct 
    '''
    height2 = height +5
    middle = height2  -2 
    if outline == False :
        for i in range(1 ,height+1):
            print("*"*(height2)+ " "*i)
    if outline == True :
        print("*" * height2)
        for i in range(0, middle):
            print("*" +" "*(middle)+"*")
        print("*" * height2)

####################################################################################################################
def draw_upsideDownTRI(height,outline):
    '''
    uses height and shape input construct 
    '''
    if outline== False:
        for i in range(0, height):
            print("*"*(height-i))
    if outline == True :
        for i in range(0, height):
            if i == 0 or i == height-1 or  i == height-2:
                print("*"*(height-i))

            if  0 < i < height-2 :
                print("*"+" "*(height-2-i)+"*")

####################################################################################################################



####################################################################################################################
 # TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    '''
    this acts as a directory for all shapes ..so user input actually gets pushed to this function
    '''
    if shape == "pyramid":
        draw_pyramid(height, outline)
    if shape == "square" :
         draw_square(height, outline)
    if shape == "triangle" :
       draw_triangle(height, outline)     
    if shape == "diamond" :
        draw_diamond(height,outline)
    if shape == "rectangle" :
        draw_Rect(height,outline)
    if shape == "downtri":
        draw_upsideDownTRI(height,outline) 
    
####################################################################################################################
# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    '''
    asks user if they would outline or not..and converts all user input to lowercase
    so that no matter how they type it ,it'll understand
    '''
    outline = input("outline (y/n) :").lower()

    if outline == "y" :
        return True
    if outline == "n" or outline == "" :
        return False  


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

