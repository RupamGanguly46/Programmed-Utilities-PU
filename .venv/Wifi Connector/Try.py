import subprocess
import os

def create_and_add_wifi_profile(ssid, password):
    # Create a temporary XML profile with plain text password
    profile_xml = f"""<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>{ssid}</name>
    <SSIDConfig>
        <SSID>
            <name>{ssid}</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>{password}</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>"""

    # Save the profile to an XML file
    xml_file_path = "temp_wifi_profile.xml"
    with open(xml_file_path, "w") as file:
        file.write(profile_xml)

    try:
        # Add the profile using netsh
        subprocess.run(
            ["netsh", "wlan", "add", "profile", f"filename={xml_file_path}"],
            check=True,
            capture_output=True,
            text=True
        )
        print("Profile added successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error adding profile: {e.stderr}")
    finally:
        # Clean up the temporary XML file
        os.remove(xml_file_path)

# Example usage
ssid = "Shubh"
password = "        "
create_and_add_wifi_profile(ssid, password)
