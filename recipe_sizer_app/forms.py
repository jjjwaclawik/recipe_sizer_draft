from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'url', 'ingr01name', 'ingr01measunit', 'ingr01measamount', 'ingr02name', 'ingr02measunit', 'ingr02measamount', 'ingr03name', 'ingr04measunit', 'ingr04measamount', 'ingr04name', 'ingr05measunit', 'ingr06measamount', 'ingr06name', 'ingr06measunit', 'ingr07measamount', 'ingr08name', 'ingr08measunit', 'ingr08measamount', 'ingr09name', 'ingr10measunit', 'ingr10measamount', 'ingr10name', 'ingr11measunit', 'ingr12measamount', 'ingr12name', 'ingr12measunit', 'ingr13measamount', 'ingr14name', 'ingr14measunit', 'ingr14measamount', 'ingr15name', 'ingr15measunit', 'ingr15measamount', ]
    # remove read-only owner    fields = ['author', 'name', 'description', 'url', 'owner', 'ingr01name', 'ingr01measunit', 'ingr01measamount', 'ingr02name', 'ingr02measunit', 'ingr02measamount', 'ingr03name', 'ingr04measunit', 'ingr04measamount', 'ingr04name', 'ingr05measunit', 'ingr06measamount', 'ingr06name', 'ingr06measunit', 'ingr07measamount', 'ingr08name', 'ingr08measunit', 'ingr08measamount', 'ingr09name', 'ingr10measunit', 'ingr10measamount', 'ingr10name', 'ingr11measunit', 'ingr12measamount', 'ingr12name', 'ingr12measunit', 'ingr13measamount', 'ingr14name', 'ingr14measunit', 'ingr14measamount', 'ingr15name', 'ingr15measunit', 'ingr15measamount', ]
    