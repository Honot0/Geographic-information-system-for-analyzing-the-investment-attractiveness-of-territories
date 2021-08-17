# from .phones import TheCall
from .models import Task3, MapsModel

from django.forms import ModelForm
from django.forms import ModelForm, Textarea, Select, TextInput

class TaskForm(ModelForm):
    class Meta:
        model = Task3
        fields = ["Title","stNumber","ndNumber"]

        widgets = {"Title":Textarea(attrs={'class':'form-control',
                                           'aria-label':'Put here text with phones to extract'
                                           }),
                   "stNumber": TextInput(attrs={'class': 'form-control form-control-lg',
                                            'aria-label': '.form-control-lg example',
                                            'placeholder':'+7 '

                                            }),
                   "ndNumber": TextInput(attrs={'class': 'form-select form-select-lg mb-3',
                                            'aria-label': '.form-select-lg example',
                                            'placeholder': '(123) 456-78-90'
                                            })
                   }


class MapsForm(ModelForm):
    class Meta:
        model = MapsModel
        fields = ["Field1","Field2","Field3"]



        widgets = {"Field1": TextInput(attrs={'placeholder': 'Field1' , "size":"50"
                                              }),
                   "Field2": TextInput(attrs={'placeholder': 'Field2', "size":"50"
                                              }),
                   "Field3": TextInput(attrs={'placeholder': 'Field3', "size":"50"
                                              })


                   }





