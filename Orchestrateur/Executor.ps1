param(
	[parameter(Mandatory=$true)][string]$machine,
	[parameter(Mandatory=$true)][string]$logiciel,
	[float]$DelayMin = 0.1,
	[float]$DelayMax = 1
)

<#

https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-random?view=powershell-7.5

#>

$DurationField = "Duration"
$ResultField = "Result"
$MachineField = "Machine"
$SoftwareField = "Logiciel"

function Install($installationState){
	$delay = Get-Random -Minimum $DelayMin -Maximum $DelayMax
	Start-Sleep -Seconds $delay
	$installationState[$DurationField] = $delay
	$installationState[$ResultField] = 0, 1 | Get-Random
}

function InstallationJson( $InstallationState ){
	$JsonStr = $InstallationState | ConvertTo-Json -Depth 4
	return $JsonStr
}

function Main(
	[string]$computer,
	[string]$program
){
	$InstallationState = @{
		$MachineField = $computer;
		$SoftwareField = $program;
		$DurationField = -1;
		$ResultField = $false
	}
	Install $InstallationState
	Write-Host (InstallationJson $InstallationState)
	return
}

Main $machine $logiciel
