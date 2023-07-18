from django import forms
from shop.models import  shopComment ,Order
from shop.models import Newsletter
from captcha.fields import CaptchaField
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from shop.models import Calender

class ShopCommentForm(forms.ModelForm):

    class Meta:
        model = shopComment
        fields =['product','name','subject','email','massage']
        
  
class NewsletterForm(forms.ModelForm):
    
    class Meta:
        model = Newsletter
        fields ='__all__'
      
        
class CalenderForm(forms.ModelForm):
    class Meta:
        model = Calender
        fields = ['name', 'date', 'date_time']

    def __init__(self, *args, **kwargs):
        super(CalenderForm, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(label=_('date'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )

        # you can added a "class" to this field for use your datepicker!
        # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})

        self.fields['date_time'] = SplitJalaliDateTimeField(label=_('date time'), 
            widget=AdminSplitJalaliDateTime # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
        )
    
        
