import subprocess
import os

def create_and_add_wifi_profile(ssid, password):
    # Path to the PowerShell script
    ps_script_path = os.path.abspath(r"C:\Users\HP\PycharmProjects\Programmed Utilities - PU\.venv\Wifi Connector\CreateWiFiProfile.ps1")

    try:
        # Run the PowerShell script to create and add the Wi-Fi profile
        result = subprocess.run(
            ["C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe", "-ExecutionPolicy", "Bypass", "-File", ps_script_path, "-ssid", ssid, "-password", password],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print("Error adding profile or connecting:")
            print(result.stderr)
        else:
            print("Profile added and connection attempt made.")
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error adding profile or connecting: {e.stderr}")

# Example usage
ssid = "Shubh"
password = "        "
create_and_add_wifi_profile(ssid, password)
