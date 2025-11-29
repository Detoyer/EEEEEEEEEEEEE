# from pyscript import Element
from js import document
from pyodide.ffi import create_proxy
import js

# # volume = 0
# #Color Input
# print("Color of slab: \n" \
# "1. Grey \n" \
# "2. Red \n" \
# "3. Green \n" \
# "4. Custom")
# color = int(input("Which color do you want?: "))
# while color > 4 or color < 1:
#     print("That is not a valid option")
#     color = int(input("Which color do you want?: "))
# match color :
#     case 1:
#         color = "Grey"
#         price = 1
#     case 2:
#         color = "Red"
#         price = 2
#     case 3: 
#         color = "Green"
#         price = 2
#     case 4:
#         color = input("Enter a custom color: ")
#         price = 3



# #Depth Input
# print("Depth of slab (mm): \n" \
# "1. 38 \n" \
# "2. 45")
# depth = int(input("What depth do you want?: "))
# while depth > 2 or depth < 1:
#     print("That is not a valid option")
#     depth = int(input("What depth do you want?: "))
# depth = 38 if depth == 1 else 45

# #Shape/Size Input
# print("Shape and size (mm) of slab: \n" \
# "1. Square, 600 x 600 \n" \
# "2. Square, 450 x 450 \n" \
# "3. Rectangle, 600 x 700 \n" \
# "4. Rectangle, 600 x 450 \n" \
# "5. Round, Diameter of 300 \n" \
# "6. Round, Diameter of 450")
# shapeSize = int(input("Which shape and size do you want?: "))
# while shapeSize > 6 or shapeSize < 1:
#     print("That is not a valid option")
#     shapeSize = int(input("Which shape and size do you want?: "))


# print("These are the options you selected: \n" 
#     f"Color: {color} \n" 
#     f"Depth: {depth}mm \n" 
#     f"Volume: {volume}mm\u00b3")

# print("Please note that orders are only supplied in multiples of 20 slabs")
# numofslabs = int(input("How much slabs do you want?(20-100): "))
# while numofslabs < 20 or numofslabs > 100:
#     print("Invalid number")
#     numofslabs = input("Please reenter the amount of slabs.(20-100): ")

# if grade == 1:
#     grade = "Base quality concrete"
# else:
#     grade = "High quality concrete"

# print("These are your order details \n" \
#     f"Amount of slabs: {numofslabs} \n"
#     f"Grade of concrete: {grade} \n"
#     f"Order price: ${price:.2f}")

def calculatevolume(shapeSize, depth):
    volume = 0
    match shapeSize:
        case 1:
            volume = depth * 600 * 600
        case 2:
            volume = depth * 450 * 450
        case 3:
            volume = depth * 600 * 700
        case 4:
            volume = depth * 600 * 450
        case 5:
            volume = depth * (22/7) * (300/2)**2
        case 6:
            volume = depth * (22/7) * (450/2)**2
    return volume

def validatenumofslabs(numofslabs):
    if numofslabs%20 != 0:
        numofslabs = (numofslabs - numofslabs%20) + 20
    if numofslabs > 100:
        numofslabs = 100
    return numofslabs

def calculateprice(color,depth,shapeSize,grade,numofslabs):
    price = 0
    volume = calculatevolume(int(shapeSize),int(depth))
    numofslabs = validatenumofslabs(numofslabs)
    volume = volume * numofslabs
    match color:
        case 1:
            price = (volume/100000) * 0.05
        case 2:
            price = (volume/100000) * 0.055
        case 3:
            price = ((volume/100000) * 0.0575) + 5
    
    if grade == 2:
        price = price * 1.07

    document.getElementById("price").innerHTML = (f"Total: ${price:.2fz}")

# def calculate(event):
#     color = document.getElementById("color").value
#     depth = document.getElementById("depth").value
#     shapeSize = document.getElementById("shapeSize").value
#     grade = document.getElementById("grade").value
#     numofslabs = document.getElementById("numofslabs").value
#     calculateprice(int(color),int(depth),int(shapeSize),int(grade),int(numofslabs))

def showPrice():
    color = document.getElementById("color").value
    depth = document.getElementById("depth").value
    shapeSize = document.getElementById("shapeSize").value
    grade = document.getElementById("grade").value
    numofslabs = document.getElementById("numofslabs").value
    price = 0
    volume = calculatevolume(int(shapeSize),int(depth))
    numofslabs = validatenumofslabs(numofslabs)
    volume = volume * numofslabs
    match color:
        case 1:
            price = (volume/100000) * 0.05
        case 2:
            price = (volume/100000) * 0.055
        case 3:
            price = ((volume/100000) * 0.0575) + 5
        

def select(event):
    # event.stopPropagation()
    event.preventDefault()
    parent = event.target.closest(".shape")
    child = parent.querySelector("input")
    if child.value == "1":
        text = '''<label class="container"><div id="pad">600 x 600</div>
                        <input type="radio" class="shapeSize" name="radio1" value="tbd">
                        <span class="checkmark"></span>
                    </label>
                    
                    <label class="container"><div id="pad">450 x 450</div>
                        <input type="radio" name="radio1" value="tbd">
                        <span class="checkmark"></span>
                    </label>'''
    elif child.value == "2":
        text = '''<label class="container"><div id="pad">600 x 700</div>
                        <input type="radio" class="shapeSize" name="radio1" value="tbd">
                        <span class="checkmark"></span>
                    </label>
                    
                    <label class="container"><div id="pad">600 x 450</div>
                        <input type="radio" name="radio1" value="tbd">
                        <span class="checkmark"></span>
                    </label>'''
    else:
        text = '''<label class="container"><div id="pad">Diameter of 300</div>
                        <input type="radio" class="shapeSize" name="radio1" value="tbd">
                        <span class="checkmark"></span>
                    </label>
                    
                    <label class="container"><div id="pad">Diameter of 450</div>
                        <input type="radio" name="radio1" value="tbd">
                        <span class="checkmark"></span>
                    </label>'''
    
    document.getElementById("checkbox2").innerHTML = (text)
    
    radios = document.querySelectorAll('input[name="radio"]')
    for radio in radios:
        radio.checked = False

    child.checked = True

# js.alert("Script is running!")  
js.console.log("Script is running")

click = create_proxy(select)
pad = document.getElementsByClassName("shape")
for elements in pad:
    elements.addEventListener("click", click)

calc = create_proxy(showPrice)
variable1 = document.getElementById("calculate")
variable1.addEventListener("click", calc)