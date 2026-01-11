# views



from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def product_list(request):

    if request.method == "POST":

        json_data = request.body            # <type:raw bytes> 
        print("request body data",type(json_data))

        stream  = "io.BytesIO"(json_data)    # <type:i0_bytes>

        print("converted into bytes io data",type(stream))

        python_data = "JSONParser()".parse(stream) # <type:python_dict>

        my_serializer =  "ProductSerializer"(data=python_data)
        my_serializer.is_valid(raise_exception=True)
        my_serializer.save()

        return "HttpResponse"(my_serializer.data)
    
    return "HttpResponse"("Only post method allowed to this api endpoint")
        

        

"request.body contains raw bytes , and request.data is alreadt parsed into python dict before even request reacing to the views drf does it automatically"