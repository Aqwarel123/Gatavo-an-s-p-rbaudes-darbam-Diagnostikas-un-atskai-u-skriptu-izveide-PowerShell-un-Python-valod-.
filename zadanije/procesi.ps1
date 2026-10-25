$lielakie = Get-Process |
    Sort-Object WorkingSet -Descending |
    Select-Object -First 10 Name, WorkingSet

$lielakie | Export-Csv -Path "procesi.csv" -NoTypeInformation -Encoding UTF8
