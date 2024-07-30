from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MeasureType(models.Model):
    type=models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.type

class Measure(models.Model):
    type=models.ForeignKey(MeasureType,on_delete=models.DO_NOTHING)  #CharField(max_length=20)
    name=models.CharField(max_length=25,blank=True)  #
    abbrev=models.CharField(max_length=15,blank=True)
    def __str__(self):
        return self.name
    
MeasureChoices = ( ("Teaspoons" , "tsp"), 
        ("Table Spoons" , "TBSP"), 
        ("1/4 Cup" , "1/4 Cup"), 
        ("1/3 Cup" , "1/3 Cup"), 
        ("1/2 Cup" , "1/2 Cup"), 
        ("1 Cup" , "Cup"), 
        ("1 Pint" , "Pint"), 
        ("1 Quart" , "Quart"), 
        ("1 Gallon" , "Gallon"),)

class Recipe(models.Model):
    name = models.CharField(max_length=125)
    #owner = owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    
    description = models.CharField(max_length=300)
    # Enhancement - Update to Rich Text editor to store INSTRUCTIONS for combining ingredients, temperature cooking time & etc.
    url = models.URLField(null=True,blank=True)
      
    #Definition of fixed ingredient fields
    #ENHANCEMENT - convert to subtable of ingredients ... requires subforms / subview to display variable length list of ingredients and individual CRUD actions for each ingredient
    ingr01name=models.CharField(max_length=25,blank=True) 
    ingr01measunit=models.CharField(max_length=15,choices=MeasureChoices, blank=True)
        #ingr01measunit=models.ForeignKey(MeasureType,on_delete=models.DO_NOTHING) - relational model
    ingr01measamount=models.CharField(max_length=15,blank=True)

    ingr02name=models.CharField(max_length=25,blank=True) 
    ingr02measunit=models.CharField(max_length=15,choices=MeasureChoices, blank=True)
    ingr02measamount=models.CharField(max_length=15,blank=True) 

    ingr03name=models.CharField(max_length=25,blank=True) 
    ingr04measunit=models.CharField(max_length=15,choices=MeasureChoices, blank=True)
    ingr04measamount=models.CharField(max_length=15,blank=True) 

    ingr04name=models.CharField(max_length=25,blank=True) 
    ingr05measunit=models.CharField(max_length=15,choices=MeasureChoices, blank=True)
    ingr06measamount=models.CharField(max_length=15,blank=True) 

    ingr06name=models.CharField(max_length=25,blank=True) 
    ingr06measunit=models.CharField(max_length=15,choices=MeasureChoices, blank=True)
    ingr07measamount=models.CharField(max_length=15,blank=True) 

    ingr08name=models.CharField(max_length=25,blank=True) 
    ingr08measunit=models.CharField(max_length=15,choices=MeasureChoices, blank=True)
    ingr08measamount=models.CharField(max_length=15,blank=True) 

    ingr09name=models.CharField(max_length=25,blank=True) 
    ingr10measunit=models.CharField(max_length=15,choices=MeasureChoices, blank=True)
    ingr10measamount=models.CharField(max_length=15,blank=True) 

    ingr10name=models.CharField(max_length=25,blank=True) 
    ingr11measunit=models.CharField(max_length=15,choices=MeasureChoices, blank=True)
    ingr12measamount=models.CharField(max_length=15,blank=True) 

    ingr12name=models.CharField(max_length=25,blank=True) 
    ingr12measunit=models.CharField(max_length=15,choices=MeasureChoices, blank=True)
    ingr13measamount=models.CharField(max_length=15,blank=True) 

    ingr14name=models.CharField(max_length=25,blank=True) 
    ingr14measunit=models.CharField(max_length=15,choices=MeasureChoices, blank=True)
    ingr14measamount=models.CharField(max_length=15,blank=True) 

    ingr15name=models.CharField(max_length=25,blank=True) 
    ingr15measunit=models.CharField(max_length=15,choices=MeasureChoices, blank=True)
    ingr15measamount=models.CharField(max_length=15,blank=True) 

    def __str__(self):
        return self.title
    
#""" multi line comment """

