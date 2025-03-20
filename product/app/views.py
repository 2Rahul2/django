from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.shortcuts import render
from .utils.scrapeReviews import ScrapeAmzonReview

def home(request):
    return render(request, "app/index.html")

def SentimentAnalysis(request):
    productName = request.GET.get("product" ,'')
    if not productName:
        return JsonResponse({"data":"Product name not given"})
    ScrapeReviewObject = ScrapeAmzonReview()
    try:
        product_url = ScrapeReviewObject.search_amazon_product(productName)
        print("product name = " ,productName)
        print("product_url = " ,product_url)
        product_review = ScrapeReviewObject.scrape_amazon_reviews(product_url)
        return JsonResponse({"data":f"Product name recevied : {productName}" ,"review":product_review})
    except:
        return JsonResponse({"data":f"Product name recevied : {productName}" ,"review":"No review found"})

