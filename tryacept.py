try:
  print("hello")
  print("let's divide!")
  num= int(input("number:"))
  result= (21/num)

except:
        print("oops!")
        result= "ya done screwed up"
finally:
    print(result)
