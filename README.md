# meraki_logs_downloader
Simple script to bulk download Cisco Meraki MX Logs.

By default, Cisco Meraki portal only allows you to export 1 page of logs at a time.  This simple script uses the Meraki API to download up to 1000 log entries per site from MX devices and writes them to a CSV file.


To run:

python3 meraki_logs.py

You will need your Cisco Meraki API Key (docs found here: https://documentation.meraki.com/General_Administration/Other_Topics/Cisco_Meraki_Dashboard_API)

The script will prompt you to paste in your API key and the file name to write to.
