from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.shortcuts import render
from .utils.scrapeReviews import ScrapeAmzonReview
from .utils.gpt_summary import GetSummary
import json
def home(request):
    return render(request, "app/senti.html")

def SentimentAnalysis(request):
    productName = request.GET.get("product" ,'')
    if not productName:
        return JsonResponse({"data":"Product name not given"})
    ScrapeReviewObject = ScrapeAmzonReview()
    try:
        product_url = ScrapeReviewObject.search_amazon_product(productName)
        # print("product_url = " ,product_url)
        product_review = ScrapeReviewObject.scrape_amazon_reviews(product_url)
        print(product_review)
        if len(product_review) != 0:
            gptSummary = GetSummary()
            jsonOutput = gptSummary.get_summary(product_name=productName , review_text=' '.join(product_review))
            print("JSON OUTPUT : " , jsonOutput)
            if(jsonOutput!=None):
                return JsonResponse(json.loads(jsonOutput))
            print("incorrect json response : ",jsonOutput)
        return JsonResponse({"data":f"error getting summary"})
        
        # return JsonResponse({"data":f"Product name recevied : {productName}" ,"review":product_review})
    except Exception as e:
        print(e)
        return JsonResponse({"data":f"Product name recevied : {productName}" ,"review":"No review found"})

