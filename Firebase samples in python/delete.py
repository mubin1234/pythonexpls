from firebase.firebase import FirebaseApplication
fb=FirebaseApplication("https://mubin-22b7e.firebaseio.com/",None)
pno=int(input("Enter product no to delete:"))
fb.delete("stock",pno)
print(pno,"product deleted")
