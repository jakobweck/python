reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Appraiser" /v UtcOnetimeSend /t REG_DWORD /d 1 /f

schtasks /run /TN "\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser"

:CompatCheckRunning

schtasks /query /TN "\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser" | findstr Ready >nul

if NOT "%errorlevel%" == "0" ping localhost >nul &goto :CompatCheckRunning

schtasks /run /TN "\Microsoft\Windows\Setup\gwx\refreshgwxconfig"
