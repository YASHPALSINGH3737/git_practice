def username_generator(first_name, last_name):
  if len(first_name) < 4 or len(last_name) < 5:
    if len(first_name) < 4 and len(last_name) < 5:
      username = first_name+last_name
    elif len(first_name) < 4 or not len(last_name) < 5:
      username = first_name + last_name[:4]
    else:
      username = first_name[:3] + last_name
  else:
    username = first_name[:3] + last_name[:4]
  return username

def password_generator(username):
  password = ""
  for i in range(len(username)):
    password += username[i - 1]
  
  return password


