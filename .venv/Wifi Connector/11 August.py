import subprocess
import os

def create_and_add_wifi_profile(ssid, password):
    # Create a temporary XML profile with plain text password
    profile_xml = """<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
	<name>Shubh</name>
	<SSIDConfig>
		<SSID>
			<hex>5368756268</hex>
			<name>Shubh</name>
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
				<protected>true</protected>
				<keyMaterial>01000000D08C9DDF0115D1118C7A00C04FC297EB01000000E9BBCF4CF8963445B7745EE850B34E110000000002000000000010660000000100002000000037288A30645916CB4890D4075630F09ED3C851D1864DF6559E8290D4BFEBCD40000000000E80000000020000200000000B3E93E3934454A39736CDCBF67D9335F9C68DD5B3FB77FAF87050D40914694D10000000916068C9E76409245F8E55A83E4C48EF40000000A9FE5728D652C2C90667199B741BC2ED66B7B50C916A9B5721120FF909A44D1A2CBB40F8F32264D34C3B4A31B52128A82BA1DF316D3A3DE57405A9D54F9448D1</keyMaterial>
			</sharedKey>
		</security>
	</MSM>
	<MacRandomization xmlns="http://www.microsoft.com/networking/WLAN/profile/v3">
		<enableRandomization>false</enableRandomization>
	</MacRandomization>
</WLANProfile>
"""

    # Save the profile to an XML file
    xml_file_path = "temp_wifi_profile.xml"
    with open(xml_file_path, "w") as file:
        file.write(profile_xml)

    try:
        # Check the generated XML file content
        with open(xml_file_path, "r") as file:
            print("Generated XML profile:")
            print(file.read())

        # Add the profile using netsh
        result = subprocess.run(
            ["netsh", "wlan", "add", "profile", f"filename={xml_file_path}"],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print("Error adding profile:")
            print(result.stderr)
        else:
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
