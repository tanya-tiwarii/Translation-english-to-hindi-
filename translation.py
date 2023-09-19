from googletrans import Translator

def trans(para):
    translator = Translator()
    out=translator.translate(para,dest='hi')
    return out.text

def main():
    text2 = input("Enter paragraph: \n")
    trans_text = trans(text2)
    print(trans_text)
    
if __name__ == "__main__":
    main()
os.system("pause")