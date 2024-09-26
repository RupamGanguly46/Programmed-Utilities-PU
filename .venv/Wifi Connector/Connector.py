import subprocess
import os

def check_profile_exists(ssid):
    # Run the netsh command to show profiles
    result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error checking profiles: {result.stderr}")
        return False

    # Check if the SSID is in the list of profiles
    return ssid in result.stdout


def create_profile(ssid, password):
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
    result = subprocess.run(["netsh", "wlan", "add", "profile", f"filename={profile_file}"], capture_output=True,
                            text=True)
    if result.returncode != 0:
        print(f"Error adding profile: {result.stderr}")
        return False

    os.remove(profile_file)
    return True


def connect_to_wifi(ssid, password):
    if check_profile_exists(ssid):
        print(f"Profile for {ssid} already exists. Connecting using existing profile...")
    else:
        print(f"Profile for {ssid} does not exist. Creating profile...")
        if not create_profile(ssid, password):
            print("Failed to create profile.")
            return

    # Connect to the network
    result = subprocess.run(["netsh", "wlan", "connect", f"name={ssid}"], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Successfully connected to {ssid}")
    else:
        print(f"Failed to connect to {ssid}: {result.stderr}")


# Example usage
ssid = "Shubh"
password = "        "
connect_to_wifi(ssid, password)


