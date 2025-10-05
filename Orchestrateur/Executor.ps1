param(
	[parameter(Mandatory=$true)][string]$machine,
	[parameter(Mandatory=$true)][string]$logiciel,
	[float]$DelayMin = 0.1,
	[float]$DelayMax = 1
)

<#

https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-random?view=powershell-7.5

#>

function Install($installation_state){
	$delay = Get-Random -Minimum $DelayMin -Maximum $DelayMax
	Start-Sleep -Seconds $delay
	$installation_state["Duration"] = $delay
	$installation_state["Result"] = $true, $false | Get-Random
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
	Write-Host $installation_state["Result"]
	exit(0)
}

Main $machine $logiciel
