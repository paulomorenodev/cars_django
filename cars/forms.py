from django import forms
from cars.models import Car
    
class CardModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self. cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor minimo do carro deve ser de R$ 20.000,00')
        return value
    
    def clean_factory_year(self):
        factory_year = self. cleaned_data.get('factory_year')
        if factory_year < 1980:
            self.add_error('value', 'Não é possivel cadastrar carros fabricados antes de 1980')
        return factory_year
