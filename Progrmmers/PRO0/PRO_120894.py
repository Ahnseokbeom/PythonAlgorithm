def solution(numbers):
    word_dict = {
        'zero': '0','one': '1','two': '2','three': '3','four': '4',
        'five': '5','six': '6','seven': '7','eight': '8','nine': '9'
    }
    
    for word, num in word_dict.items():
        numbers = numbers.replace(word, num)
    return int(numbers

print(solution("onetwothreefourfivesixseveneightnine"))
print(solution("onefourzerosixseven"))
