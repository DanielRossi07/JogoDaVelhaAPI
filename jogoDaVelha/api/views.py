from django.shortcuts import render


def index(request):
    return render(request, "api/index.html")


"""def new_game(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            # Process the JSON data
            return JsonResponse({'message': 'JSON data received', 'data': json_data})
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON data'})


def play(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            # Process the JSON data
            return JsonResponse({'message': 'JSON data received', 'data': json_data})
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON data'})"""


