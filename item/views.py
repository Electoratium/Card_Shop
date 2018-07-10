from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *
from landing.models import AuthorModel
from .forms import OrderFormTemplate
from django.core.mail import send_mail
from datetime import datetime




def item(request, itemId):
    form = OrderFormTemplate()

    if not request.POST:
        item = get_object_or_404(ItemModel, pk=itemId, isActive=True)

        itemImages = ItemImages.objects.filter(isActive=True).filter(item__pk=itemId, item__isActive=True)

        itemInfo = GeneralDetails.objects.first()

        author = AuthorModel.objects.first()

        return render(request, 'item.html',
                      {'form': form, 'item': item, 'images': itemImages, 'sendingDetails': itemInfo.sendingDetails, 'author': author})
    else:
        post = request.POST


        if post:
            name = post['name']
            text = post['text']
            email = post['email']
            phone = post['phone']
            itemModel = ItemModel.objects.get(pk = itemId)

            Orders.objects.create(text = text, name = name, email = email, phone = phone, item = itemModel)






            def getData():
                resultData = [itemModel.name]
                for (key, value) in post.items():
                    if not key == "csrfmiddlewaretoken":
                        if value:
                            resultData.append(value)
                        else:
                            resultData.append(' - ')
                resultData.append(datetime.now().strftime("%m-%d %H:%M"))
                return resultData


            values = getData()











            messageText = 'Заказ товара: {0} \n Покупатель: {1} \n Вопрос: {2} \n email: {3} \n вопрос: {4} \n номер телефона: {5} \n время заказа: {6}'.format(
                values[0], values[1], values[2], values[3], values[4], values[5], values[6])

            toEmail = GeneralDetails.objects.first().workEmail


            send_mail(
                'Заказ',
                messageText,
                'rateeva.mail.shop@gmail.com',
                [toEmail],
                fail_silently=False,
            )


            return JsonResponse({'status':200})
        else:
            return JsonResponse({'status':400})
