from django.shortcuts import render, get_object_or_404
from .models import Part, Category

# Create your views here.
def index(request):
    part_list=Part.objects.all()
    context={'part_list': part_list}
    return render(request, 'archinator/part_list.html', context)

def detail(request, part_id): ##부위 별 세부 시나리오 표시
    part=get_object_or_404(Part, pk=part_id)
    symptom_list=part.category_set.all()
    context={'symptom_list': symptom_list, 'part': part}
    return render(request, 'archinator/part_detail.html', context)

def diagnose(request, part_id, symptom_id): ##시나리오 별 질문
    part=get_object_or_404(Part, pk=part_id)
    symptom_list=part.category_set.all()
    symptom=symptom_list.get(id=symptom_id)
    context={'symptom': symptom, 'part': part}
    html='archinator/'+str(part_id)+'/'+str(symptom_id)+'.html'
    # diseases[part_id(부위)][symptom_id(시나리오)]= ['가능한 질병 리스트']
    return render(request, html, context)

def question(request, part_id, symptom_id, question_num):
    part=get_object_or_404(Part, pk=part_id)
    symptom_list=part.category_set.all()
    symptom=symptom_list.get(id=symptom_id)
    context={'symptom': symptom, 'part': part}
    html='archinator/'+str(part_id)+'/'+str(symptom_id)+'-'+str(question_num)+'.html'
    return render(request, html, context)

