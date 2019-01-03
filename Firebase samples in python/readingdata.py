from firebase.firebase import FirebaseApplication
fb=FirebaseApplication("https://mubin-22b7e.firebaseio.com/",None)
d1=fb.get("stock",None)
print(d1)
