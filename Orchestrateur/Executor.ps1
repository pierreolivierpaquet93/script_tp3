param(
	[parameter(Mandatory=$true)][string]$machine,
	[parameter(Mandatory=$true)][string]$logiciel
)

<#

https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-random?view=powershell-7.5

#>

$DelayMin = 0.1
$DelayMax = 1

$delay = Get-Random -Minimum $DelayMin -Maximum $DelayMax

Start-Sleep -Seconds $delay

function Install($installation_state){
	$installation_state["Duration"] = 666
}

function Main(
	[string]$computer,
	[string]$program
){
	$installation_state = @{
		"Machine" = $computer;
		"Logiciel" = $program;
		"Duration" = -1;
		"Result" = $false
	}
	Install $installation_state
	Write-Host $installation_state["Duration"]
	exit(0)
}

Main $machine $logiciel
