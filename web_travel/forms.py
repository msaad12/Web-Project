from django import forms
from django.forms import widgets


class ResturantReviewForm(forms.Form):

    review = forms.CharField(widget=forms.Textarea)
    rating = forms.IntegerField()