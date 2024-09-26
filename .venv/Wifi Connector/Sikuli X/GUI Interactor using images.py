# SikuliX Script to connect to Wi-Fi networks

# Define your passwords
passwords = ["password1", "password2", "password3"]

# Click on the Wi-Fi icon (you need to have an image of the icon saved)
click("path/to/wifi_icon.png")

# Wait for the available networks menu to appear
wait(1)

# Loop through available networks
for i in range(3):  # Adjust based on the number of passwords
    # Click on the network (you need an image of the network)
    click("path/to/network_image.png")

    # Enter the password
    type(passwords[i])
    type(Key.ENTER)

    # Wait for a connection attempt
    wait(5)

    # Check if connected (implement your check here)
    if is_connected():  # Placeholder function
        popup("Connected to network: " + str(i))
        break

def is_connected():
    # Implement a check to see if connected to Wi-Fi
    return False  # Placeholder