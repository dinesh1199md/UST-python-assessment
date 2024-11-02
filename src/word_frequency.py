
def frequency_check(text):
    words=text.split()
    word={x:words.count(x) for x in words }
    alpnum_sort={k:v for k,v in sorted(word.items(),key= lambda e:e[0])}.items()
    return list(alpnum_sort)

def word_frequency():
    try:
        input_file_path = "input_data/word_frequency_input.txt"
        with open(input_file_path,"r") as file:
            texts=file.read().strip()
        if texts:
            frq_result=frequency_check(texts)
            print("Word frequency sorted alphanumerically :\n",frq_result)
            print()
        else:
            print("Please Check the inputfile")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print("Exception @word_frequency:",e)