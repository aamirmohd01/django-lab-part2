from django.shortcuts import render

def analyze_text(request, sentence):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    vowel_list = [char for char in sentence if char in vowels]
    consonant_list = [char for char in sentence if char in consonants]
    
    context = {
        'sentence': sentence,
        'num_vowels': len(vowel_list),
        'num_consonants': len(consonant_list),
        'vowel_list': vowel_list,
        'consonant_list': consonant_list,
    }
    
    return render(request, 'analysis_app/analyze.html', context)
