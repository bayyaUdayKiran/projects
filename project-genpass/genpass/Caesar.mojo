fn ordify(s: String) -> Int:
    var num: String = ""
    for ch in s:
        num+=(ord(ch))

    var res: Int

    try:
        res = alot(num)
    except:
        print("method 'alot()' only accepts integers")
    
    return res


fn main():
   print(ordify("Hello World"))
