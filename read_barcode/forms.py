from django import forms
from .models import Amount


class ProductSearchForm(forms.ModelForm):
    name = forms.CharField(label='商品名', required=False)


class AmountForm(forms.ModelForm):
    amount = forms.IntegerField(label='個数',required=False,
                                widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))

    class Meta:
        model = Amount
        fields = (
            'amount',
        )