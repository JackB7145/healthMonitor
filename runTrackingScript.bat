shutdown -s -t 1800
msg * Computer will shutdown in 30 minutes. Remember to shower and wash face after!
cd ./progress
start powershell -Command "Get-Process | Where-Object { $_.MainWindowTitle -and $_.Name -ne 'cmd' } | Stop-Process -Force"
python trackingScript.py