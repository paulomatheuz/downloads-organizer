$ErrorActionPreference = "Stop"

$taskName = "Downloads Organizer"
$task = Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue

if ($null -ne $task) {
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
    Write-Output "Scheduled task removed: $taskName"
} else {
    Write-Output "Scheduled task is not installed."
}
