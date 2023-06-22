from django.shortcuts import render

def calculation(request):
    total=0
    per=0
    grade="--"
    data={}
    try:
        if request.method=="POST":
            v1=int(request.POST.get("val1"))
            v2=int(request.POST.get("val2"))
            v3=int(request.POST.get("val3"))
            v4=int(request.POST.get("val4"))
            v5=int(request.POST.get("val5"))

            total=v1+v2+v3+v4+v5
            per=(total/500)*100
            
            if per >= 75:
                grade="O"
            elif per>= 60:
                grade="A"
            elif per>= 40:
                grade="B"
            else:
                grade="F"
            
            data={
                "total":total,
                "per":per,
                "grade":grade
            }

    except:
        data={
            "total":total,
            "per":per,
            "grade":grade
        }

    return render(request,"marksheet.html",data)