"""        makemigrations does not like multiple fields having the same Foreign key relation ... 
        clashes with reverse accessor for
        ERRORS:
    recipe_sizer_app.Measure.type: (fields.E300) Field defines a relation with model 'MeasureType', which is either not installed, or is abstract.      
    recipe_sizer_app.Recipe.ingr01measunit: (fields.E304) Reverse accessor 'MeasureType.recipe_set' for 'recipe_sizer_app.Recipe.ingr01measunit' clashes with reverse accessor for 'recipe_sizer_app.Recipe.ingr02measunit'.
            HINT: Add or change a related_name argument to the definition for 'recipe_sizer_app.Recipe.ingr01measunit' or 'recipe_sizer_app.Recipe.ingr02measunit'.

        ingr02name=models.CharField(max_length=25,blank=True) 
        ingr02measunit=models.ForeignKey(MeasureType,on_delete=models.DO_NOTHING)
        ingr02measamount=models.CharField(max_length=15,blank=True) 
        ingr03name=models.CharField(max_length=25,blank=True) 
        ingr04measunit=models.ForeignKey(MeasureType,on_delete=models.DO_NOTHING)
        ingr04measamount=models.CharField(max_length=15,blank=True) 
        ingr04name=models.CharField(max_length=25,blank=True) 
        ingr05measunit=models.ForeignKey(MeasureType,on_delete=models.DO_NOTHING)
        ingr06measamount=models.CharField(max_length=15,blank=True) 
        ingr06name=models.CharField(max_length=25,blank=True) 
        ingr06measunit=models.ForeignKey(MeasureType,on_delete=models.DO_NOTHING)
        ingr07measamount=models.CharField(max_length=15,blank=True) 
        ingr08name=models.CharField(max_length=25,blank=True) 
        ingr08measunit=models.ForeignKey(MeasureType,on_delete=models.DO_NOTHING)
        ingr08measamount=models.CharField(max_length=15,blank=True) 
        ingr09name=models.CharField(max_length=25,blank=True) 
        ingr10measunit=models.ForeignKey(MeasureType,on_delete=models.DO_NOTHING)
        ingr10measamount=models.CharField(max_length=15,blank=True) 
        ingr10name=models.CharField(max_length=25,blank=True) 
        ingr11measunit=models.ForeignKey(MeasureType,on_delete=models.DO_NOTHING)
        ingr12measamount=models.CharField(max_length=15,blank=True) 
        ingr12name=models.CharField(max_length=25,blank=True) 
        ingr12measunit=models.ForeignKey(MeasureType,on_delete=models.DO_NOTHING)
        ingr13measamount=models.CharField(max_length=15,blank=True) 
        ingr14name=models.CharField(max_length=25,blank=True) 
        ingr14measunit=models.ForeignKey(MeasureType,on_delete=models.DO_NOTHING)
        ingr14measamount=models.CharField(max_length=15,blank=True) 
        ingr15name=models.CharField(max_length=25,blank=True) 
        ingr15measunit=models.ForeignKey(MeasureType,on_delete=models.DO_NOTHING)
        ingr15measamount=models.CharField(max_length=15,blank=True) 
    """



""" draft version code ... with relational tables between recipe and recipe-ingredients 
(replacing with fixed ingredient01 through ingredient15 fields to demonstrate simple CRUD application )
class MeasureType(models.Model):
    type=models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.type

class Measure(models.Model):
    type=models.ForeignKey(MeasureType,on_delete=models.DO_NOTHING)  #CharField(max_length=20)
    name=models.CharField(max_length=25,blank=True)  #
    #nextmeasure=models.CharField(max_length=20)  # Get list from defined measures.name
    nextmeasure=models.ForeignKey(Measure)  #WHERE fk MeasureType = this MeasureType (cascading Picklist) 
    # measure will be used in multiple recipes, don't cascade deletes ,on_delete=models.CASCADE)
    prevmeasure=models.CharField(max_length=20)  # Get list from defined measures.name
    
    
    def __str__(self):
        return self.name
    

    class Recipe(models.Model):
        Recipe=models.ForeignKey(recipe,on_delete=CASCADE)
        Ingredient=models.ForeignKey(ingredient,on_delete=models.CASCADE)   
        #CASCADE -IF- ingredients defined with a one-to-one relationship per-recipe, 
    Otherwise , on_delete=models.DO_NOTHING if there is a subtable of ingredients with a FK relationship
        owner = models.ForeignKey(User,on_delete=models.Cascade)"""