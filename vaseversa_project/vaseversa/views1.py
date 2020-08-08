from django.shortcuts import render


def home (request):
	return render(request, 'home.html')

def reverse (request):
	user_text = request.GET['usertext']
	reverse_text = user_text[::-1]
	word_count = len(user_text) 
	#print (test_get_text)
	return render(request, 'reverse.html', {'usertext':user_text,
		'reversedtext':reverse_text,'wordcount':word_count})

	#11111111111111
	#22222222222222