from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'Nama': 'Muhammad Mariozulfandy',
        'Kelas': 'PBP C',
        'Aplikasi': 'Book List'
    }

    return render(request, "main.html", context)