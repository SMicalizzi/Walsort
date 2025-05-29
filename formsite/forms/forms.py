from django.db import models
from django import forms


class SimpleForm(forms.Form):
    user_list = []#{}
    user_input = models.CharField(max_length=100)
    new_list = []
    category_list = ["Fresh Produce","Bread","Bakery","Frozen","Grocery","Snacks & Bev","Dairy","Deli","Meat & Seafood","Alcohol"]
    def __str__(self):
        return self.user_list
    def add_item(self, item):
        user_list = self.user_list
        user_list = user_list.append((item.name,item.category))
        return user_list
    def myFunc(self, e):
        x = e[1]
        #x = self.user_list.get(e)
        y = self.category_list.index(x)
        return y
    def sort_list(self):
        new_List = self.user_list
        new_List = sorted(new_List, key = self.myFunc)
        #new_List = list(self.user_list)
        #new_List = sorted(new_List, key = self.myFunc)
        return new_List


class Item(SimpleForm):
    def __init__(self, name, category):
        self._name = name
        self._category = category
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        self._category = category
    
    def getCategoryIndex(self):
        category = self.category
        categoryList = SimpleForm.category_list
        if category in categoryList:
            return categoryList.index(category) + 1
        else:
            return "index not found"