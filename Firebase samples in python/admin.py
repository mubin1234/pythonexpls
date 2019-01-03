from firebase.firebase import FirebaseApplication
fb=FirebaseApplication("https://mubin-22b7e.firebaseio.com/",None)
fb.put("mubin","admin",{"username":"admin","password":"admin"})
print("admin account is created in database")
