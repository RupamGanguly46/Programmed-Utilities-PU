param (
    [string]$ssid,
    [string]$password
)

# Ensure the Temp directory exists
if (-Not (Test-Path -Path "C:\Temp")) {
    New-Item -ItemType Directory -Path "C:\Temp"
}

# Generate the Wi-Fi profile XML content
$profileXml = @"
<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>$ssid</name>
    <SSIDConfig>
        <SSID>
            <name>$ssid</name>
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
                <keyMaterial>$password</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>
"@

# Save the profile XML to a file
$profilePath = "C:\Temp\wifi_profile.xml"
$profileXml | Out-File -FilePath $profilePath -Encoding utf8

Write-Host "Profile XML created at: $profilePath"

# Add the Wi-Fi profile
$addProfileResult = netsh wlan add profile filename=$profilePath

# Check if profile was added successfully
if ($addProfileResult -match "added on interface") {
    Write-Host "Profile added successfully."
    # Attempt to connect to the Wi-Fi network using the new profile
    $connectResult = netsh wlan connect name=$ssid
    Write-Host "Connection result: $connectResult"
} else {
    Write-Host "Failed to add profile."
    Write-Host $addProfileResult
}

# Clean up the temporary profile file
Remove-Item -Path $profilePath
