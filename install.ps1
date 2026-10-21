$ErrorActionPreference = "Stop"

$taskName = "Downloads Organizer"
$scriptPath = Join-Path $PSScriptRoot "organize.py"

$pythonOutput = & py -c "import sys; print(sys.executable)"

if ($LASTEXITCODE -ne 0) {
    throw "Could not locate Python."
}

$pythonPath = ($pythonOutput | Out-String).Trim()
$pythonwPath = Join-Path (Split-Path -Parent $pythonPath) "pythonw.exe"

if (-not (Test-Path -LiteralPath $scriptPath -PathType Leaf)) {
    throw "Organizer script not found: $scriptPath"
}

if (-not (Test-Path -LiteralPath $pythonwPath -PathType Leaf)) {
    throw "Python windowless executable not found: $pythonwPath"
}

$currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name

$action = New-ScheduledTaskAction `
    -Execute $pythonwPath `
    -Argument ('"{0}"' -f $scriptPath) `
    -WorkingDirectory $PSScriptRoot

$trigger = New-ScheduledTaskTrigger -AtLogOn -User $currentUser

$principal = New-ScheduledTaskPrincipal `
    -UserId $currentUser `
    -LogonType Interactive `
    -RunLevel Limited

$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -MultipleInstances IgnoreNew `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 10)

$task = New-ScheduledTask `
    -Action $action `
    -Trigger $trigger `
    -Principal $principal `
    -Settings $settings `
    -Description "Organize downloaded files once at user logon."

Register-ScheduledTask `
    -TaskName $taskName `
    -InputObject $task `
    -Force | Out-Null

Write-Output "Scheduled task installed: $taskName"
Write-Output "The organizer will run once at each user logon."
