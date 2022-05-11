import csv


 def get(self, request):
        result = []

        with open('hotnow_data.csv', mode='r') as blog_lists:
            reader = csv.reader(blog_lists)

            for list in reader:
                result.append(list)

        return JsonResponse({'search list' : result}, status=200)
    
def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="hotnow_data.csv"'

    writer = csv.writer(response)
    print(writer)
    
    return response