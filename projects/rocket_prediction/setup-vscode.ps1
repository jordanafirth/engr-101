$ErrorActionPreference = 'Stop'
$courseRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '../..')).Path
$manifestPath = Join-Path $courseRoot 'pixi.toml'
$localPixi = Join-Path $courseRoot '.tools/pixi/pixi.exe'
if (Test-Path -LiteralPath $localPixi) {
    $pixiPath = $localPixi
} else {
    $pixiPath = (Get-Command pixi -ErrorAction Stop).Source
}

& $pixiPath install --manifest-path $manifestPath --locked
if ($LASTEXITCODE -ne 0) { throw 'Pixi installation failed. Resolve the error above and rerun setup.' }

# Launch through Pixi so Windows native libraries receive the activated PATH.
$kernelDirectory = Join-Path $PSScriptRoot 'outputs/vscode-kernel'
New-Item -ItemType Directory -Force -Path $kernelDirectory | Out-Null
$kernelSpec = @{
    argv = @($pixiPath, 'run', '--manifest-path', $manifestPath, '--locked',
             'python', '-m', 'ipykernel_launcher', '-f', '{connection_file}')
    display_name = 'Engr 101 Rocket (Pixi)'
    language = 'python'
}
$kernelSpec | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $kernelDirectory 'kernel.json') -Encoding UTF8
& $pixiPath run --manifest-path $manifestPath --locked python -m jupyter kernelspec install --user --replace --name engr101-rocket $kernelDirectory
if ($LASTEXITCODE -ne 0) { throw 'Notebook kernel registration failed.' }
Write-Host 'Setup complete. In VS Code select the Engr 101 Rocket (Pixi) notebook kernel.'
