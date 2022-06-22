from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datahandler
import pandas as pd
import s3fileHandler

    
# Create your views here.
def index(request):
    print("here")
    return HttpResponse("Hello world")

@csrf_exempt
def getTopLanguages(request):
    print("this is lang request")
    print(request)
    print("I'm here")
    # body_unicode = request.body.decode('utf-8')
    # body_data = json.loads(body_unicode)
    if request.method=='GET':
        top_languages = datahandler.get_top_languages()
        top_languages = pd.DataFrame(top_languages,columns=['Languages'])
        file_name = "./outputFiles/" + "languages" + ".csv"
        top_languages.to_csv(file_name)
        s3fileHandler.uploadToS3(file_name)
        return JsonResponse("File has been generated and uploaded successfully",safe=False)
    return JsonResponse("Failed",safe=False)



@csrf_exempt
def getTopStates(request):
    print(request)
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    if request.method=='GET':
        for rec in body_data:
            language = rec['language']
            top_states = datahandler.get_top_states(language=language)
            top_states = pd.DataFrame(top_states,columns=['top_states'])
            file_name = "./outputFiles/" + "top_states" + ".csv"
            top_states.to_csv(file_name)
            s3fileHandler.uploadToS3(file_name)
            return JsonResponse("File has been generated and uploaded successfully",safe=False)
        return JsonResponse("Failed",safe=False)

@csrf_exempt
def getTopCities(request):
    print(request)
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    if request.method=='GET':
        for rec in body_data:
            state = rec['state']
            top_cities = datahandler.get_top_cities(state=state)
            top_cities = pd.DataFrame(top_cities,columns=['top_cities'])
            file_name = "./outputFiles/" + "top_cities" + ".csv"
            top_cities.to_csv(file_name)
            s3fileHandler.uploadToS3(file_name)
            return JsonResponse("File has been generated and uploaded successfully",safe=False)
        return JsonResponse("Failed",safe=False)

@csrf_exempt
def getCategories(request):
    print("hey there")
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    if request.method=='GET':
        for rec in body_data:
            language = rec['language']
            # preference = rec['preference']
            city = rec['city']
            top_categories = datahandler.get_top_categories(language=language, city=city)
            top_categories = pd.DataFrame(top_categories,columns=['top_categories'])
            file_name = "./outputFiles/" + "top_categories" + ".csv"
            top_categories.to_csv(file_name)
            s3fileHandler.uploadToS3(file_name)
            return JsonResponse("File has been generated and uploaded successfully",safe=False)
        return JsonResponse("Failed",safe=False)

@csrf_exempt
def getSubCategories(request):
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    if request.method=='GET':
        for rec in body_data:
            language = rec['language']
            city = rec['city']
            category = rec['category']

            subCategories = datahandler.get_top_subcategories(language=language, city=city, category=category)
            subCategories = pd.DataFrame(subCategories,columns=['subCategories'])
            file_name = "./outputFiles/" + "subCategories" + ".csv"
            subCategories.to_csv(file_name)
            s3fileHandler.uploadToS3(file_name)
            return JsonResponse("File has been generated and uploaded successfully",safe=False)
        return JsonResponse("Failed",safe=False)

@csrf_exempt
def getMicroCategories(request):
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    if request.method == 'GET':
        for rec in body_data:
            language = rec['language']
            city = rec['city']
            category = rec['category']
            subcategory = rec['subcategory']

            microCategories = datahandler.get_top_microcategories(language=language, city=city, category=category, subcategory=subcategory)
            microCategories = pd.DataFrame(microCategories,columns=['microCategories'])
            file_name = "./outputFiles/" + "microCategories" + ".csv"
            microCategories.to_csv(file_name)
            s3fileHandler.uploadToS3(file_name)
            return JsonResponse("File has been generated and uploaded successfully",safe=False)        
        return JsonResponse("Failed",safe=False)

@csrf_exempt
def getProducts(request):
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    if request.method == 'GET':
        for rec in body_data:
            language = rec['language']
            city = rec['city']
            category = rec['category']
            subcategory = rec['subcategory']
            microcategory = rec['microcategory']

            products = datahandler.get_top_products(language=language, city=city, category=category, subcategory=subcategory, microcategory=microcategory)
            products = pd.DataFrame(products,columns=['products'])
            file_name = "./outputFiles/" + "products" + ".csv"
            products.to_csv(file_name)
            s3fileHandler.uploadToS3(file_name)
            return JsonResponse("File has been generated and uploaded successfully",safe=False)
        return JsonResponse("Failed",safe=False)

