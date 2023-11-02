#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import DocketForm

def create_docket(request):
    if request.method == 'POST':
        form = DocketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('docket_list')  # Assuming you'll have a view for listing dockets
    else:
        form = DocketForm()

    form = {'insert_me': "I am a text from Home/Views.py"}
    return render(request, 'create_docket.html',  {'form': form})

