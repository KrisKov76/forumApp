from django import forms


class PersonForm(forms.Form):
    STATUS_CHOICE = (
        (1, 'Draft'),
        (2, 'Published'),
        (3, 'Archived'),
    )

    person_name = forms.CharField(
        label='Кратък текст',
        max_length=10,
        widget=forms.TextInput(attrs={
            'placeholder': 'Въведете име',
            'class': 'form-control'
        })
    )

    # person_name = forms.CharField(
    #     label='Съдържание',
    #     max_length=10,
    #     widget=forms.Textarea,
    # )

    # person_name = forms.CharField(
    #     label='Въведете email',
    #     max_length=10,
    #     widget=forms.EmailInput(attrs={
    #         'placeholder': 'Email'})
    # )

    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'min': 0,
            'max': 120,
            'class': 'form-control'
        })
    )

    is_lecturer = forms.BooleanField()

    status = forms.IntegerField(
        widget=forms.Select(choices=STATUS_CHOICE),
    )

    new_status = forms.IntegerField(
        widget=forms.RadioSelect(choices=STATUS_CHOICE),
    )

    checkboxes = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=STATUS_CHOICE,
    )

    date = forms.DateField()

    file = forms.FileField()

# class PostBaseForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = "__all__"
#
#
# class PostCreateForm(PostBaseForm):
#     pass
#
#
# class PostEditForm(PostBaseForm):
#     pass
#
#
# class PostDeleteForm(PostBaseForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         for field in self.fields:
#             self.fields[field].disabled = True
#
#
# class SearchForm(forms.Form):
#     query = forms.CharField(
#         label='',
#         required=False,
#         max_length=100,
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Search for a post...',
#             }
#         )
#     )


# class PostForm(forms.Form):
#     title = forms.CharField(
#         max_length=100,
#     )
#
#     content = forms.CharField(
#         widget=forms.Textarea,
#     )
#
#     author = forms.CharField(
#         max_length=30,
#     )
#
#     created_at = forms.DateTimeField()
#
#     languages = forms.ChoiceField(
#         choices=LanguageChoice.choices
#     )