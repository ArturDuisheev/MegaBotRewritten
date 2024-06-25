
function Get-ADUserByUsername {
    param (
        [string]$username
    )
    try {
        $user = Get-ADUser -Filter {SamAccountName -eq $username}
        return $user
    } catch {
        Write-Output "Ошибка: Не удалось найти пользователя с логином $username"
        exit 1
    }
}
