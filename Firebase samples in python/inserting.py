from firebase.firebase import firebaseApplication
fb=firebaseApplication("https://mubin-22b7e.firebaseio.com/",None)
while True:
    pno=int(input("Enter product no:"))
    pname=input("Enter product name:")
    pprice=float(input("Enter product price:"))
    pqty=int(input("Enter product Quantity"))
    d1={"pno":pno,"name":pname,"price":pprice,"quantity":pqty}
    fb.put("stock",pno,d1)
    print(pno,"product is saved")
    ans=input("To continue type y/Y:")
    if ans=="Y" or ans=="y":
        continue
    else:
        break
