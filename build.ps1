$exclude = @("venv", "formsPOO.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "formsPOO.zip" -Force