Import-Module ActiveDirectory

. .\get_user.ps1

function Disable-ADUserAccount {
    param (
        [string]$username
    )
    try {
        Disable-ADAccount -Identity $username
        Write-Output "Пользователь $username был успешно заблокирован."
    } catch {
        Write-Output "Ошибка: Не удалось заблокировать пользователя $username"
        exit 1
    }
}

param (
    [string]$username
)

$user = Get-ADUserByUsername -username $username
if ($user) {
    Write-Output "Найден пользователь: $($user.Name) ($($user.SamAccountName))"
    Disable-ADUserAccount -username $user.SamAccountName
} else {
    Write-Output "Ошибка: Пользователь с логином $username не найден."
}
