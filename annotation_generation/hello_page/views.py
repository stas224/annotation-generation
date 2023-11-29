from django.shortcuts import render

from .model import generate_response


def method(request):

    output_text = ''
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')
        annotation, plan = generate_response(input_text)
        output_text = 'Аннотация:\n{}\nПлан:\n{}'.format(annotation, plan)
    context = {'output_text': output_text}

    return render(request, 'index.html', context)

