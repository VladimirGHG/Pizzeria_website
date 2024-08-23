from django import forms

from .models import Pizza, Burger, Restaurants


class BaseProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["details"].widget = forms.Textarea(attrs={"placeholder": "Details about the product"})

    def clean_score(self):
        score = self.cleaned_data.get("score")
        if score > 10 or score < 0:
            raise forms.ValidationError("Score must be in range of 0-10")
        return score

    def save(self, commit=True, *args, **kwargs):
        product_instance = super().save(commit=False)
        if product_instance.price > 20000:
            product_instance.price = 20000
        if commit:
            product_instance.save()
        return product_instance


class PizzaForm(BaseProductForm):
    class Meta:
        model = Pizza
        fields = ("name", "price", "score", "details", "category", "image")
        help_texts = {"name": "* Ensure to pass the actual product name *"}
        error_messages = {
            "score": {"required": "Make sure to have a valid score"}
        }


class BurgerForm(BaseProductForm):
    class Meta:
        model = Burger
        fields = ("name", "price", "score", "details", "category", "image")
        help_texts = {"name": "* Ensure to pass the actual product name *"}
        error_messages = {
            "score": {"required": "Make sure to have a valid score"}
        }


class RestaurantForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Restaurants
        fields = ("name", "logo", "burgers", "pizzas")
        help_texts = {"name": "* Ensure to pass the actual restaurant name *"}
