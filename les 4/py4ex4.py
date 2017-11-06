def new_password(oldPassword, newPassword):
    if newPassword != oldPassword and len(newPassword) >= 6:
            return True
    return False

invoerOldPassword = input('geef hier je oude wachtwoord op: ')
invoerNewPassword = input('geef hier je nieuwe wachtwoord op: ')
print(new_password(invoerNewPassword, invoerOldPassword))