import subprocess

def list_available_ssids():
    # Run the netsh command to get a list of available networks
    result = subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True)

    # Check if the command was successful
    if result.returncode != 0:
        print("Error retrieving networks")
        print(result.stderr)
        return

    # Extract SSIDs from the output
    ssid_list = []
    for line in result.stdout.splitlines():
        if "SSID" in line:
            parts = line.split(":")
            if len(parts) == 2:
                ssid = parts[1].strip()
                if ssid and ssid != "Network":
                    ssid_list.append(ssid)

    return ssid_list


# Fetch and print the list of available SSIDs
def display_networks():
    available_ssids = list_available_ssids()
    if available_ssids:
        print("Available WiFi Networks:")
        for ssid in available_ssids:
            print(ssid)
    else:
        print("No WiFi networks found.")


import subprocess

def connect_to_wifi(ssid, password):
    # Define the profile name
    profile_name = ssid

    # Create a profile XML for the network
    profile_xml = f"""
    <?xml version="1.0"?>
    <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
        <name>{profile_name}</name>
        <SSIDConfig>
            <SSID>
                <name>{ssid}</name>
            </SSID>
        </SSIDConfig>
        <connectionType>ESS</connectionType>
        <connectionMode>auto</connectionMode>
        <MSM>
            <security>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <keyMaterial>{password}</keyMaterial>
            </security>
        </MSM>
    </WLANProfile>
    """

    # Save the XML to a file
    profile_file = "wifi_profile.xml"
    with open(profile_file, "w") as file:
        file.write(profile_xml)

    # Add the profile
    result = subprocess.run(["netsh", "wlan", "add", "profile", f"filename={profile_file}"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error adding profile: {result.stderr}")
        return

    # Connect to the network
    result = subprocess.run(["netsh", "wlan", "connect", f"name={profile_name}"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error connecting to network: {result.stderr}")
        return

    print(f"Connected to {ssid} successfully")


# Example usage
ssid = "Shubh"
password = "        "
connect_to_wifi(ssid, password)


